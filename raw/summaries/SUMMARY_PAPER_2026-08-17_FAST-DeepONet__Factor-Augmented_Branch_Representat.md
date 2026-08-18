---
title: FAST-DeepONet: Factor-Augmented Branch Representations for High-Dimensional PDE Inputs in the Small-Sample Regime
url: http://arxiv.org/abs/2608.15408v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_20-31-51Z_FAST_DeepONet_Factor_AugmentedBranchRepresentation.md
generated_at: 2026-08-17 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FAST‑DeepONet, a branch representation that combines a fixed spectral path with a regularized projection of the orthogonal residual to stabilize deep operator networks for high‑dimensional PDE inputs. On Navier‑Stokes flow it reduces mean relative L2 error from 0.1556 to near 0.04 while keeping few trainable parameters, and improves performance across multiple test sets by up to 37% with fewer parameters.

## Key Takeaways
- FAST‑DeepONet lowers mean relative L2 error on Navier–Stokes from 0.1556 to near 0.04, showing that sensor grid refinement can be done without a statistical penalty.
- It achieves up to a 37% reduction in training loss across independent test sets for Darcy flow and terminal wavefield prediction while using three to seven times fewer trainable parameters than the original DeepONet.
- The improvement is attributed to a fixed spectral path handling correlated sensors and a residual path with directional penalty applied after normalizing each row of the effective residual map.

## Context
Deep operator networks struggle when faced with thousands of strongly correlated sensor measurements but only a limited number of training samples, leading to instability. This work addresses that instability by providing a branch representation that balances fixed spectral components with a regularized residual path, enabling reliable performance in high‑dimensional settings.

## Implications
For practitioners, FAST‑DeepONet offers a practical solution for deploying deep operators on real‑world sensor grids without sacrificing accuracy or computational cost. In industry, the method can accelerate model training and deployment across fluid dynamics simulations, making large‑scale PDE prediction more feasible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15408v1)
