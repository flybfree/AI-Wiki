---
title: Second-Moment Memory in Coordinatewise Adam
url: http://arxiv.org/abs/2608.15824v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-16_15-56-36Z_Second_MomentMemoryinCoordinatewiseAdam.md
generated_at: 2026-08-18 20:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how Adam’s second-moment memory—its moving average of squared gradients—affects optimization speed, showing that this memory can cause a slowdown even with finite-variance noise. It derives an O(M_2^{-1/2}) bound on the expected positive normalized update after initialization, where M_2 is the effective memory length.

## Key Takeaways
- The second-moment memory in Adam leads to an expected positive normalized update of order M_2^{-1/2}, indicating that longer memory slows progress. - This directional bound translates into a lower bound on average stationarity for smooth convex problems with normalized gap, smoothness, and variance. - Long memory can suppress optimization despite finite-variance stochastic gradients.

## Context
Adam’s denominator includes a moving average of squared gradients to stabilize updates, but its cost is rarely quantified in practice. This work reveals that the memory itself introduces inefficiency, challenging assumptions about Adam’s near-linear convergence guarantees under standard noise models.

## Implications
For practitioners using Adam, longer second-moment memory may degrade performance without clear benefit, suggesting alternative optimizers or memory truncation strategies might be preferable. The findings highlight a nuance in stochastic optimization where algorithmic design can unintentionally hinder progress.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15824v1)
