---
title: Lantern: Conflict-Aware Gradient Blending for Physics-Guided Diffusion Models in Calorimeter Simulation
url: http://arxiv.org/abs/2607.25060v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_20-42-39Z_Lantern_Conflict_AwareGradientBlendingforPhysics_G.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Lantern, a physics‑aware diffusion model that improves the fidelity of calorimeter shower simulations beyond pure statistical denoising. By adding two auxiliary losses and using GradBlend to align their gradients with the denoising objective, Lantern achieves significant gains in both FPD and Correlation Frobenius Distance compared to baseline methods.

## Key Takeaways
- The Correlation Frobenius Distance (CFD) quantifies correlation fidelity at layer‑wise and voxel‑wise scales, providing a single normalized score for physics fidelity.  
- A variance‑stabilized voxel residual loss grounded in counting statistics conflicts with denoising gradients, requiring a temporary denoising‑only phase to preserve shower fidelity.  
- The graph Laplacian loss over detector geometry is non‑conflicting and can be integrated smoothly without schedule adjustments.

## Context
Physics‑guided generative models aim to respect underlying physical laws while maintaining computational efficiency, a challenge highlighted by the need for accurate calorimeter surrogate training in high‑energy physics experiments. This work advances that goal by embedding per‑sample structure into diffusion learning through task‑symmetric loss scheduling.

## Implications
Lantern’s approach reduces reliance on expensive Monte Carlo simulations, enabling faster model updates and higher fidelity predictions for accelerator control systems. Practitioners can leverage the non‑conflicting Laplacian loss to improve calibration without sacrificing denoising quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25060v1)
