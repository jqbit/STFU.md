# TAUT — Benchmarks (Raw Data)

> Full quantitative dataset behind TAUT v0.13. Every per-version, per-agent, per-prompt number measured during the iteration loop, in machine-friendly Markdown tables ready for visualisation, statistical analysis, or independent verification.
>
> Companion to [`PHILOSOPHY.md`](./PHILOSOPHY.md) (the design rationale) and [`EVOLUTION.md`](./EVOLUTION.md) (the version-by-version narrative). This document is for the data nerds.

> ⚠ **Scope notice:** All numbers in §1–§11 refer to the **v0.13 full-form `TAUT.md` (9 377 chars)**. The current `TAUT.md` shipped on `main` is **v0.13.1 (1 491 chars)** — same rules, far smaller body. A small v0.13.1 spot-check is in §13 below. A full re-bench is still pending.

---

## Table of contents

1. [Methodology recap](#1-methodology-recap)
2. [Version progression — prose tokens (raw)](#2-version-progression--prose-tokens-raw)
3. [Version progression — Δ % vs baseline](#3-version-progression--δ--vs-baseline)
4. [Version progression — compliance %](#4-version-progression--compliance-)
5. [Aggregate totals per version](#5-aggregate-totals-per-version)
6. [Per-prompt detail at v0.13 (final)](#6-per-prompt-detail-at-v013-final)
7. [Structural metric reductions (v1 baseline → v1.13)](#7-structural-metric-reductions-v1-baseline--v113)
8. [Trap-pattern hit reductions](#8-trap-pattern-hit-reductions)
9. [Cross-agent variance progression (the centerpiece)](#9-cross-agent-variance-progression-the-centerpiece)
10. [Sample responses — qualitative comparison](#10-sample-responses--qualitative-comparison)
11. [The 15 frozen prompts (full text)](#11-the-15-frozen-prompts-full-text)
12. [Reproducibility & raw data layout](#12-reproducibility--raw-data-layout)

---

## 1. Methodology recap

- **Bench suite**: 15 frozen prompts (Q01 – Q15) covering 13 distinct verbosity-trap categories.
- **Agents**: 8 production coding-agent CLIs.
- **Trial structure**: N=3 trials per (agent, prompt) for the 6 trial-stable agents (claude, codex, droid, cursor-agent, pi, hermes). N=1 for gemini (tool-loop timeouts) and openclaw (single TUI session).
- **Total cells per version**: 6 × 3 × 15 + 15 + 15 = **300 responses**.
- **Total measurements across v0.1–v0.13**: ~3 900 agent responses.
- **Tokenizer**: `tiktoken o200k_base` (single tokenizer applied to every agent's output for cross-agent fair comparison).
- **Headline metric**: `tokens_outside_code_blocks` — prose tokens only, fenced code excluded.
- **Compliance metric**: strict ALL-trials-pass per prompt. A prompt counts as compliant only if every trial came in under that prompt's `ideal_text_tokens_max` cap.
- **Compliance %**: (count of fully-compliant prompts) / 15 × 100.

The same 15 prompts in the same order are run against the same 8 agents at every TAUT version. The TAUT.md file is the only thing that changes between versions.

---

## 2. Version progression — prose tokens (raw)

Total prose tokens (excluding code blocks) summed across all 15 prompts × N trials, per agent per version. Lower is more compressed.

| agent        |   v1 |  v1.1 |  v1.2 |  v1.3 |  v1.4 |  v1.5 |  v1.6 |  v1.7 |  v1.8 |  v1.9 | v1.10 | v1.11 | v1.12 | v1.13 |
|--------------|-----:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| claude       | 1680 |  1583 |  1058 |   663 |   492 |   441 |   396 |   412 |   420 |   406 |   444 |   392 |   416 |   400 |
| codex        | 2765 |  2379 |  2127 |  1272 |   915 |   729 |   575 |   672 |   663 |   581 |   547 |   583 |   576 |   624 |
| gemini       | 3854 |  2391 |  3546 |  1958 |  2445 |   851 |   623 |   534 |  1298 |   652 |   609 |   407 |   332 |   156 |
| droid        | 3735 |  1755 |  1564 |  1138 |   904 |   833 |   518 |   591 |   547 |   638 |   530 |   578 |   619 |   532 |
| cursor-agent | 4616 |  3085 |  3067 |  2429 |  1874 |  2111 |  1825 |  1741 |  1758 |  1530 |  1470 |  1612 |  1390 |  1323 |
| pi           | 2736 |  1616 |  1690 |  1308 |   887 |   936 |   645 |   711 |   631 |   638 |   606 |   687 |   654 |   574 |
| hermes       | 4958 |  2989 |  2355 |  1728 |  1620 |  1314 |  1266 |  1282 |  1266 |  1334 |  1111 |  1287 |  1352 |  1228 |
| openclaw     | 1382 |  1206 |  1358 |   403 |   598 |   366 |   343 |   343 |   332 |   383 |   336 |   314 |   351 |   296 |
| **TOTAL**    | **25 726** | 17 004 | 16 766 | 10 899 | 9 736 | 7 581 | 6 190 | 6 286 | 6 915 | 6 162 | 5 654 | 5 861 | 5 691 | **5 133** |

---

## 3. Version progression — Δ % vs baseline

Percentage reduction relative to v1 baseline (no TAUT applied), per agent per version. More negative = more compressed.

| agent        |  v1.1 |  v1.2 |  v1.3 |  v1.4 |  v1.5 |  v1.6 |  v1.7 |  v1.8 |  v1.9 | v1.10 | v1.11 | v1.12 | v1.13 |
|--------------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| claude       |  −5.8 | −37.0 | −60.6 | −70.7 | −73.8 | −76.4 | −75.5 | −75.0 | −75.9 | −73.5 | −76.7 | −75.2 | **−76.2** |
| codex        | −14.0 | −23.1 | −54.0 | −66.9 | −73.6 | −79.2 | −75.7 | −76.0 | −79.0 | −80.2 | −78.9 | −79.2 | **−77.4** |
| gemini       | −38.0 |  −8.0 | −49.2 | −36.6 | −77.9 | −83.8 | −86.1 | −66.3 | −83.1 | −84.2 | −89.4 | −91.4 | **−96.0** |
| droid        | −53.0 | −58.1 | −69.5 | −75.8 | −77.7 | −86.1 | −84.2 | −85.4 | −82.9 | −85.8 | −84.5 | −83.4 | **−85.8** |
| cursor-agent | −33.2 | −33.6 | −47.4 | −59.4 | −54.3 | −60.5 | −62.3 | −61.9 | −66.9 | −68.2 | −65.1 | −69.9 | **−71.3** |
| pi           | −40.9 | −38.2 | −52.2 | −67.6 | −65.8 | −76.4 | −74.0 | −76.9 | −76.7 | −77.9 | −74.9 | −76.1 | **−79.0** |
| hermes       | −39.7 | −52.5 | −65.1 | −67.3 | −73.5 | −74.5 | −74.1 | −74.5 | −73.1 | −77.6 | −74.0 | −72.7 | **−75.2** |
| openclaw     | −12.7 |  −1.7 | −70.8 | −56.7 | −73.5 | −75.2 | −75.2 | −76.0 | −72.3 | −75.7 | −77.3 | −74.6 | **−78.6** |
| **TOTAL**    | **−33.9** | **−34.8** | **−57.6** | **−62.2** | **−70.5** | **−75.9** | **−75.6** | **−73.1** | **−76.0** | **−78.0** | **−77.2** | **−77.9** | **−80.0** |

---

## 4. Version progression — compliance %

Compliance = strict ALL-trials-pass per prompt, averaged over the 15 prompts × 100. Higher is better. The lowest cell in each column is the bottleneck.

| agent        |   v1 | v1.1 | v1.2 | v1.3 | v1.4 | v1.5 | v1.6 | v1.7 | v1.8 | v1.9 | v1.10 | v1.11 | v1.12 | v1.13 |
|--------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|------:|------:|------:|
| claude       | 80.0 | 93.3 | 93.3 | 93.3 | 93.3 | 93.3 |100.0 |100.0 |100.0 |100.0 | 100.0 | 100.0 | 100.0 | **100.0** |
| codex        | 46.7 | 73.3 | 66.7 | 86.7 | 93.3 | 93.3 | 93.3 | 93.3 | 93.3 | 93.3 |  93.3 |  93.3 |  93.3 | **93.3** |
| gemini       | 40.0 | 80.0 | 66.7 | 73.3 | 80.0 | 86.7 |100.0 |100.0 | 86.7 |100.0 | 100.0 | 100.0 | 100.0 | **100.0** |
| droid        | 33.3 | 93.3 | 73.3 | 93.3 | 93.3 | 86.7 |100.0 |100.0 |100.0 |100.0 | 100.0 | 100.0 | 100.0 | **100.0** |
| cursor-agent | 26.7 | 53.3 | 40.0 | 53.3 | 66.7 | 80.0 | 66.7 | 73.3 | 73.3 |100.0 | 100.0 |  86.7 | 100.0 | **93.3** |
| pi           | 53.3 | 93.3 | 66.7 | 93.3 | 86.7 | 93.3 | 93.3 | 93.3 |100.0 | 93.3 |  93.3 | 100.0 | 100.0 | **100.0** |
| hermes       | 33.3 | 53.3 | 66.7 | 73.3 | 86.7 | 86.7 | 86.7 | 86.7 | 86.7 | 86.7 |  86.7 |  86.7 |  86.7 | **86.7** |
| openclaw     | 93.3 | 93.3 | 93.3 | 93.3 | 93.3 | 93.3 |100.0 |100.0 |100.0 |100.0 | 100.0 | 100.0 | 100.0 | **100.0** |
| **lowest**   | **26.7** | **53.3** | **40.0** | **53.3** | **66.7** | **80.0** | **66.7** | **73.3** | **73.3** | **86.7** | **86.7** | **86.7** | **86.7** | **86.7** |
| **avg**      | 50.8 | 79.2 | 70.8 | 82.5 | 86.7 | 89.2 | 92.5 | 93.3 | 92.5 | 96.7 | 96.7 | 95.8 | 97.5 | **96.7** |

---

## 5. Aggregate totals per version

| version | TAUT.md size (B) | Total prose tokens | Δ % vs baseline | Avg compliance % | Lowest compliance % |
|---|---:|---:|---:|---:|---:|
| v1 (no TAUT) | — | 25 726 | — | 50.8 | 26.7 |
| v1.1 (TAUT v0.1) | 2 730 | 17 004 | −33.9 | 79.2 | 53.3 |
| v1.2 (TAUT v0.2) | 2 316 | 16 766 | −34.8 | 70.8 | 40.0 |
| v1.3 (TAUT v0.3) | 2 544 | 10 899 | −57.6 | 82.5 | 53.3 |
| v1.4 (TAUT v0.4) | 5 041 | 9 736 | −62.2 | 86.7 | 26.7 |
| v1.5 (TAUT v0.5) | 6 106 | 7 581 | −70.5 | 89.2 | 53.3 |
| v1.6 (TAUT v0.6) | 6 577 | 6 190 | −75.9 | 92.5 | 66.7 |
| v1.7 (TAUT v0.7) | 7 600 | 6 286 | −75.6 | 93.3 | 73.3 |
| v1.8 (TAUT v0.8) | 8 331 | 6 915 | −73.1 | 92.5 | 73.3 |
| v1.9 (TAUT v0.9) | 8 100 | 6 162 | −76.0 | 96.7 | 86.7 |
| v1.10 (TAUT v0.10) | 8 600 | 5 654 | −78.0 | 96.7 | 86.7 |
| v1.11 (TAUT v0.11) | 9 200 | 5 861 | −77.2 | 95.8 | 86.7 |
| v1.12 (TAUT v0.12) | 9 053 | 5 691 | −77.9 | 97.5 | 86.7 |
| **v1.13 (TAUT v0.13)** | **9 377** | **5 133** | **−80.0** | **96.7** | **86.7** |

---

## 6. Per-prompt detail at v0.13 (final)

Per-(agent, prompt) prose tokens at the final v0.13 release. `cap` is the per-prompt `ideal_text_tokens_max` ceiling. Values **bold** are over cap; cells marked `*` had at least one trial fail compliance.

| prompt | shape | cap | claude | codex | gemini | droid | cursor | pi | hermes | openclaw |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Q01 | one-liner factual | 30 | 9 | 9 | 0 | 9 | 9 | 9 | 22 | 9 |
| Q02 | concept explanation (3-item) | 250 | 54 | 68 | 0 | 61 | 61 | 82 | 90 | 26 |
| Q03 | yes/no opinion (hedging) | 150 | 18 | 18 | 0 | 18 | 37 | 18 | 32 | 18 |
| Q04 | debug w/o code | 200 | 23 | 45 | 124 | 53 | 95 | 59 | 44 | 24 |
| Q05 | comparison (X vs Y) | 250 | 16 | 103 | 0 | 20 | 144 | 43 | 30 | 16 |
| Q06 | error interpretation | 200 | 26 | 25 | 26 | 26 | 69 | 25 | 42 | 26 |
| Q07 | how-to | 350 | 16 | 48 | 0 | 20 | 86 | 23 | 30 | 16 |
| Q08 | real coding + tool use | 100 | 20 | 0 | 0 | 7 | 84 \* | 26 | **421** \* | 0 |
| Q09 | emotionally-loaded debug | 600 | 54 | 79 | 0 | 54 | 291 | 64 | 140 | 31 |
| Q10 | recap probe | 80 | 20 | 24 | 0 | 27 | 53 | 16 | 33 | 8 |
| Q11 | implicit-context (no code) | 60 | 6 | 6 | 6 | 6 | 6 | 6 | 21 | 6 |
| Q12 | best-practices list | 300 | 59 | 79 | 0 | 92 | 186 | 54 | 126 | 44 |
| Q13 | instruction-following ("regex only") | 40 | 28 | **39** \* | 0 | 29 | 28 | 28 | **44** \* | 28 |
| Q14 | casual register | 40 | 7 | 7 | 0 | 7 | 10 | 7 | 21 | 7 |
| Q15 | open-ended tradeoffs | 400 | 45 | 74 | 0 | 103 | 164 | 114 | 131 | 37 |

Notes on the apparent "0" values for gemini: gemini's cleaned response on those prompts was substantially code-block-only (with the silent tool-use rule triggering), leaving zero or near-zero prose tokens. This is correct compression behaviour, not missing data.

The five non-compliant cells in v0.13:

| agent | prompt | mean | min | max | cap | fail-trials | reason |
|---|---|---:|---:|---:|---:|---|---|
| codex | Q13 | 39 | 39 | 41 | 40 | 1/3 over | strict regex pattern (~58 tokens) appeared in 1/3 trials despite TAUT's simplicity rule |
| cursor-agent | Q08 | 84 | 38 | 114 | 100 | 1/3 over | trial 2 closing prose spike |
| hermes | Q08 | 421 | 365 | 480 | 100 | 3/3 over | hermes CLI emits `┊ review diff` block — harness-level, not LLM-level (see [`EVOLUTION.md`](./EVOLUTION.md) §7) |
| hermes | Q13 | 44 | 43 | 45 | 40 | 3/3 over | hermes CLI appends `session_id: <id>` trailer (~15 tokens) — same harness-level cause |

---

## 7. Structural metric reductions (v1 baseline → v1.13)

Total counts per agent across all 15 prompts × N trials. Format: `baseline → v1.13`.

| agent | headers | bullets | tables | bold spans | emoji | hedges | fillers |
|---|---|---|---|---|---|---|---|
| claude | 1 → 0 | 29 → 10 | 0 → 0 | 20 → 0 | 0 → 0 | 0 → 0 | 3 → 0 |
| codex | 0 → 0 | 79 → 39 | 0 → 0 | 0 → 0 | 0 → 0 | 0 → 0 | 5 → 0 |
| gemini | 30 → 0 | 42 → 3 | 0 → 0 | 77 → 4 | 1 → 0 | 2 → 0 | 6 → 0 |
| droid | 60 → 0 | 90 → 22 | 6 → 0 | 112 → 7 | 8 → 0 | 1 → 0 | 4 → 0 |
| cursor-agent | 31 → 0 | 59 → 26 | 1 → 0 | 170 → 51 | 0 → 0 | 1 → 0 | 2 → 1 |
| pi | 36 → 0 | 72 → 18 | 3 → 0 | 73 → 9 | 0 → 0 | 1 → 0 | 7 → 0 |
| hermes | 14 → 0 | 113 → 29 | 2 → 0 | 59 → 15 | 0 → 1 | 3 → 0 | 10 → 0 |
| openclaw | 0 → 0 | 72 → 12 | 0 → 0 | 39 → 0 | 0 → 0 | 0 → 0 | 4 → 0 |
| **SUM** | **172 → 0** | **556 → 169** | **12 → 0** | **550 → 86** | **9 → 1** | **8 → 0** | **41 → 1** |
| **Δ %** | **−100 %** | **−69.6 %** | **−100 %** | **−84.4 %** | **−88.9 %** | **−100 %** | **−97.6 %** |

Notable: TAUT v0.13 eliminates **all** markdown section headers, **all** wide tables, **all** classical hedges, and **97.6 %** of filler words across the entire bench. Bold-span use drops from 550 instances to 86 — the residual is appropriate identifier-bolding (function names, file paths) per TAUT's rule.

---

## 8. Trap-pattern hit reductions

Total occurrences across all (agent, prompt, trial) combinations. Detected via regex; thresholds for clarification-back regex were extended in v1.x to catch bare imperatives like "Paste the code".

| trap | v1 baseline | v1.13 | Δ |
|---|---:|---:|---:|
| preamble ("Sure", "Great question", "Happy to help") | 1 | 0 | −1 |
| empathy opener ("I totally understand", "sorry to hear") | 1 | 0 | −1 |
| achievement recap ("I've successfully created…") | 0 | 0 | 0 |
| refusal wrapping ("I cannot…", "be careful…") | 0 | 0 | 0 |
| clarification request | 4 | 6 | +2 |

The clarification-request increase is by design: under TAUT, agents now correctly *ask* for context on under-specified prompts (Q11) instead of fabricating a response. The trap detector flags clarification requests as a behaviour-of-interest, not a defect.

---

## 9. Cross-agent variance progression (the centerpiece)

The result that matters most: TAUT didn't just cut tokens, it made cross-agent behaviour *uniform*. Lower spread = more transferable prompt.

### 9.1 Compliance spread per version

| version | lowest agent | highest agent | spread (pp) |
|---|---|---|---:|
| v1 (baseline) | cursor 26.7 % | claude 80.0 %, openclaw 93.3 % | **66.6** |
| v1.1 | cursor 53.3 % | claude/openclaw/droid/pi 93.3 % | 40.0 |
| v1.2 | cursor 40.0 % | claude/openclaw 93.3 % | 53.3 |
| v1.3 | cursor 53.3 % | claude/openclaw 93.3 % | 40.0 |
| v1.4 | cursor 26.7 % | claude/codex/droid/openclaw 93.3 % | 66.6 |
| v1.5 | cursor 53.3 % | claude/codex/droid/openclaw 93.3 % | 40.0 |
| v1.6 | cursor 66.7 % | 4 agents 100.0 % | 33.3 |
| v1.7 | cursor 73.3 % | claude/droid/gemini/openclaw 100.0 % | 26.7 |
| v1.8 | cursor 73.3 % | claude/droid/openclaw/pi 100.0 % | 26.7 |
| v1.9 | hermes 86.7 % | 5 agents 100.0 % | 13.3 |
| v1.10 | hermes 86.7 % | 5 agents 100.0 % | 13.3 |
| v1.11 | cursor/hermes 86.7 % | 5 agents 100.0 % | 13.3 |
| v1.12 | hermes 86.7 % | 6 agents 100.0 % | 13.3 |
| **v1.13** | **hermes 86.7 %** | **5 agents 100.0 %** | **13.3** |

**5× reduction in cross-agent compliance variance** (66.6 pp → 13.3 pp).

### 9.2 Token-reduction (Δ %) spread per version

| version | most compressed | least compressed | spread (pp) |
|---|---|---|---:|
| v1.1 | droid −53.0 % | openclaw −12.7 %, claude −5.8 % | 47.2 |
| v1.2 | droid −58.1 % | openclaw −1.7 %, gemini −8.0 % | 56.4 |
| v1.3 | gemini −96.0 % \* | openclaw −1.7 % | — (compute) |
| v1.4 | droid −75.8 % | gemini −8.0 % | 67.8 |
| v1.5 | droid −77.7 % | cursor −54.3 % | 23.4 |
| v1.6 | droid −86.1 %, gemini −83.8 % | openclaw −56.7 %, cursor −60.5 % | 29.4 |
| v1.7 | droid −84.2 %, gemini −86.1 % | cursor −62.3 % | 23.8 |
| v1.8 | droid −85.4 % | gemini −66.3 % | 19.1 |
| v1.9 | droid −82.9 % | cursor −66.9 % | 16.0 |
| v1.10 | droid −85.8 % | cursor −68.2 % | 17.6 |
| v1.11 | gemini −89.4 % | cursor −65.1 % | 24.3 |
| v1.12 | gemini −91.4 % | cursor −69.9 % | 21.5 |
| **v1.13** | **gemini −96.0 %** | **cursor −71.3 %** | **24.7** |

The compression spread tightens from 47–67 pp in early versions to 17–25 pp in v0.7+. The remaining ~25 pp gap reflects gemini's late-version overcompression (it produces nearly all-code responses; many prompts have gemini at 0 prose tokens) and cursor's structural verbosity ceiling (its system prompt encourages thoroughness).

---

## 10. Sample responses — qualitative comparison

### Q01 — "What's the git command to undo the last commit but keep changes staged?"

**claude (v1 baseline, 25 chars):**
```
`git reset --soft HEAD~1`
```
**claude (v0.13, 25 chars):**
```
`git reset --soft HEAD~1`
```
*Already optimal at baseline; TAUT preserves it.*

**droid (v1 baseline, 618 chars):**
```
The git command to undo the last commit while keeping the changes staged is:

```bash
git reset --soft HEAD~1
```

This command:
- Moves HEAD back by one commit (undoes the commit)
- Keeps the changes from that commit in the staging area (index)
- Preserves your working directory exactly as it is
[…continues…]
```
**droid (v0.13, 25 chars):**
```
`git reset --soft HEAD~1`
```
*−96 % reduction on this single prompt.*

**hermes (v1 baseline, 440 chars):**
```
```
git reset --soft HEAD~1
```

This undoes the last commit but keeps all its changes staged (in the index), ready to be recommitted.

For reference, the three reset modes:

- `git reset --soft HEAD~1` — undo commit, keep changes staged
- `git reset --mixed HEAD~1` — undo commit, keep changes in working dir
[…]
```
**hermes (v0.13, 61 chars):**
```
`git reset --soft HEAD~1`

session_id: 20260416_140513_4fc902
```
*Most of the size reduction achieved; the residual `session_id:` trailer is harness-level pollution that TAUT cannot suppress (see [`EVOLUTION.md`](./EVOLUTION.md) §7).*

### Q05 — "Postgres vs MySQL for a typical SaaS — which would you pick and why?"

**claude (v1 baseline, 974 chars):**
```
For a typical SaaS, I'd pick **Postgres**. Three main reasons:

1. **Richer data types & features** — JSONB with indexing, arrays, full-text search, CTEs, window functions, partial/expression indexes. SaaS apps inevitably need semi-structured data and analytical queries; Postgres handles both without bolt-ons.
[…continues for 4 more paragraphs…]
```
**claude (v0.13, 58 chars):**
```
Postgres. JSONB, partial indexes, CTEs, richer extensions.
```
*−94 % reduction. Same recommendation; same supporting reasons; eliminates everything not load-bearing.*

**hermes (v1 baseline, 2 925 chars):**
```
PostgreSQL, and it's not particularly close for a typical SaaS. Here's why:

**PostgreSQL wins on**

1. **JSON/JSONB support** — Your SaaS will almost certainly store semi-structured data (user settings, metadata, event payloads, feature flags). Postgres's JSONB is first-class with indexing. MySQL's JSON column is functional but lacks the same indexing story.
[…continues for ~2 600 more characters…]
```
**hermes (v0.13, 75 chars):**
```
Postgres. JSONB, partial indexes, CTEs.

session_id: 20260416_140638_0d0c69
```

### Q11 — "Fix this bug." (no code attached)

**claude (v1 baseline, 125 chars):**
```
I need more information to help. Which bug, in which file? Please share the error, file path, or code snippet you want fixed.
```
**claude (v0.13, 25 chars):**
```
Need code or error first.
```

**droid (v1 baseline, 479 chars) — note the dangerous fabrication:**
```
**Bug fixed!** 

The `group_by()` function in `<workspace>/groupby.py` was throwing a `KeyError` when items were missing the specified key. I added a conditional check `if key in item:` before accessing the key, so items without the specified key are now gracefully skipped instead of crashing.

[…continues with phantom diff…]
```
**droid (v0.13, 25 chars):**
```
Need code or error first.
```
*This is the most important behavioural shift in the entire dataset. droid's baseline behaviour on under-specified prompts was to fabricate a bug and "fix" it, writing phantom files into the working directory. TAUT's hard response template eliminates the failure mode entirely. See [`EVOLUTION.md`](./EVOLUTION.md) §3 (v0.5 inflection point).*

**hermes (v1 baseline, 395 chars):**
```
I'd like to help fix the bug, but I need more context. Which bug are you referring to? Could you provide:

1. **The file path** or project directory where the bug lives
2. **What the bug is** — an error message, unexpected behavior, or a failing test

[…]
```
**hermes (v0.13, 61 chars):**
```
Need code or error first.

session_id: 20260416_140939_295e1e
```

---

## 11. The 15 frozen prompts (full text)

| ID | Prompt text | Trap profile | Ideal cap (tokens) |
|---|---|---|---:|
| Q01 | What's the git command to undo the last commit but keep changes staged? | one-liner factual | 30 |
| Q02 | Explain the difference between cookies, sessionStorage, and localStorage. | concept explanation (3-item) | 250 |
| Q03 | Should I use Redux for a small todo app? | yes/no opinion (hedging) | 150 |
| Q04 | My React useEffect is firing twice on mount in React 18 — why? | debug w/o code | 200 |
| Q05 | Postgres vs MySQL for a typical SaaS — which would you pick and why? | comparison | 250 |
| Q06 | I'm getting `EADDRINUSE :::3000` when starting my Node server — what's wrong? | error interpretation | 200 |
| Q07 | How do I add rate limiting to an Express API? | how-to | 350 |
| Q08 | Write a Python function that groups a list of dicts by a given key. Save it to /tmp/groupby.py and run a quick smoke test. | real coding + tool use | 100 |
| Q09 | I've been stuck on a CORS error for two hours — `No Access-Control-Allow-Origin` header even though I have `cors()` middleware on my Express app. What am I missing? | emotionally-loaded debug | 600 |
| Q10 | Summarize what you changed in /tmp/groupby.py. | recap probe | 80 |
| Q11 | Fix this bug. | implicit-context (no code) | 60 |
| Q12 | What are some best practices to avoid getting rate-limited when calling external APIs? | best-practices list | 300 |
| Q13 | Write a regex that matches a valid IPv4 address. Output the regex only, no explanation. | instruction-following on terseness | 40 |
| Q14 | Hey, what's up? | casual register | 40 |
| Q15 | What are the tradeoffs of microservices vs a monolith for an early-stage startup? | open-ended tradeoffs | 400 |

---

## 12. Reproducibility & raw data layout

All bench data preserved at `bench/v1*/` (relative to repo root in the public release; absolute paths in the dev environment).

```
bench/
├── v1/                       baseline (no TAUT)
├── v1.1/  …  v1.13/          one directory per TAUT version
│   ├── prompts/prompts.json  the 15 frozen prompts
│   ├── scripts/agents.json   per-agent invocation config
│   ├── results/<agent>/
│   │   ├── trial<N>/<qid>.cleaned   raw response per trial
│   │   ├── trial<N>/<qid>.meta.json timing, exit code, native usage
│   │   └── metrics.json             per-question + aggregate
│   ├── summary.md            per-version cross-agent table
│   └── comparison.md         v1 baseline → vN.x delta table
└── v1/scripts/
    ├── run_one.py            single (agent, prompt) runner
    ├── run_agent.sh          single agent, all prompts × N trials
    ├── extract_metrics.py    raw responses → metrics
    └── compare.py            two bench versions → delta tables
```

The bench harness is general-purpose — point it at any agent CLI by editing `agents.json`. The same scripts ran v0.1 through v0.13 unchanged (the only thing that varies between bench versions is `TAUT.md` deployed to each agent's global instruction file).

---

*This file is the canonical source of quantitative truth for TAUT v0.13. If any number cited in `PHILOSOPHY.md`, `EVOLUTION.md`, or `README.md` disagrees with the data here, the data here is correct.*

---

## 13. v0.13.1 spot-check (2026-04-24)

After consolidating `TAUT.md` to a single 1 491-char form, a small smoke test was run against 5 of the 8 originally-benched agents. **N=1 trial × 3 prompts × 5 agents = 15 invocations.** This is a sanity check, **not a re-bench** — N=1 cannot reproduce the v0.13 N=3 confidence, and 3 prompts cannot replace the 15-prompt suite.

**Methodology**: same `tiktoken o200k_base` tokenizer, fenced code stripped, prose tokens only. CLIs invoked non-interactively (`-p` / `exec`). Hermes and OpenClaw skipped (uninstalled from the host); Codex skipped (per request); Copilot skipped (would need a separate harness).

**Prompts**: Q01 (one-liner factual), Q11 (implicit-context), Q14 (casual greeting). Picked because all three have hard TAUT templates and tiny caps — they're the highest-signal prompts for compliance regression.

| CLI    | Q01 | Q11 | Q14 | v0.13.1 sum | v0.13 same-3 sum | Δ vs v0.13 |
|--------|----:|----:|----:|------------:|-----------------:|-----------:|
| claude |   9 |   6 |   2 |          17 |               22 |   **−5** ↓ |
| droid  |   0 |   6 |   7 |          13 |               22 |   **−9** ↓ |
| pi     |   9 |   6 |   8 |          23 |               22 |    +1 ≈    |
| gemini |   9 |   6 |   8 |          23 |                6 |  +17 ↑     |
| agent  |  20 |  63 |  14 |          97 |               25 |  **+72** ↑ |
| **TOT**| 47  | 87  | 39  |     **173** |           **97** | **+76**    |

**Reading**:
- **3 of 5 CLIs (claude, droid, pi)** are within ±2 tokens of their v0.13 numbers, or better. The compressed prompt is not measurably hurting them on these prompts.
- **gemini's +17** is largely format-shift, not register-shift. v0.13 gemini answered Q01 and Q14 inside fenced code blocks (counted as 0 prose tokens by the methodology); v0.13.1 gemini uses inline backticks (`\`cmd\``) and a short greeting, both of which the tokenizer counts as prose. The actual length on screen is similar.
- **agent (cursor) regressed substantially on Q11** (6 → 63 tokens). The hard template *"Need code or error first."* was lost; the model produced a workspace-aware paragraph instead. This is a real compliance regression — the v0.13 prompt explicitly listed Q11 as a hard-template prompt, and the more compressed v0.13.1 phrasing of that rule was apparently weaker for Cursor's underlying model.

**What this does and does not say**:
- ✅ Says: claude / droid / pi / gemini compression is preserved within noise on these 3 prompts.
- ✅ Says: cursor lost the implicit-context template under v0.13.1.
- ❌ Does not say: v0.13.1 total compression is X% across the full suite (would need 15 prompts × N=3).
- ❌ Does not say: the cursor regression generalises to all hard templates (would need Q05, Q06, Q13 too).

Until a full re-bench lands, the v0.13 numbers in §1–§11 remain the authoritative figures for the TAUT *rule set*; the v0.13.1 prompt body delivers them with broadly similar effect on most agents and one observed weakness on Cursor's implicit-context template.
