<div align="center">

# TAUT 🪡

**TAUT** *(taut, adj.)* — pulled tight; not slack.
*Also a backronym: **T**erse **A**gent **U**tterance **T**uning.*

### A 1.5 KB system prompt that cuts AI coding-agent output by ~80%

No fine-tuning. No API change. No harness change. **Just one Markdown file** dropped into your agent's global instruction slot.

[![release](https://img.shields.io/github/v/release/jqbit/TAUT?style=flat-square&color=blue&label=release)](https://github.com/jqbit/TAUT/releases)
[![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![agents](https://img.shields.io/badge/agents-5-orange?style=flat-square)](#-supported-agents)
[![reduction](https://img.shields.io/badge/output_reduction-77--87%25-red?style=flat-square)](#-benchmark)
[![compliance](https://img.shields.io/badge/compliance-100%25_(5/5_agents)-brightgreen?style=flat-square)](#-benchmark)
[![stars](https://img.shields.io/github/stars/jqbit/TAUT?style=flat-square&color=yellow)](https://github.com/jqbit/TAUT/stargazers)
[![last commit](https://img.shields.io/github/last-commit/jqbit/TAUT?style=flat-square)](https://github.com/jqbit/TAUT/commits/main)

**Works with:** Claude Code · Google Gemini · Factory Droid · Pi Coding Agent · Cursor Agent

</div>

---

## ⚡ Why TAUT?

Modern AI coding agents are RLHF-trained to be *helpful*, which makes them **verbose by default** — preambles, hedges, "when to use which" closers, security postscripts you didn't ask for. Output tokens are 3–5× the price of input. Latency scales linearly with output length. Reading 600 tokens to extract one command costs the most expensive token rate of all: **your attention**.

**TAUT fixes that.** One 1.5 KB file. Five agents tested. ≥77 % output reduction on every one. 100 % compliance with hard prompt-shape caps.

---

## 📊 Benchmark (v0.13.1 — 5 agents × 5 prompts × N=1)

| Agent       | Baseline (no TAUT) | With TAUT v0.13.1 | **Δ %**     | Compliance |
|-------------|-------------------:|------------------:|------------:|-----------:|
| **gemini**  |              1 008 |               133 | **−86.8 %** | 100 % (5/5)|
| **pi**      |                967 |               153 | **−84.2 %** | 100 % (5/5)|
| **claude**  |                599 |               119 | **−80.1 %** | 100 % (5/5)|
| **agent**\* |                640 |               140 | **−78.1 %** | 100 % (5/5)|
| **droid**   |                601 |               136 | **−77.4 %** | 100 % (5/5)|
| **TOTAL**   |          **3 815** |             **681** | **−82.1 %** | avg **100 %** |

> 5 agents · 5 prompts (Q01 one-liner / Q05 comparison / Q06 error / Q11 implicit-context / Q14 greeting) · N=1 trial · `tiktoken o200k_base` cross-agent fair tokenizer · empty cwd per cell to control for autonomous workspace inspection. Each agent invoked non-interactively (`-p` / `exec`). Droid Q06 + Q11 baseline = DNF (droid hangs without TAUT on under-specified prompts; excluded from droid's reduction calc — 3 prompts only). Full data in [`BENCHMARKS.md` §14](./BENCHMARKS.md#14-v0131-five-agent-bench-2026-04-24).

\* **Cursor Agent**: TAUT compliance depends on the cursor model. The default `composer-2-fast` does NOT respect TAUT's hard templates (it always describes workspace state and adds tips). Use `agent --model gpt-5.3-codex -p ...` (or `gpt-5.2`) for the figures shown — these models follow the TAUT register cleanly. See [`AGENT-LOCATIONS.md` §Cursor](./AGENT-LOCATIONS.md#cursor-agent) for a wrapper alias.

---

## 🚀 Install — pick your agent, run one line

Each command downloads `TAUT.md` from this repo and writes it to the agent's global instruction file path. No clone, no script, just `curl`.

```bash
# Claude Code
mkdir -p ~/.claude && curl -fsSL https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md -o ~/.claude/CLAUDE.md

# Google Gemini
mkdir -p ~/.gemini && curl -fsSL https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md -o ~/.gemini/GEMINI.md

# Factory Droid
mkdir -p ~/.factory && curl -fsSL https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md -o ~/.factory/AGENTS.md

# Pi Coding Agent
mkdir -p ~/.pi/agent && curl -fsSL https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md -o ~/.pi/agent/AGENTS.md

# Cursor Agent
curl -fsSL https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md -o ~/AGENTS.md
```

<details>
<summary><b>Install all five at once</b></summary>

```bash
TAUT_URL=https://raw.githubusercontent.com/jqbit/TAUT/main/TAUT.md
for d in ~/.claude/CLAUDE.md ~/.gemini/GEMINI.md ~/.factory/AGENTS.md ~/.pi/agent/AGENTS.md ~/AGENTS.md; do
  mkdir -p "$(dirname "$d")" && curl -fsSL "$TAUT_URL" -o "$d"
done
```
</details>

### Smoke test (any agent)

```bash
claude -p "What's the git command to undo the last commit but keep changes staged?"
# expect: `git reset --soft HEAD~1`   (and nothing else)
```

If you see a paragraph instead of one line, the file isn't loading. See [`AGENT-LOCATIONS.md`](./AGENT-LOCATIONS.md#verification-command).

---

## 📁 What's inside

| File | Purpose |
|---|---|
| [`TAUT.md`](./TAUT.md) | The prompt itself (1 521 chars) |
| [`AGENT-LOCATIONS.md`](./AGENT-LOCATIONS.md) | Per-agent deploy paths + verification |
| [`PHILOSOPHY.md`](./PHILOSOPHY.md) | Design rationale, ML grounding, cited research |
| [`EVOLUTION.md`](./EVOLUTION.md) | v0.1 → v0.13 journey, what worked, what didn't |
| [`BENCHMARKS.md`](./BENCHMARKS.md) | Full raw data — every per-version per-agent number |
| [`CHANGELOG.md`](./CHANGELOG.md) | Version-by-version headline metrics |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | How to add agents, run benchmarks, propose changes |

---

## 🤖 Supported agents

```
1. Claude Code (Anthropic)        →  ~/.claude/CLAUDE.md
2. Google Gemini CLI              →  ~/.gemini/GEMINI.md
3. Factory Droid                  →  ~/.factory/AGENTS.md
4. Pi Coding Agent                →  ~/.pi/agent/AGENTS.md
5. Cursor Agent CLI               →  ~/AGENTS.md  (use --model gpt-5.3-codex)
```

Same file, five agents, ≥77 % output reduction across the lot at 100 % compliance with the v0.13.1 5-prompt suite.

---

## 💡 What TAUT actually does

- **Hard numerical caps** on response length per prompt-shape (one-liner ≤ 20 tokens, comparison ≤ 70, best-practices list ≤ 120, etc.)
- **Hard response templates** for under-specified prompts ("Fix this bug." → *"Need code or error first."*)
- **Structural caps** (headers, tables, bold, bullets, emoji)
- **Anti-helpfulness rule** — no unsolicited security postscripts, no "when to use which" closers
- **Tool-use silence** — code/file writes execute without narration
- **Self-trim & draft-then-halve** rules — meta-cognitive compression loops

---

## ❓ FAQ

<details>
<summary><b>Will TAUT make my agent dumber?</b></summary>

No — and there's published evidence brevity *improves* accuracy. The "Brevity Constraints Reverse Performance Hierarchies in Language Models" paper (cited in [`PHILOSOPHY.md`](./PHILOSOPHY.md) §6) found that constraining models to brief responses improved accuracy by up to 26 percentage points on certain benchmarks. Verbose answers give the model more room to be wrong, contradict itself, or wander. Tighter answers stay on-target.
</details>

<details>
<summary><b>How is this different from just saying "be concise"?</b></summary>

"Be concise" has no measurable success criterion. TAUT specifies **numerical caps per prompt-shape** ("max 16 words per sentence", "comparison = 1 sentence pick + 0 supporting clauses"), **hard response templates** for high-variance prompts, and **structural caps** (max 1 bullet list, ≤6 words per bullet). RLHF-trained models follow checkable rules ~25 percentage points better than they follow stylistic suggestions. See [`EVOLUTION.md`](./EVOLUTION.md#3-key-inflection-points) §3.
</details>

<details>
<summary><b>Why not just use caveman?</b></summary>

Caveman's compression mechanics work — they're the foundation TAUT builds on. The problem is the *caveman persona*. Under heavy "caveman" framing, several models personify the character ("ugh, caveman ready", "ooga booga project info?"). This burns tokens on roleplay, drifts latent representations toward a stereotyped subspace ([Shanahan et al., *Nature*, 2023](https://www.nature.com/articles/s41586-023-06647-8)), and reads as unprofessional in production contexts. TAUT keeps caveman's compression and replaces the persona with a senior-engineer register. Full rationale in [`PHILOSOPHY.md`](./PHILOSOPHY.md#3-the-caveman-personification-problem-the-reason-taut-exists) §3.
</details>

<details>
<summary><b>Does TAUT work on agents that aren't in your list?</b></summary>

Probably yes, with caveats. `TAUT.md` is a generic system prompt — any agent that loads a global Markdown instruction file will read it. The five agents listed are the ones tested in v0.13.1. If you try it on another agent (Aider, Continue, Sweep, Hermes, OpenClaw, Codex CLI, Copilot CLI, etc.), please [open a compatibility report](./.github/ISSUE_TEMPLATE/agent-compatibility.md). The v0.13 8-agent bench (with the older 9 377-char prompt) is preserved in [`BENCHMARKS.md`](./BENCHMARKS.md) §1–§11 for historical reference.
</details>

<details>
<summary><b>Why does cursor need a model flag?</b></summary>

Cursor's default model `composer-2-fast` is RLHF-trained to always provide workspace context, alternative-command tips, and explanatory closers — even when the system prompt explicitly forbids them. With TAUT v0.13.1 it lands at ~30 % reduction (compared to ~80 % for the four other agents). Switching to `gpt-5.3-codex` or `gpt-5.2` (`agent --model gpt-5.3-codex -p ...`) restores the figures in the benchmark table. The recommended alias is `alias cursor-agent='agent --yolo --model gpt-5.3-codex'`.
</details>

<details>
<summary><b>What if I want it on only some prompts, not always?</b></summary>

TAUT has built-in override clauses: it explicitly resumes full verbosity for security warnings, destructive-action confirmations, or when the user says "I don't understand". You can also just say *"verbose mode"* or *"disable TAUT"* in any turn. See `TAUT.md` §Override + §Persistence.
</details>

<details>
<summary><b>Will TAUT bloat my input tokens?</b></summary>

`TAUT.md` is 1 521 bytes ≈ ~400 tokens (down from ~2 000 in v0.13). Every major API supports prompt caching (Anthropic, OpenAI, Google) at ~90 % input-cost reduction on cached prefixes. Loaded once per session, TAUT pays for itself within ~1–2 turns of normal usage and saves dramatically more from there. Long-running terminals (`claude` opened once, used many turns) maximise the cache hit rate.
</details>

<details>
<summary><b>Can I customise TAUT for my team's style?</b></summary>

Absolutely. `TAUT.md` is just a Markdown file — fork it, edit it, deploy your fork. The compression mechanics are stable; the register, examples, and per-prompt-shape caps are all tunable. See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for how to bench your variant.
</details>

---

## 🎓 Origin

Inspired by **[caveman](https://github.com/JuliusBrussee/caveman)** by Julius Brussee — the first widely-shared prompt to take output-side compression seriously. TAUT diverges from caveman by replacing the caveman *persona* with a senior-engineer *register* that preserves caveman-grade compression without the personification, token-waste-on-character-maintenance, or production-unsuitable voice. Full credit and design-divergence rationale in [`PHILOSOPHY.md`](./PHILOSOPHY.md#2-inspiration-caveman) §2-§3.

---

## 🌟 Star this repo if it saved you tokens.

[![star history](https://img.shields.io/github/stars/jqbit/TAUT?style=social)](https://github.com/jqbit/TAUT/stargazers)

Issues + PRs welcome. Particularly interested in:
- Agent-compatibility reports for CLIs not in the supported-5 list
- Per-cursor-model bench data
- Variance / methodology improvements
- Translations of the prompt suite to non-English contexts

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for how to add agents, run benchmarks, and propose changes.

---

## 📚 Citation

```
TAUT — Terse Agent Utterance Tuning (v0.13.1).
5-agent cross-CLI compression benchmark, 2026.
https://github.com/jqbit/TAUT
Inspired by caveman (Julius Brussee, 2026).
```

GitHub auto-renders a "Cite this repository" button from [`CITATION.cff`](./CITATION.cff).

---

## License

[MIT](./LICENSE). Free for commercial and personal use.

---

<div align="center">

**Keywords**: AI coding agent · LLM system prompt · prompt engineering · token reduction · output compression · Claude Code prompt · Gemini prompt · Cursor agent prompt · Factory Droid prompt · agentic AI · prompt optimization · LLMOps · Anthropic Claude prompt · Google Gemini prompt · concise output · terse AI · brevity constraints · LLM cost reduction · production AI · AI engineering

*Built with iteration, measurement, and respect for the reader's time.*

</div>
