---
title: Whose Gold? Annotator-Pool Disagreement Is Large at the Item Level, and Hidden by Small Leaderboards
url: http://arxiv.org/abs/2608.15980v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_00-19-52Z_WhoseGold_Annotator_PoolDisagreementIsLargeattheIt.md
generated_at: 2026-08-17 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates disagreement between annotator pools and benchmark authors on preference items, showing that while item‑level disagreements are high, model leaderboards remain identical. The study also demonstrates that the observed invariance is a statistical artifact rather than evidence of robustness.

## Key Takeaways
- On unanimous items, expert and crowd annotators disagree at 23.6% (different majority) and reverse on 8.5%, yet aggregated leaderboards show zero displacement.
- Model win rates shift by only ~1.9 percentage points when pools are swapped, indicating weak sensitivity to annotation pool changes.
- A ten‑model leaderboard is displaced with probability 0.86 under the same perturbation, showing that small leaderboards can appear stable but larger ones are vulnerable.

## Context
Preference benchmarking relies on aggregating diverse annotator judgments; this study reveals that reported consensus may mask underlying variability. Understanding these dynamics is crucial for trustworthy model evaluation and for recognizing that stability in leaderboards does not guarantee reliable ranking.

## Implications
For industry practitioners, this means that leaderboard rankings may not reflect true model performance and could mislead product decisions. Researchers should examine annotation noise rather than assume aggregation yields robust results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15980v1)
