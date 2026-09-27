---
title: "Paper Acceptance Calibration — 2026-09-27"
date: "2026-09-27"
type: reference
tags: [ai-research, curation, arxiv, quality-control]
---

# Paper Acceptance Calibration — 2026-09-27

## Decision Corpus

The review database contains **11,003 decisions**:

- **793 keeps**
- **10,210 rejects**
- No recorded skips

Only 563 decision paths still exist at their recorded locations (562 kept and 1 rejected). Most older rejected paths were removed or moved after review, so the original decision corpus was not sufficient for similarity training by itself.

## Findings

1. **The keep/reject distribution is highly imbalanced.** Similarity separation must not be trusted until at least five kept and five rejected examples are available in the similarity index.
2. **Decision records previously stored only token features.** This lost the title, source, and summary evidence when a reviewed file moved or was deleted.
3. **Generated filenames polluted the learned features.** Long filename-derived tokens appeared in accepted and rejected feature lists and could create false associations.
4. **Benchmark and evaluation terms are not sufficient acceptance evidence.** They occur frequently in rejected papers and must remain subordinate to explicit AI relevance and durable research value.
5. **Agent, harness, coding-agent, safety, and evaluation papers are the strongest recurring areas in the retained set, but application papers still require independent evidence.**
6. **Historical accepted papers should not be retroactively deleted just because the new gate is stricter.** The revised policy applies to future intake unless retrospective cleanup is explicitly authorized.

## Process Changes

- Store a decision-time snapshot of title, source, and summary preview with every future keep/reject decision.
- Use those snapshots as similarity documents when the original file no longer exists.
- Ignore overlong filename-artifact tokens during learned-profile and similarity extraction.
- Keep similarity as a ranking signal only; it cannot override the explicit-interest or durable-value gates.
- Mark keep/reject separation unreliable until both classes have at least five usable examples.
- Preserve separate `keep`, `defer`, and `exclude` semantics at the policy layer while retaining existing database compatibility for `reject` and `skip` records.

## Next Calibration Step

Review a fresh balanced sample of accepted and rejected papers after decision snapshots accumulate. Use it to tune thresholds by precision and false-negative rate rather than by raw keyword frequency.
