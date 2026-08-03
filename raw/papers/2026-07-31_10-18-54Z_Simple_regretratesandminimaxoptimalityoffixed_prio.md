---
title: Simple-regret rates and minimax optimality of fixed-prior expected improvement in Matérn and squared-exponential RKHSs
published: 2026-07-31T10:18:54Z
authors: Emmanuel Vazquez, Sébastien Petit
url: http://arxiv.org/abs/2607.29245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simple-regret rates and minimax optimality of fixed-prior expected improvement in Matérn and squared-exponential RKHSs

## Abstract
We study the expected improvement (EI) policy for minimizing a deterministic objective function $f$ on a nonempty compact set $\mathcal X \subset\mathbb R^d$. We assume that $f$ belongs to the RKHS $\mathcal H_k$ of a continuous positive-semidefinite kernel $k$ on $\mathcal X$. Function values are observed exactly, and EI is computed from a fixed zero-mean Gaussian-process model with covariance $σ^2k$. After an initial design, the policy queries a point whose EI is at least a fixed positive fraction of its maximum.   We identify the normalized posterior standard deviation at a candidate point $x$ with the norm of the corresponding innovation in the canonical feature space, namely the component of $k(x,\cdot)$ orthogonal to the span of the preceding evaluation representers. Sequential separation radii bound the ranked innovation norms along arbitrary query sequences. We estimate these radii using Gram determinants and Kolmogorov widths for subspaces of different dimensions, then combine the estimates with a one-step regret inequality to obtain finite-budget bounds for simple regret.   After $N$ post-initial queries, simple regret is $O(N^{-ν/d})$ for isotropic Matérn kernels of smoothness $ν>0$. For the isotropic squared-exponential kernel, simple regret is $O(\exp[-c_1\min\{N, N^{1/d}\log(eN)\}])$ for some $c_1>0$. With exact EI maximization, it is $O(\exp[-c_2N^{1/d} \log(eN)])$ for some $c_2>0$. For every fixed $B\geq0$, these bounds are uniform over the RKHS ball of radius $B$.   If $\mathcal X$ has nonempty interior and $B>0$, then, among deterministic methods whose final recommendation may be any point of $\mathcal X$, the exact EI policy is minimax-rate optimal over the RKHS ball of radius $B$ for Matérn kernels and minimax-rate optimal up to constants in the exponent for squared-exponential kernels.

## Metadata
- **Published**: 2026-07-31T10:18:54Z
- **Authors**: Emmanuel Vazquez, Sébastien Petit
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29245v1)