---
title: Beyond Effective Sample Size: Effective Number of Proposals for Adaptive Importance Sampling
url: http://arxiv.org/abs/2608.15154v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_10-12-05Z_BeyondEffectiveSampleSize_EffectiveNumberofProposa.md
generated_at: 2026-08-17 21:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the effective number of proposals (ENP) as a diagnostic for population‑based adaptive importance sampling that complements existing effective sample size (ESS) measures. ENP estimates how many distinct proposal components actually contribute to approximating the target distribution, detecting cases where standard ESS would mislead.

## Key Takeaways
- ENP combines normalized weight per proposal with a redundancy measure from target‑weighted samples to count non‑redundant empirical contributions.
- A high ESS can coexist with low ENP when many proposals generate samples in the same region, indicating poor arrangement of proposals.
- The metric serves as a feedback signal that can trigger rejuvenation of redundant proposals.

## Context
Population‑based adaptive importance sampling is widely used to approximate complex target distributions in Bayesian inference and machine learning. Existing diagnostics focus on ESS, which only reflects weight concentration but ignores how proposal components are distributed across the sampling space.

## Implications
Practitioners can reduce wasted sampling effort by identifying redundant proposals early, leading to faster convergence and lower computational cost in high‑dimensional applications. This improves efficiency of AIS pipelines without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15154v1)
