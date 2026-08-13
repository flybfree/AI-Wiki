---
title: Adaptive Bregman Proximal Stochastic Gradient with a Stabilized Barzilai--Borwein Step Size
url: http://arxiv.org/abs/2608.12009v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_12-46-05Z_AdaptiveBregmanProximalStochasticGradientwithaStab.md
generated_at: 2026-08-12 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Ada-BPSG, a line-search-free variant of Bregman proximal stochastic gradient that mitigates step-size sensitivity by using a stabilized Barzilai--Borwein candidate and a mediant aggregation scheme. It achieves O(n/K) convergence for convex objectives, restarted linear rates under relative quadratic growth, and an O(1/K) bound for nonconvex Bregman residuals.

## Key Takeaways
- Ada-BPSG replaces line searches with a stabilized BB candidate that aggregates secant information via mediants to reduce weight on nearly singular local ratios.  
- The method provides analytical convergence guarantees: O(n/K) rate for convex problems, restarted linear rates under relative quadratic growth, and an O(1/K) bound for nonconvex Bregman residuals.  
- Experiments show Ada-BPSG delivers low objective values with reduced sensitivity to initial step size compared to standard variance‑reduced baselines.

## Context
In AI optimization, variance reduction is essential when Euclidean smoothness assumptions fail, yet line searches are computationally expensive. Ada-BPSG’s analytical guarantees simplify implementation and enable scalable training of high‑dimensional models without costly line‑search overheads.

## Implications
For practitioners, the method reduces dependence on initial step size, leading to more robust convergence across diverse datasets. Industries can deploy Ada-BPSG in large‑scale recommendation or factorization pipelines without costly line‑search overheads.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12009v1)
