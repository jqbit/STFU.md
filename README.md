# STFU.md — Shut The Flip Up

**The 671-byte prompt that cuts coding-agent yap by ~80%.**

Makes your agents shut the flip up.

STFU.md is a drop-in compression prompt for AI assistants. It keeps the useful parts — answers, tools, code, reasoning — and cuts the filler: preambles, hedges, restatements, summaries, postscripts, and “let me know if...” sludge.

Use it anywhere an AI gives you too much yap.

## Tired of ooga-booga concise mode?

We've all seen **caveman mode**: it works because it makes agents stop writing essays. Great idea. Real pain point.

But it also spends prompt tokens making your agent act like a monke.

STFU.md keeps the compression, drops the bit. No roleplay. No persona collapse. No “me fix bug now” energy. Just a tighter communication register for people who want the answer, not a campfire skit.

If your AI keeps doing this:

- “Sure — here’s a comprehensive breakdown...”
- Repeating your question back to you
- Adding five caveats you did not ask for
- Explaining the command after you asked for only the command
- Ending every answer with “let me know if you want me to...”

Then STFU mode is for you.

Caveman-style prompting is reported around **~65% average prose reduction**. STFU.md's 5-agent reference bench hit **−82.1% total prose reduction** with **100% average compliance** — over a 15-point jump without spending the prompt budget on roleplay.

Same goal. Less gimmick. More compliance.

| Approach | What it does | Tradeoff |
|---|---|---|
| Default AI | Polite, padded, exhaustive | slow, expensive, attention tax |
| Caveman mode | Shorter answers via persona | concise, but ooga-booga leakage |
| STFU.md | Shorter answers via output rules | concise without roleplay |

STFU.md is for anyone who has ever thought: **“I asked for the answer, not a TED Talk.”**

## Pick your prompt

| File | Use it for | What it optimizes |
|---|---|---|
| [`STFU.md`](STFU.md) | coding agents, CLIs, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor/Cline rules | terse dev output without breaking tools/code/logic |
| [`STFU.chat.md`](STFU.chat.md) | ChatGPT, Claude, Gemini, Perplexity, web/mobile AI apps, custom instructions | terse general answers without code-agent baggage |

If you write code with agents: use **`STFU.md`**.  
If you mostly chat with AI in a web UI: use **`STFU.chat.md`**.

## Headline

| metric | value |
|---|---|
| coding-agent prompt | **671 bytes** (`STFU.md`) |
| measured reduction | **~80 % less coding-agent prose** |
| communication-only | yes — tools/code/logic unchanged |
| harnesses tested | 11: claude, codex, copilot, droid, hermes, opencode, openclaw, pi, cline, agent/cursor, gemini |
| target | 100 % compliance · ≥ 80 % prose reduction |

See [`data/benchmarks.md`](data/benchmarks.md) for full per-harness numbers + [`data/visualizations/`](data/visualizations/) for charts. Honest gaps documented in [`data/research/critical-findings.md`](data/research/critical-findings.md).

## Install for coding agents

Drop `STFU.md` into the matching instruction slot:

| Agent | Slot |
|---|---|
| Claude Code | `~/.claude/CLAUDE.md` |
| Gemini CLI | `~/.gemini/GEMINI.md` |
| Codex | `~/.codex/AGENTS.md` |
| GitHub Copilot CLI | `~/.copilot/copilot-instructions.md` |
| Factory Droid | `~/.factory/AGENTS.md` |
| Hermes | `~/.hermes/SOUL.md` |
| OpenCode | `~/.opencode/AGENTS.md` |
| OpenClaw | `~/.openclaw/AGENTS.md` |
| Pi | `~/.pi/agent/AGENTS.md` |
| Cline | `~/.cline/data/rules/STFU.md` |
| Cursor Agent | `~/AGENTS.md` |

One-liner deploy across all 11:

```bash
URL=https://raw.githubusercontent.com/jqbit/STFU.md/main/STFU.md
for d in ~/.claude/CLAUDE.md ~/.gemini/GEMINI.md ~/.codex/AGENTS.md \
         ~/.copilot/copilot-instructions.md ~/.factory/AGENTS.md \
         ~/.hermes/SOUL.md ~/.opencode/AGENTS.md ~/.openclaw/AGENTS.md \
         ~/.pi/agent/AGENTS.md ~/.cline/data/rules/STFU.md ~/AGENTS.md; do
  mkdir -p "$(dirname "$d")" && curl -fsSL "$URL" -o "$d"
done
```

## Install for ChatGPT / Claude / Gemini / Perplexity

Copy [`STFU.chat.md`](STFU.chat.md) into your app's custom instructions, project instructions, system prompt, or saved prompt.

Raw URL:

```text
https://raw.githubusercontent.com/jqbit/STFU.md/main/STFU.chat.md
```

Quick copy from terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/jqbit/STFU.md/main/STFU.chat.md
```

## Why this exists

Most AI tools are trained to be “helpful,” which often means verbose. That is expensive in three ways:

- **Time:** more tokens to wait for
- **Money:** more output tokens to pay for
- **Attention:** more fluff to scan

STFU mode fixes the default register. It does not make the model dumber. It makes the model stop narrating obvious things.

## Good outputs feel like this

```text
Cause: port already bound.
Fix: kill process or change PORT.
```

```text
git reset --soft HEAD~1
```

```text
Yes — use SQLite first. Switch when writes/concurrency hurt.
```

## Share line

```text
STFU.md makes your agents shut the flip up — cuts coding-agent yap by ~80%.
```

## License

MIT. See [`LICENSE`](LICENSE).
