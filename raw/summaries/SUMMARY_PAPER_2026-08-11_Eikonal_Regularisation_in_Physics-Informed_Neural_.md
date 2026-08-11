---
title: Eikonal Regularisation in Physics-Informed Neural Networks for Three-Dimensional Level-Set Advection: Transferability of Two-Dimensional Design Principles
url: http://arxiv.org/abs/2608.08322v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_20-20-13Z_EikonalRegularisationinPhysics_InformedNeuralNetwo.md
generated_at: 2026-08-11 13:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the eikonal regularisation weight that dominates hyperparameter selection in two‑dimensional level‑set advection transfers to three dimensions and remains stable across runs. By testing four benchmark flows with multiple seeds, it shows that the optimal weight varies by up to five orders of magnitude depending on how far the exact solution deviates from the signed‑distance property. Multi‑seed experiments reveal that small weights increase seed‑to‑seed variance, while larger weights improve reproducibility and accuracy.

## Key Takeaways
- The eikonal weight shifts dramatically between rigid‑body and deforming flows, ranging from 10⁻¹ to 10⁻⁵, indicating sensitivity to the extent of interface distortion.  
- Only two out of four three‑dimensional benchmarks inherit the same weight pattern as their two‑dimensional counterparts, so direct transfer is not guaranteed without verification.  
- At low weights, seed variability equals the model error; the regulariser reduces this variance by more than an order of magnitude, enhancing both reproducibility and performance.

## Context
Physics‑informed neural networks rely on residual and initial‑condition losses complemented by geometric penalties to enforce physical constraints. The eikonal regulariser is a standard tool for preserving signed‑distance fields in level‑set problems. This study extends that framework to three dimensions, addressing the gap between two‑dimensional design principles and higher‑dimensional applicability.

## Implications
For practitioners developing AI models of fluid interfaces, the findings suggest careful hyperparameter calibration per problem geometry rather than relying on a universal setting. The improved reproducibility at larger weights offers practical benefits for training stability in industrial simulations where consistent results are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08322v1)
