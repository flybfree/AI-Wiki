---
title: Covariance Last-Layer Ensembles: Function-Space Diversity for Efficient Uncertainty Quantification
url: http://arxiv.org/abs/2607.23856v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_21-56-02Z_CovarianceLast_LayerEnsembles_Function_SpaceDivers.md
generated_at: 2026-07-27 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a Covariance Last-Layer Ensemble (cov‑LLE) that directly restores function‑space diversity in ensembles, addressing the limitation of standard Last‑Layer Ensembles where members converge on similar predictions. By penalizing covariance among member activations, cov‑LLE recovers much of the diversity and calibration lost to weight‑orthonormality while maintaining a single‑pass inference cost. The method improves prediction variance from 22.1 × 10⁻³ to 9.3 × 10⁻³ and ECE from 0.035 to 0.090, matching the performance of a deep ensemble at one‑time backbone cost.

## Key Takeaways
- cov‑LLE places a direct covariance penalty on member activations, unlike weight‑orthonormality which only decorrelates weights and not predictions, thereby preventing collapse in function space.
- The method recovers most of the diversity and calibration of a deep ensemble at 1× backbone cost, reducing prediction variance from 22.1 × 10⁻³ to 9.3 × 10⁻³ and ECE from 0.035 to 0.090.
- Adding a scale‑invariant direction score improves ROC AUC by +0.16 to +0.18, fixing near‑OOD failure without sacrificing accuracy.

## Context
Ensemble methods are widely used for uncertainty quantification in machine learning, but many suffer from high computational cost and loss of diversity due to shared gradients. Recent work on orthonormal certificates offers indirect solutions that fail to fully restore function‑space variation. cov‑LLE tackles this by focusing on the covariance of activations, offering a more efficient alternative.

## Implications
For practitioners, cov‑LLE provides a lightweight way to achieve calibrated uncertainty estimates without retraining large models, which is valuable in real‑time applications and limited‑resource settings. The improved AUC gains suggest that simple regularization can yield significant performance boosts, encouraging broader adoption of ensemble‑based OOD detection in industry pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23856v1)
