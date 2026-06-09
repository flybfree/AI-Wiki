---
title: Proximal Projection for Doubly Sparse Regularized Models
published: 2026-05-06T16:31:20Z
authors: Jia Wei He, R. Ayesha Ali, Gerarda Darlington
url: http://arxiv.org/abs/2605.05093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Proximal Projection for Doubly Sparse Regularized Models

## Abstract
Regularization is often used in high-dimensional regression settings to generate a sparse model, which can save tremendous computing resources and identify predictors that are most strongly associated with the response. When the predictors can be represented by a Gaussian graphical model, the structure of the predictor graph can be exploited during regularization. Our proposed model exploits this underlying predictor graph structure by decomposing the estimated coefficient vector into a sum of latent variables that correspond to the sum of each node contribution to the coefficient vector. Regularization is then performed on the latent variables rather than on the coefficient vector directly. We use a penalty function that permits a clear user-defined trade-off between the L1 and L2 penalties and propose a novel proximal projection during optimization. Further, our implementation computes the projection operator for the intersection of selected groups, which conserves more computing resources compared to predictor duplication methods, especially for high-dimensional data. Through simulation, we evaluate the performance of our approach under different graph structures and node counts, and present results on real-world data. Results suggest that our method exhibits stable performance relative to other singly or doubly sparse graphical regression models.

## Metadata
- **Published**: 2026-05-06T16:31:20Z
- **Authors**: Jia Wei He, R. Ayesha Ali, Gerarda Darlington
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.05093v1)