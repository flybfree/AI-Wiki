---
title: How Much Regularization Survives Averaging? Update Masking in Federated Learning
url: http://arxiv.org/abs/2608.23286v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_14-13-18Z_HowMuchRegularizationSurvivesAveraging_UpdateMaski.md
generated_at: 2026-08-24 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how regularization introduced by masking survives federated averaging when clients apply different masks. It proves that client-specific masks reduce the effective regularization by a factor equal to the cohort size, while using identical masks restores it with a factor of inverse gradient diversity. Experiments on CIFAR‑10 show the regularization is weakened from 10 to around 1.2 when masks differ, and only improves modestly when sampling or heterogeneity changes.

## Key Takeaways
- Client-specific masking reduces the regularization strength by exactly the cohort size, meaning each additional client dilutes the effect of mask‑induced sharpness penalties.
- Using a shared mask restores regularization with a factor equal to the inverse gradient diversity across the cohort, which can be as high as 1.19 on CIFAR‑10.
- Turning off minibatch sampling or increasing data heterogeneity raises the effective regularization back toward its original value, indicating that these factors mitigate the loss of mask‑driven regularization.

## Context
Federated learning aims to achieve flat minima across non-IID clients, and existing methods rely on sharpness‑aware minimization which requires centralized gradient information. This work highlights a theoretical gap: local masking provides free regularization but is lost when averaging with heterogeneous masks, affecting generalization performance.

## Implications
Practitioners must consider mask uniformity or alternative regularization strategies to preserve the benefits of noise‑based training in federated settings. The findings suggest that standard federated averaging may underestimate regularization strength, leading to suboptimal convergence and higher error rates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23286v1)
