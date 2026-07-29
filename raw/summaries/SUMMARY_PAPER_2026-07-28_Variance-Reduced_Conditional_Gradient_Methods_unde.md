---
title: Variance-Reduced Conditional Gradient Methods under Markovian Sampling for Nonconvex Composite Optimization
url: http://arxiv.org/abs/2607.25785v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_14-37-47Z_Variance_ReducedConditionalGradientMethodsunderMar.md
generated_at: 2026-07-28 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates variance‑reduced conditional gradient methods when stochastic composite nonconvex objectives are optimized over a compact convex set with gradients arriving along a single trajectory of an ergodic Markov chain. By introducing MC‑ALFCG, which merges momentum CG with capped multilevel Monte Carlo and per‑iteration clipping, the authors achieve tight error bounds that account for projection‑free constraints and pathwise dynamics.

## Key Takeaways
- The method’s conditional bias is bounded by O(τ_mix/T) uniformly over all starting states, where τ_mix is the mixing time of the chain and T the number of iterations.  
- Coupling between gradient estimates controls the second moment of gradient differences through iterate displacement, enabling variance reduction without explicit projection steps.  
- Clipping enforces pathwise bounds required for adaptive analysis, and the recursion reduces to independent sampling under σ²→2ΛGσ² and L²→2ΛL² with Λ=O(τ_mix log T).

## Context
This work extends classical single‑trajectory variance reduction results to composite nonconvex problems where gradient updates are not projected onto a feasible set, a common scenario in deep learning training. The approach leverages Markovian dynamics to design algorithms that adaptively balance bias and variance across iterations.

## Implications
For practitioners, MC‑ALFCG offers a practical way to train complex models with limited projection operations while maintaining provable sample complexity. In industry, the method can reduce computational cost and improve convergence speed for large‑scale optimization tasks where exact projections are costly or unavailable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25785v1)
