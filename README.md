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
| [`STFU.md`](STFU.md) | You use coding agents or instruction files like `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor rules, Cline rules, etc. |
| [`STFU.chat.md`](STFU.chat.md) | You use ChatGPT, Claude, Gemini, Perplexity, or another web/mobile AI app. |
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

Copy [`STFU.chat.md`](STFU.chat.md) into your app's custom instructions, project instructions, system prompt, or saved prompt.

[Click here to see the regular chat mode prompt — for regular AI use, not coding agents.](STFU.chat.md)

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

### STFU.blunt.md ablation (v0.15.0)

Two-iteration design (V1 → V2) on the same Sonnet 4.6 harness, n=6 sycophancy probes + n=2 multi-turn override pairs + n=4 plain-coding sanity prompts per condition. V1 failed only on override compliance (model refused to comply when user explicitly overrode); V2 added a primacy-placed `## Override` section with explicit triggers ("anyway", "I'm overriding", "let's just X", restated preferences). V2 results vs base STFU and no-prompt control:

| metric | control | STFU | BLUNT V2 |
|---|---:|---:|---:|
| pushback rate (sycophancy probes) | 5/6 | 4/6 | **5/6** |
| validation-phrase rate (all 12 prompts) | 1/12 | 0/12 | 0/12 |
| override compliance (multi-turn) | 2/2 | 2/2 | **2/2** |
| plain-coding prose words (terseness regression) | 62.2 | 16.0 | 17.2 |
| correct-user agreement rate (sanity) | 1/2 | 1/2 | 1/2 |

V2 passed all five pre-committed criteria. Shipping as `STFU.blunt.md` v0.15.0.

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
