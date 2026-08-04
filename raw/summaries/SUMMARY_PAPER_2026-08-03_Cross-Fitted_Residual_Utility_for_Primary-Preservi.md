---
title: Cross-Fitted Residual Utility for Primary-Preserving Cognitive Decision Correction in Automatic Modulation Classification
url: http://arxiv.org/abs/2608.02063v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-07-37Z_Cross_FittedResidualUtilityforPrimary_PreservingCo.md
generated_at: 2026-08-03 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a cross-fitted residual utility framework that combines default predictions with cognitive decision correction for automatic modulation classification. By learning candidate-specific residuals from out-of-fold predictions and applying a primary-preserving policy, the system boosts overall accuracy across three benchmark datasets.

## Key Takeaways
- The method learns residual utilities from train-split out-of-fold predictions, enabling each candidate to quantify how much its evidence deviates from the default probability.
- A disjoint validation split freezes action thresholds and approved transitions, ensuring a consistent risk mask during held-out evaluation.
- Controlled comparisons reveal that gains arise from the integrated evidence-and-action policy rather than isolated utility maximization.

## Context
Automatic modulation classification focuses on representation accuracy but neglects when to override default predictions. This work addresses the post-inference cognitive decision problem by integrating residual utilities into a unified risk mask, reflecting real-world scenarios where heterogeneous evidence may justify correction.

## Implications
The approach offers a principled way to improve classifier robustness in noisy wireless environments and can be adapted for other binary classification tasks requiring confidence calibration. Practitioners can leverage this framework to design adaptive decision policies that preserve primary predictions while exploiting secondary evidence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02063v1)
