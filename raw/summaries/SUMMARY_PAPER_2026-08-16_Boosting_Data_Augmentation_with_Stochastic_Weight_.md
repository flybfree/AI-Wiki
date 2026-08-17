---
title: Boosting Data Augmentation with Stochastic Weight Averaging
url: http://arxiv.org/abs/2608.14373v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-15-23Z_BoostingDataAugmentationwithStochasticWeightAverag.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how stochastic weight averaging can be used to exploit symmetries in deep learning tasks without requiring repeated training runs. It finds that SWA applied to augmented data yields an equiviariance improvement beyond what SWA alone would provide, especially in the infinite-width limit. Experiments on computer vision and graph classification models confirm these theoretical gains.

## Key Takeaways
- In the infinite‑width limit, SWA on augmented data produces an equiviariance boost that exceeds the benefit of SWA itself.
- The analysis approximates the stochastic training trajectory with an Ornstein–Uhlenbeck process to derive this result.
- Numerical experiments across diverse models and symmetry types consistently support the theoretical findings.

## Context
Modern deep learning often struggles to capture task symmetries, leading to suboptimal performance despite simple augmentation tricks. This work bridges theory and practice by providing a closed‑form analysis of SWA’s symmetry benefits without costly ensembles.

## Implications
Practitioners can now apply SWA more effectively to improve model robustness across symmetric data distributions. The method reduces training overhead while delivering measurable gains, making it attractive for large‑scale deployment in computer vision and graph analytics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14373v1)
