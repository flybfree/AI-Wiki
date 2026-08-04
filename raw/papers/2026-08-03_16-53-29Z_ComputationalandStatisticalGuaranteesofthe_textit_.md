---
title: Computational and Statistical Guarantees of the \textit{c}-Rectified flow
published: 2026-08-03T16:53:29Z
authors: Leda Wang, Zhehao Xu, Qiang Liu, Harrison H. Zhou
url: http://arxiv.org/abs/2608.02487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Computational and Statistical Guarantees of the \textit{c}-Rectified flow

## Abstract
Recently, rectified flow has emerged as a fundamental framework for large-scale image generation, powering state-of-the-art systems such as FLUX.1 and Stable Diffusion 3. Despite its remarkable empirical success, the computational and statistical guarantees of iterative rectified flow have remained largely unexplored. We address this problem by studying \textit{c}-rectified flow, a cost-aware class of rectified flow that projects velocity fields onto a gradient class while preserving endpoint marginals. The ordinary rectified flow can fail to recover the optimal transport coupling: in a Gaussian case study, the iteration converges to the optimal coupling if and only if the source and target covariance matrices commute. In contrast, under suitable compactness and uniform-integrability assumptions, iterative \textit{c}-rectified flow always converges to the optimal transport coupling. We further establish quantitative one-step contraction and exponential convergence guarantees under projection-stability assumptions for both quadratic and strongly convex displacement costs. Finally, under a Hölder ball assumption, we develop new minimax-optimal score estimation rates and show that, when combined with iterative \textit{c}-rectified flow, they yield a rate-optimal estimator of the optimal transport for the dimension \(d \ge 3\) and a nearly parametric rate for \(d=1,2\).

## Metadata
- **Published**: 2026-08-03T16:53:29Z
- **Authors**: Leda Wang, Zhehao Xu, Qiang Liu, Harrison H. Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02487v1)