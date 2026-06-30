---
title: Highly Data Parallelizable Estimation of the Sliced-Wasserstein Distance Using Cumulative Distribution Functions
published: 2026-06-29T13:53:29Z
authors: Christophe Vauthier, Quentin Mérigot, Anna Korba
url: http://arxiv.org/abs/2606.30310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Highly Data Parallelizable Estimation of the Sliced-Wasserstein Distance Using Cumulative Distribution Functions

## Abstract
The Sliced Wasserstein (SW) distance has emerged as a computationally attractive alternative to the Wasserstein distance by leveraging one-dimensional optimal transport along random projections. Standard estimators of the SW distance rely on Monte Carlo averages of one-dimensional Wasserstein distances computed via quantile functions, which require sorting projected samples and access to full datasets. In this work, we introduce a new class of estimators for the Sliced Wasserstein distance based on cumulative distribution functions (CDFs) of projected measures, that avoid sorting and scale via massive dataset parallelism. This class includes several estimators, some of them being indexed by hyperparameters controlling their variance or smoothness. We show that they are especially well suited to scenarios in which CDFs are more tractable than quantile functions, such as mixtures of Gaussians, and moreover that they are also naturally compatible with federated learning, since CDFs of projected data can be computed and aggregated locally without requiring the exchange of raw samples.

## Metadata
- **Published**: 2026-06-29T13:53:29Z
- **Authors**: Christophe Vauthier, Quentin Mérigot, Anna Korba
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.30310v1)