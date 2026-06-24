---
title: New Bounds for the Last Iterate of the Stochastic subGradient Method
url: http://arxiv.org/abs/2606.24879v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-23_17-55-18Z_NewBoundsfortheLastIterateoftheStochasticsubGradie.md
generated_at: 2026-06-24 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the performance of the last iterate produced by the stochastic subgradient method when applied to one‑dimensional convex Lipschitz objectives with a fixed step size η = Θ(1/√n). The authors show that under additive i.i.d. subgradient noise with uniformly bounded variance, the error at the final iteration is O(1/√n), eliminating the additional log n factor seen in generic bounds. Conversely, without assuming i.i.d., the error can degrade to (log n)/√n, indicating that the uniform‑variance assumption alone does not guarantee optimality even in one dimension.

## Key Takeaways
- The last iterate of SsGM achieves an optimization error of order 1/√n when using fixed stepsizes η = Θ(1/√n) and additive i.i.d. subgradient noise with bounded variance, removing the extra log n factor.
- Without the i.i.d. assumption, the same setup can produce an error scaling as (log n)/√n, showing that uniform‑variance alone is insufficient for optimality in dimension one.
- The result resolves negatively the open problem raised by Koren and Segal in COLT 2020, which questioned whether SsGM could achieve O(1/√n) error without additional assumptions.

## Context
The stochastic subgradient method remains a cornerstone of online learning for convex optimization, especially when exact gradients are unavailable. Understanding the behavior of its final iteration is crucial because many algorithms rely on this point to approximate the true optimum. This work sharpens the theoretical limits in one dimension, providing clearer insight into how noise assumptions affect convergence rates.

## Implications
For practitioners developing robust online solvers, the findings suggest that guaranteeing i.i.d. subgradient noise is essential for achieving optimal error bounds; otherwise, performance may be limited by log n factors. This influences algorithm design and verification in machine learning systems where low‑dimensional problems are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.24879v1)
