---
title: Below the Noise Floor: Bimodal Seed Collapse and Distinct Failure Modes in Small-Model Knowledge Distillation
url: http://arxiv.org/abs/2608.27729v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_21-40-19Z_BelowtheNoiseFloor_BimodalSeedCollapseandDistinctF.md
generated_at: 2026-08-30 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the reliability of knowledge distillation for small student models in function routing tasks, revealing that gains reported with single seeds are often misleading due to high variance across multiple seeds. The study demonstrates bimodal seed collapse and distinct failure modes such as wrong-function selection, output truncation, and elevated variance, showing that only progressive_kd and rank_kd consistently avoid these issues.

## Key Takeaways
- Per-seed standard deviation for KD variants ranges from 2.8 to 48.7 percentage points, which can swallow any claimed improvement below five points.
- Three of seven KD configurations exhibit bimodal collapse: some seeds drop below 55% accuracy while others train normally, and a fourth shows elevated variance.
- The failure modes are distinct: ce_kd and ce_paraphrase suffer from wrong-function selection, reasoning_kd experiences output truncation with only 0.9% accuracy.

## Context
The findings highlight a critical gap in evaluating small-model knowledge distillation where single-seed results dominate discussions, obscuring broader performance instability. This issue is relevant as many real-world deployments rely on such models without thorough validation across multiple seeds.

## Implications
For practitioners, the paper urges systematic multi‑seed testing to uncover hidden failures and select robust KD methods like progressive_kd or rank_kd. Industry adoption of small student models must therefore incorporate rigorous evaluation protocols to ensure reliable performance gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27729v1)
