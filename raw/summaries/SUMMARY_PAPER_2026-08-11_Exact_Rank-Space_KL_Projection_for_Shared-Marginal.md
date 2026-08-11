---
title: Exact Rank-Space KL Projection for Shared-Marginal Low-Rank Factors: Application to Doubly Stochastic Clustering
url: http://arxiv.org/abs/2608.08642v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_11-29-05Z_ExactRank_SpaceKLProjectionforShared_MarginalLow_R.md
generated_at: 2026-08-11 13:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper develops an exact Kullback-Leibler projection for low‑rank factorizations where the row factors are nonnegative, share a learned column marginal, and have prescribed row marginals of equal total mass. It shows that this projection can be solved with a matrix‑free Hessian of size O((n+m)r), enabling an efficient mirror‑descent algorithm for doubly stochastic graph learning.

## Key Takeaways
- The exact KL projection reduces to a strictly convex gauge‑fixed dual with only r‑1 effective variables, making the problem tractable even for large graphs.  
- The Hessian is expressed as a sum of categorical covariance terms and supports O((n+m)r) matrix‑free Hessian–vector products, allowing fast gradient updates without forming dense matrices.  
- Under a nonvanishing latent‑mass condition the algorithm enjoys an O(1/N) mirror‑stationarity bound and strictly positive accumulation points that are KKT stationary, guaranteeing feasibility at each step.

## Context
This work addresses a longstanding challenge in graph learning: constructing doubly stochastic graphs from low‑rank factorizations without explicitly optimizing an n×n matrix. By leveraging exact projection geometry and Bregman backtracking, the method avoids dense variable materialization while preserving strong convergence guarantees typical of manifold‑regularized optimization.

## Implications
For practitioners, this approach offers a scalable framework for clustering tasks where doubly stochastic graphs are desired, delivering comparable accuracy with minimal computational overhead. The theoretical guarantees also provide confidence that the algorithm will converge to feasible solutions, encouraging adoption in real‑world AI pipelines requiring robust and efficient graph generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08642v1)
