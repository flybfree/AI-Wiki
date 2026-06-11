---
title: A Riemannian Approach to Low-Rank Optimal Transport
published: 2026-06-10T14:17:08Z
authors: Pratik Jawanpuria, Bamdev Mishra
url: http://arxiv.org/abs/2606.12120v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Riemannian Approach to Low-Rank Optimal Transport

## Abstract
Low-rank optimal transport (OT) mitigates the quadratic scaling of classical solvers, yet existing approaches rely heavily on first-order mirror-descent updates that require careful hyperparameter tuning and ignore the optimization landscape's curvature. To address these limitations, we propose a unified Riemannian geometric framework for low-rank OT, modeling balanced and unbalanced rank-$r$ positive factored couplings as novel smooth embedded submanifolds of the positive orthant. By equipping these manifolds with the Fisher-Rao product metric, we derive tractable formulations for Riemannian projectors, retractions, and Hessian-vector products. Our cost-agnostic framework seamlessly extends to linear OT, Gromov-Wasserstein (GW), fused GW, and their unbalanced counterparts. For balanced OT, our geometric ingredients are computed via efficient conjugate-gradient and iterative Bregman updates. For the unbalanced OT, our operations elegantly reduce to closed-form scalings, completely eliminating inner iterative loops. In both regimes, per-iteration complexity scales linearly with dataset size, and we provide a rank-sufficiency certificate for global optimality verification. Extensive experiments across a range of problem sizes demonstrate that our regularization-free first- and second-order solvers achieve faster convergence and superior performance over existing state-of-the-art low-rank OT solvers.

## Metadata
- **Published**: 2026-06-10T14:17:08Z
- **Authors**: Pratik Jawanpuria, Bamdev Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12120v1)