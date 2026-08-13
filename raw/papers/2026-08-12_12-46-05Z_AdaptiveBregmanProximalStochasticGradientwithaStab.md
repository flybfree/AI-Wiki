---
title: Adaptive Bregman Proximal Stochastic Gradient with a Stabilized Barzilai--Borwein Step Size
published: 2026-08-12T12:46:05Z
authors: Chenhan Jin, Shengze Xu, Binghui Xie, Kaiwen Zhou, Fan Jia, James Cheng, Tieyong Zeng
url: http://arxiv.org/abs/2608.12009v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Bregman Proximal Stochastic Gradient with a Stabilized Barzilai--Borwein Step Size

## Abstract
Bregman proximal stochastic gradient (BPSG) methods bring variance-reduced composite optimization to objectives whose geometry is poorly captured by Euclidean smoothness. Their performance, however, remains sensitive to the step size: raw stochastic curvature estimates can fluctuate sharply, whereas line searches add repeated proximal evaluations. We introduce Ada-BPSG, a line-search-free BPSG method that couples the SAGA gradient table with a stabilized Barzilai--Borwein (BB) candidate. A mediant aggregates incremental secant information so that nearly singular local ratios receive little weight, and an explicit safeguard translates the resulting curvature estimate into the bounded step-size sequence required for convergence. This design yields a direct analytical chain from relative smoothness and component-wise variance control to convergence in finite-dimensional normed spaces. We prove an $O(n/K)$ ergodic rate for convex objectives, a restarted linear rate under relative quadratic growth, and an $O(1/K)$ bound for a Bregman proximal residual in the nonconvex setting. On logistic regression and sparse nonnegative matrix factorization, Ada-BPSG combines low objective values with substantially less sensitivity to the initial step size than standard variance-reduced baselines, while avoiding line search.

## Metadata
- **Published**: 2026-08-12T12:46:05Z
- **Authors**: Chenhan Jin, Shengze Xu, Binghui Xie, Kaiwen Zhou, Fan Jia, James Cheng, Tieyong Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12009v1)