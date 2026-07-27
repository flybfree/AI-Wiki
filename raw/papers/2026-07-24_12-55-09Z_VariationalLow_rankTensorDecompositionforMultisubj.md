---
title: Variational Low-rank Tensor Decomposition for Multisubject Spatiotemporal Data Analysis
published: 2026-07-24T12:55:09Z
authors: Laura M. Montaldo, Ricardo A. Borsoi, Sebastian Miron, Tulay Adali
url: http://arxiv.org/abs/2607.22262v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Variational Low-rank Tensor Decomposition for Multisubject Spatiotemporal Data Analysis

## Abstract
Modeling shared and subject-specific structure in multisubject spatiotemporal data remains challenging, particularly in neuroimaging, where both spatial and temporal patterns exhibit rich variability across subjects. Existing matrix and tensor decompositions provide interpretable factorizations, but rely on fixed multilinear structures or coupling schemes that may limit their flexibility in capturing complex variability. In this work, we introduce a spatiotemporal variational tensor decomposition (ST-VTD) framework that combines a tensor factorization generative model with structured priors to jointly represent spatial maps and temporal dynamics. Spatial factors are regularized to promote a low-rank structure inspired by the LL1 decomposition, while temporal factors are modeled using a learned Long short-term memory (LSTM)-based prior, enabling flexible and adaptive dynamics. Posterior inference is performed using an amortized variational formulation by unrolling iterations of an optimization algorithm, leading to an interpretable and parameter-efficient architecture. The proposed inference framework employs a warm-start strategy based on group independent component analysis, which we found to improve optimization performance. Experiments on a realistic synthetic functional MRI (fMRI) dataset demonstrate that the proposed approach significantly improves latent factor recovery compared with representative classical and probabilistic decomposition benchmarks.

## Metadata
- **Published**: 2026-07-24T12:55:09Z
- **Authors**: Laura M. Montaldo, Ricardo A. Borsoi, Sebastian Miron, Tulay Adali
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22262v1)