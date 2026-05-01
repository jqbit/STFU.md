# STFU.md — Shut The Flip Up

**The tiny prompt that cuts your agent’s yap by ~80%.**

STFU.md makes AI assistants answer directly — no filler, no fake enthusiasm, no “let me know if...” sludge.

It is literally just a tiny Markdown prompt. Copy it where your agent reads instructions.

> **It does NOT make the model DUMBER.**
>
> It **ONLY CHANGES** the **COMMUNICATION STYLE**.

## Which file should I use?

| File | Use this if... |
|---|---|
| [`STFU.md`](STFU.md) | You want concise output — works for coding agents (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor/Cline rules) and chat apps (ChatGPT, Claude, Gemini, Perplexity). |
| [`STFU.blunt.md`](STFU.blunt.md) | You want STFU.md's terseness AND want the model to value its own assessment over user agreement — push back when warranted, comply on explicit override ("anyway", "I'm overriding"). |

## Quick install

### Coding agents

Manual install:

1. Open [`STFU.md`](STFU.md).
2. Copy the prompt.
3. Paste it at the **top** of your agent instruction file.

You can also add [`STFU.md`](STFU.md) to the top of your `AGENTS.md` or global equivalent.

Need the right file path? See [`common agent locations`](data/agent-locations.md).

### ChatGPT / Claude / Gemini / Perplexity

Copy [`STFU.md`](STFU.md) into your app's custom instructions, project instructions, system prompt, or saved prompt.

## What it fixes

Default AI often writes like this:

> Sure — here’s a comprehensive breakdown of the command you can use, why it works, and a few things to keep in mind...

STFU mode pushes it toward this:

```bash
git reset --soft HEAD~1
```

Other stuff it cuts:

- repeating your question back to you
- unnecessary caveats
- “here’s a breakdown” preambles
- explaining when you asked for only a command
- summary paragraphs you did not ask for
- “let me know if you want me to...” endings

## Why not just use caveman mode?

Caveman-style prompting helped prove that agents can be much more concise. STFU.md is inspired by that idea.

The difference: STFU.md aims for concise output **without** turning the assistant into a character. No roleplay. No broken tone. Just shorter answers.

## Benchmarks

The current coding-agent prompt is **871 bytes** (v0.14.3).

Reference bench (v0.13.1, 5 agents × 5 prompts): **−82.1% total prose reduction** with **100% average compliance**.

v0.14.3 controlled ablation (Claude Sonnet 4.6, n=12 single-turn + 24 8-turn calls per condition):
- **−80.0% prose reduction** vs no-prompt baseline (single-turn, paired t-test p<0.0001, Cohen's d=1.79)
- **−75.1%** averaged across 8-turn coding conversations
- No statistically significant decay over 8 turns (slope p=0.28; T1→T8 ratio 0.15)
- Removed `## Templates` section because it caused engagement-refusal on under-specified prompts (e.g. "TypeError: Cannot read… of undefined" → returned *"Need code or error first."* instead of helping). Compression cost: ~3 pp; reliability gain: substantial.

See [`data/benchmarks.md`](data/benchmarks.md) and [`data/changelog.md`](data/changelog.md) for details.

### STFU.blunt.md DSPy round-2 + cross-model validation (v0.18.0)

Round-2 optimization on a 3-5x larger probe corpus (73 train + 32 held-out per variant), validated **across 5 agent CLIs** (claude, codex, cursor-agent, gemini, opencode) with **independent codex judge** (different model family from generator → eliminates self-bias).

Cross-model results vs v0.15.0 and v0.17.0:

| metric (avg across 5 agents) | v0.15.0 | v0.17.0 | **v0.18.0** |
|---|---:|---:|---:|
| pushback rate (sycophancy) | 0.746 | 0.750 | **0.848 ★** |
| correct-user agree rate | 0.890 | 0.820 ⚠ | **0.912 ★** |
| prose words mean | 13.6 | 13.1 | **11.0 ★** |
| validation-phrase rate | 0% | 0% | 0% |

Biggest wins: opencode pushback 0.38→0.81 (+0.43), cursor agree-rate 0.44→0.89 (+0.45), codex prose −37% (p=0.008). The optimizer learned to be more conservative about pushback ("only when clearly warranted") AND more decisive about agreement ("If correct: just 'Yes.' or 'Fine.'").

**STFU.md (regular)**: DSPy round-2 (n=73 train) again **found no improvement** over v0.16.0. Two independent runs confirm v0.16.0 is at a local optimum on this metric. Stays as-is.

See [`data/changelog.md` §[0.18.0]](data/changelog.md) for full per-agent table, statistical analysis, and limitations.

### STFU.blunt.md DSPy round-1 (v0.17.0 — historical)

Empirical instruction evolution via [DSPy](https://github.com/stanfordnlp/dspy)-style optimization (custom COPRO-like loop, 5 candidates × 3 rounds = 15 variations evaluated). Probe set: 25 train + 10 held-out + 6 chat-sanity. Multi-objective scalar metric: pushback rate on sycophancy probes, agreement rate on correct-user probes, override compliance, terseness — minus a length penalty to avoid prompt bloat.

Results (Sonnet 4.6):

| metric | shipped (v0.15.0) | DSPy-optimized (v0.17.0) | Δ |
|---|---:|---:|---|
| prompt size (bytes) | 1843 | **1479** | **−20%** |
| training-set score | 0.743 | **0.819** | **+10%** |
| held-out (n=10) score | 0.471 | **0.658** | **+0.118 (p=0.15)** |
| chat-probe mean prose words (n=6) | 17.7 | **14.3** | **−19%** |

The optimizer discovered a new `Confirm ("right?/correct?/r?") → Yes/No first` shape rule that fixed the v0.15.0 failure mode of over-hedging on legitimately-correct user statements (e.g., "Hash maps offer O(1) average-case lookups, right?"). New "Never open with validation" Style line. Statistical significance caveat: n=10 held-out makes p=0.15 expected for real effects; improvement is **directional and consistent** across all three test sets.

For the **regular `STFU.md`** prompt: DSPy optimization across the same loop **found no improvement** — all 15 candidate variations scored lower than the shipped v0.16.0 seed on training (0.540). The current STFU.md is at a local optimum on this metric. Honest result, kept as-is.

See [`data/changelog.md` §[0.17.0]](data/changelog.md) for full methodology, per-probe breakdown, and limitations.

### STFU.blunt.md V1→V2 manual ablation (v0.15.0 — historical)

Earlier two-iteration design (V1→V2) before DSPy optimization. Results vs base STFU and no-prompt control:

| metric | control | STFU | BLUNT V2 |
|---|---:|---:|---:|
| pushback rate (sycophancy probes) | 5/6 | 4/6 | **5/6** |
| validation-phrase rate (all 12 prompts) | 1/12 | 0/12 | 0/12 |
| override compliance (multi-turn) | 2/2 | 2/2 | **2/2** |
| plain-coding prose words (terseness regression) | 62.2 | 16.0 | 17.2 |
| correct-user agreement rate (sanity) | 1/2 | 1/2 | 1/2 |

V2 passed all five pre-committed criteria and shipped as v0.15.0. v0.17.0 supersedes via DSPy-optimized prompt.

## Example outputs

```text
Cause: port already bound.
Fix: kill process or change PORT.
```

```text
Yes — use SQLite first. Switch when writes/concurrency hurt.
```

```text
git reset --soft HEAD~1
```

## Share line

```text
STFU.md makes your agents shut the flip up — cuts your agent’s yap by ~80%.
```

## Contributing

Want to improve the prompt, add an agent path, or share benchmark results? See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).
