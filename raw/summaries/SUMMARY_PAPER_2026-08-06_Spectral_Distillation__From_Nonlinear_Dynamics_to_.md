---
title: Spectral Distillation: From Nonlinear Dynamics to Linear State-Space Models
url: http://arxiv.org/abs/2608.05416v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_21-20-32Z_SpectralDistillation_FromNonlinearDynamicstoLinear.md
generated_at: 2026-08-06 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a pipeline that learns an implicit spectral predictor from noisy observations of a nonlinear dynamical system using convex Observation Spectral Filtering, then converts this predictor into a compact linear state‑space model via spectral‑to‑LDS distillation. The authors prove that the resulting LDS representation achieves a prediction error that is exponentially small plus a term bounded by the complexity of the best observer, independent of any hidden latent dimension.

## Key Takeaways
- Observation Spectral Filtering provides a convex method for learning an optimal linear predictor that competes with the best possible observer.  
- The distillation step guarantees that the average prediction error decomposes into a small distillation term and a term controlled by Luenberger complexity, not latent state count.  
- Experiments show that the train‑then‑distill approach yields LDS predictors as compact or more accurate than models trained directly on nonlinear dynamics.

## Context
In reinforcement learning and behavior cloning, compressing complex dynamics into linear models is crucial for efficient simulation and transfer. This work bridges convex signal processing with state‑space modeling, offering a principled way to extract interpretable representations without solving high‑dimensional identification problems.

## Implications
The method enables practitioners to deploy compact LDS predictors in resource‑constrained environments where both accuracy and model size matter. By decoupling learning from latent dimensionality, it opens pathways for scalable simulation of nonlinear systems across AI research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05416v1)
