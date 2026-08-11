---
title: Adaptive KappaSharp: Condition-Number Shaping for Preferential Bayesian Optimization
url: http://arxiv.org/abs/2608.07859v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_01-56-13Z_AdaptiveKappaSharp_Condition_NumberShapingforPrefe.md
generated_at: 2026-08-11 13:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KappaSharp, a method that adapts the Hessian of the Gaussian process surrogate used in preferential Bayesian optimization to improve its condition number. By applying diagonal corrections where prior uncertainty is high, it reduces numerical instability without affecting query selection. On 11 benchmarks including a 16‑dimensional controller tuning problem, Adaptive KappaSharp improves performance by up to 10.9% (p=0.003) compared with the standard PBO baseline.

## Key Takeaways
- The method applies a diagonal correction to the likelihood Hessian only during model fitting, not during query selection, which avoids wasteful re‑querying of candidates that would disconnect the comparison graph.
- Correction magnitudes are larger where prior uncertainty is higher, thereby focusing effort on directions with greatest ambiguity and improving conditioning.
- An adaptive version activates corrections only when the surrogate is confident about recent comparisons, preventing unnecessary adjustments in well‑conditioned problems.

## Context
Preferential Bayesian optimization relies on pairwise user comparisons that create a graph of evaluated candidates. When each new query forms an isolated pair, the resulting likelihood matrix loses one degree of freedom, leading to rank deficiency and poor conditioning. Existing solutions either limit connectivity or add uniform regularization, both of which compromise efficiency.

## Implications
Practitioners can achieve more reliable optimization results with fewer queries by stabilizing surrogate models without sacrificing the graph‑based structure of PBO. The approach is especially valuable for high‑dimensional problems where condition number issues dominate performance, offering a practical upgrade to standard Bayesian optimization pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07859v1)
