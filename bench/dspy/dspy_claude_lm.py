"""Custom dspy.LM that wraps `claude -p` CLI (for environments without API key)."""
import json
import subprocess
import time
from typing import Any
import dspy
from litellm.types.utils import ModelResponse, Choices, Message, Usage


class ClaudeCLILM(dspy.LM):
    """dspy.LM subclass that calls `claude -p` instead of using litellm/API."""

    def __init__(self, system_prompt: str = "", model: str = "sonnet", max_tokens: int | None = 4096, temperature: float = 0.7, **kwargs):
        # Bypass parent init's litellm config — we don't need it
        self.model = f"claude-cli-{model}"
        self.cli_model = model
        self.system_prompt = system_prompt
        self.model_type = "chat"
        self.cache = False  # we handle caching ourselves
        self.kwargs = {"temperature": temperature, "max_tokens": max_tokens}
        self.history = []
        self.num_retries = 1
        self.callbacks = []
        self.provider = None
        self.use_developer_role = False
        self.finetuning_model = None
        self.launch_kwargs = {}
        self.train_kwargs = {}

    def forward(self, prompt: str | None = None, messages: list[dict] | None = None, **kwargs):
        if messages is None and prompt:
            messages = [{"role": "user", "content": prompt}]
        if not messages:
            raise ValueError("Empty messages")

        # Extract system prompt from messages if present, else use self.system_prompt
        sys_msg = self.system_prompt
        user_chunks = []
        for m in messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if role == "system":
                sys_msg = content if not sys_msg else sys_msg + "\n\n" + content
            else:
                user_chunks.append(content)
        user_message = "\n\n".join(user_chunks)

        # Build claude CLI call
        cmd = ["claude", "-p", "--output-format", "json", "--no-session-persistence",
               "--model", self.cli_model]
        if sys_msg:
            cmd += ["--append-system-prompt", sys_msg]
        cmd += [user_message]

        for attempt in range(3):
            try:
                proc = subprocess.run(cmd, capture_output=True, timeout=120, text=True)
                if proc.returncode != 0:
                    if attempt < 2:
                        time.sleep(2)
                        continue
                    raise RuntimeError(f"claude CLI failed: {proc.stderr[:500]}")
                data = json.loads(proc.stdout)
                if data.get("is_error"):
                    raise RuntimeError(f"claude CLI error: {data}")
                response_text = data.get("result", "")
                usage_data = data.get("usage", {})
                # Build litellm-shaped response
                resp = ModelResponse(
                    id=data.get("session_id", "unknown"),
                    choices=[Choices(message=Message(content=response_text, role="assistant"), finish_reason="stop", index=0)],
                    model=self.model,
                    usage=Usage(
                        prompt_tokens=usage_data.get("input_tokens", 0),
                        completion_tokens=usage_data.get("output_tokens", 0),
                        total_tokens=usage_data.get("input_tokens", 0) + usage_data.get("output_tokens", 0),
                    ),
                )
                return resp
            except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
                if attempt < 2:
                    time.sleep(2)
                    continue
                raise RuntimeError(f"claude CLI failed: {e}") from e

    def __call__(self, *args, **kwargs):
        # dspy may call as lm("prompt") or lm(messages=...)
        return self.forward(*args, **kwargs)


if __name__ == "__main__":
    lm = ClaudeCLILM()
    resp = lm.forward(prompt="say 'hello' in two words")
    print("Response:", resp.choices[0].message.content)
    print("Usage:", resp.usage)
