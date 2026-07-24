---
title: A Structure-Adaptive Random Feature Method for High-Dimensional Elliptic PDEs
published: 2026-07-22T06:10:49Z
authors: Jiale Linghu, Hao Dong, Yangshuai Wang
url: http://arxiv.org/abs/2607.19786v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Structure-Adaptive Random Feature Method for High-Dimensional Elliptic PDEs

## Abstract
Random-feature methods reduce high-dimensional elliptic PDE collocation to linear coefficient problems, but full-dimensional trial spaces overlook lower-dimensional structure. We introduce the Hierarchical Analysis-of-Variance Random Feature Method (HA-RFM), which selects coordinate blocks using closed Sobol indices of the PDE residual, identifies oblique low-rank features from fitted-predictor gradients, and couples all retained features in one regularized least-squares solve. Under structural and stability hypotheses, we establish an $L^2$ error bound that links solution and residual truncation to finite-width approximation and regularized finite-sample fitting, and we derive guarantees for width and structure recovery. The resulting width is polynomial in the dimension at fixed interaction order, with dimension-independent higher-order contributions under uniform structural control. Residual screening achieves exact recovery of the prescribed three-pair support, while fitted-predictor gradients recover oblique directions through dimension $50$. In random-ridge tests, less than $1\%$ additional width reduces errors by factors of $14$-$39$ over coordinate blocks and $34$-$100$ over equal-width full-dimensional RFM. Semilinear computations extend HA-RFM through dimension $100$, while dense and distributed interactions delineate the coordinate families required for broader structure.

## Metadata
- **Published**: 2026-07-22T06:10:49Z
- **Authors**: Jiale Linghu, Hao Dong, Yangshuai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19786v1)