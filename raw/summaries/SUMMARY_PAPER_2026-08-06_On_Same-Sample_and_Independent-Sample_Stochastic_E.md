---
title: On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities
url: http://arxiv.org/abs/2608.06182v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-42-40Z_OnSame_SampleandIndependent_SampleStochasticExtrag.md
generated_at: 2026-08-06 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates stochastic extragradient (SEG) methods for monotone variational inequality problems, focusing on same-sample SEG (S-SEG). It demonstrates that S-SEG requires stricter samplewise Lipschitz conditions than independent-sample SEG and can diverge even with modified step-sizes. The authors also prove high-probability restricted-gap convergence under relaxed assumptions for both variants.

## Key Takeaways
- Same‑sample SEG is sensitive to the samplewise Lipschitz parameter; mean Lipschitzness alone does not guarantee convergence, even on a compact feasible set.
- High‑probability restricted‑gap convergence can be established for both I‑SEG and S‑SEG under relaxed assumptions, but certain improvements are impossible in general.
- An asymmetric double step‑size rule that ensures almost sure last‑iterate convergence for I‑SEG may fail for S‑SEG, leading to almost sure divergence.

## Context
Monotone variational inequality solvers are central to many AI applications such as constrained optimization and policy learning. Determining the robustness of stochastic algorithms under diverse data conditions is crucial for reliable algorithmic design.

## Implications
For practitioners developing online learning or reinforcement learning methods that rely on VIPs, this work clarifies when S‑SEG can be safely used and warns against applying I‑SEG guarantees to same‑sample settings. It also highlights fundamental limits of convergence results in stochastic optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06182v1)
