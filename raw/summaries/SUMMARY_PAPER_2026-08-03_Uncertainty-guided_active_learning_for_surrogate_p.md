---
title: Uncertainty-guided active learning for surrogate prediction of stream-finishing wear fields
url: http://arxiv.org/abs/2608.00593v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_11-12-39Z_Uncertainty_guidedactivelearningforsurrogatepredic.md
generated_at: 2026-08-03 23:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an uncertainty‑guided active learning framework that builds a deep surrogate model to predict three erosion fields from geometry alone. The surrogate is trained on only 13 % of the 696 feasible orientations and reproduces DEM results with high Spearman correlations, while its epistemic uncertainty estimates guide which orientations are simulated next.

## Key Takeaways
- The surrogate predicts per‑triangle normal impact velocity, tangential impact velocity, and particle impact flux directly from geometry using a deep ensemble that quantifies disagreement as epistemic uncertainty.  
- Active learning selects the most uncertain orientations for DEM simulation, reducing computational cost while maintaining high prediction fidelity.  
- Calibration shows predicted uncertainties align with actual errors, achieving Spearman correlations up to 0.97 on low‑uncertainty cases and degrading smoothly as uncertainty rises.

## Context
In additive manufacturing and machining, accurate wear modeling is essential for optimizing process parameters and minimizing material loss. Traditional methods rely on exhaustive DEM simulations that are infeasible for new geometries, limiting rapid iteration cycles. This work demonstrates how AI‑driven uncertainty quantification can replace costly simulations with lightweight surrogate models.

## Implications
Manufacturers can now predict wear fields quickly, enabling real‑time process adjustments and reducing scrap rates. The approach lowers simulation expenses and accelerates design iterations, supporting sustainable production in industries where surface finish is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00593v1)
