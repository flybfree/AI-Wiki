---
title: Exact Rank-Space KL Projection for Shared-Marginal Low-Rank Factors: Application to Doubly Stochastic Clustering
published: 2026-08-09T11:29:05Z
authors: Enliang Hu
url: http://arxiv.org/abs/2608.08642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exact Rank-Space KL Projection for Shared-Marginal Low-Rank Factors: Application to Doubly Stochastic Clustering

## Abstract
We study exact Kullback--Leibler (KL) projection for low-rank factorizations whose two nonnegative factors have prescribed row marginals and a shared, learned column marginal. For arbitrary positive row marginals of equal total mass, the joint KL projection reduces exactly to a strictly convex gauge-fixed dual with only $r-1$ effective variables; its Hessian is a sum of categorical covariance terms and admits $O((n+m)r)$ matrix-free Hessian--vector products. The projection theorem is objective-independent. We then specialize this geometry to doubly stochastic (DS) graph learning through $W=U\operatorname{Diag}(g)^{-1}V^\top$, where row-simplex factors with a common column mass induce an exactly DS graph without materializing an $n\times n$ optimization variable. Combined with observed-edge sparse fitting, a stochastic anchor-reduced manifold regularizer, and Bregman backtracking, the resulting mirror-descent method preserves exact feasibility at every accepted step. Under a nonvanishing latent-mass condition, it satisfies sufficient decrease and an $O(1/N)$ mirror-stationarity bound, while strictly positive accumulation points are KKT stationary. Matched clustering experiments show competitive accuracy, feasibility residuals near numerical precision, and favorable anytime behavior without a dense learned graph.

## Metadata
- **Published**: 2026-08-09T11:29:05Z
- **Authors**: Enliang Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08642v1)