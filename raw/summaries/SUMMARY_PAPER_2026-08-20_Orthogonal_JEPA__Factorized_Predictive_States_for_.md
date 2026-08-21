---
title: Orthogonal JEPA: Factorized Predictive States for Latent World Models
url: http://arxiv.org/abs/2608.20065v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_13-59-57Z_OrthogonalJEPA_FactorizedPredictiveStatesforLatent.md
generated_at: 2026-08-20 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Orthogonal JEPA, a factorized predictive state framework that learns latent world models by decomposing target embeddings into orthogonal components and predicting each component from shared context. Experiments across diverse domains show improved representation quality, forecasting accuracy, planning performance, and long‑horizon stability compared to monolithic JEPAs.

## Key Takeaways
- Learned basis matrices decompose each target state into multiple orthogonal components, allowing the model to allocate capacity efficiently across different predictive signals.
- A dedicated prediction branch estimates each component from a shared context representation while preserving factor magnitudes for accurate state synthesis.
- Orthogonality and regularization objectives prevent redundancy, coordinate collapse, and maintain variation in projected targets.

## Context
In AI, world models are essential for tasks requiring prediction, planning, and reasoning about hidden dynamics. Traditional JEPAs treat the entire latent state as a single target embedding, which can lead to imbalanced learning and instability.

## Implications
Orthogonal JEPA offers a scalable architecture that can be applied to any partial or future observation, reducing redundancy and improving robustness in complex systems such as vision, genomics, and continuous control.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20065v1)
