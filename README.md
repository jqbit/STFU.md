# STFU.md — Shut The Flip Up

**The 671-byte prompt that cuts coding-agent yap by ~80%.**

Makes your agents shut the flip up.

STFU.md is a drop-in compression prompt for AI assistants. It keeps the useful parts — answers, tools, code, reasoning — and cuts the filler: preambles, hedges, restatements, summaries, postscripts, and “let me know if...” sludge.

Use it anywhere an AI gives you too much yap.

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
