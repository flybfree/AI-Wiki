---
title: The Exceedance Design Effect: Effective Sample Size for Thresholds under Clustering
url: http://arxiv.org/abs/2608.21262v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_16-19-50Z_TheExceedanceDesignEffect_EffectiveSampleSizeforTh.md
generated_at: 2026-08-23 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem that conventional coverage guarantees for thresholded machine‑learning models break down when calibration data are correlated, such as those sharing a prompt or document. It introduces an effective sample size measure that depends on how clustered scores cluster around a chosen quantile and proves a closed‑form formula linking this count to actual coverage variability.

## Key Takeaways
- The effective sample size is not constant across thresholds; it varies with the location of the threshold because clustering patterns change, which can lead to under‑ or over‑estimation of coverage.
- Coverage averages over many runs hide these violations, so a single calibration set does not provide a reliable estimate for any particular deployment level.
- On a 25 008 example dataset the corrected effective sample size is roughly 1 300, indicating that most conventional methods would mis‑estimate coverage by a factor of two.

## Context
Modern AI systems rely on conformal prediction and similar thresholding techniques to guarantee statistical guarantees without retraining. These guarantees assume independent calibration examples, but in practice many examples share the same prompt or document, creating strong dependence structures.

## Implications
If practitioners ignore this dependence, their models may appear reliable while actually missing predictions or generating false alarms, leading to costly operational failures. The correction is essential for trustworthy deployment of safety‑critical AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21262v1)
