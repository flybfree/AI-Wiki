---
title: Second-Moment Memory in Coordinatewise Adam
url: http://arxiv.org/abs/2608.15824v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_15-56-36Z_Second_MomentMemoryinCoordinatewiseAdam.md
generated_at: 2026-08-17 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the second‑moment memory retained by Adam’s denominator affects optimization speed. It demonstrates that keeping a long history of squared gradients can reduce expected update magnitude to O(M₂⁻¹ᐟ²), where M₂ is the effective memory length, leading to slower convergence even with finite‑variance noise.

## Key Takeaways
- The second‑moment memory in Adam’s denominator can suppress progress toward the optimum under stochastic gradient updates.  
- For a two‑point oracle, the expected positive normalized update decays as O(M₂⁻¹ᐟ²) after an initialization transient.  
- This directional bound translates into an average‑stationarity lower bound of the same order on smooth convex problems with normalized gap and variance.

## Context
Adam’s adaptive learning rate relies on maintaining a moving average of squared gradients, which is computationally cheap but may incur hidden costs in convergence speed. Recent work has shown that this memory can act as a bottleneck, especially when the history length grows large relative to stepsize scaling.

## Implications
For practitioners tuning Adam hyperparameters, excessively long second‑moment memory could be unintentionally slowing training. The insight suggests exploring shorter memory horizons or alternative optimizers that avoid such hidden slowdowns in real‑world deep learning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15824v1)
