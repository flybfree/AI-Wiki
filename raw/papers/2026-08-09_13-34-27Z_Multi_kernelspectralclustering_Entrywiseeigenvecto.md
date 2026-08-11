---
title: Multi-kernel spectral clustering: Entrywise eigenvector perturbation bounds and exact recovery
published: 2026-08-09T13:34:27Z
authors: Zeqin Lin, Guangming Pan, Zhixiang Zhang, Yinbing Zhou
url: http://arxiv.org/abs/2608.08704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-kernel spectral clustering: Entrywise eigenvector perturbation bounds and exact recovery

## Abstract
Kernel spectral clustering with a single bandwidth can be inadequate for data exhibiting multiple characteristic pairwise-distance scales, a problem particularly prevalent in the high-dimensional regime. We address this issue through a multi-kernel formulation that aggregates kernels with different bandwidths. The bandwidths are selected as prescribed empirical quantiles of the pairwise squared distances, thereby capturing the relevant distance scales without requiring prior population-scale information.   We develop a rigorous theoretical analysis of the resulting method under a general high-dimensional, multi-scale mixture model with heterogeneous cluster centers and covariance geometries. We construct a blockwise constant, low-rank informative approximation to the empirical multi-kernel matrix and establish row-wise $\ell_{2,\infty}$ perturbation bounds for its leading spectral components, as well as for the associated normalized Laplacian matrix. These bounds yield observation-level control of the spectral embedding, which is more informative than conventional global eigenspace perturbation estimates. Under suitable eigen-gap and cluster-separation conditions, we show that approximate $K$-means applied to the multi-kernel spectral embedding achieves exact recovery with high probability.

## Metadata
- **Published**: 2026-08-09T13:34:27Z
- **Authors**: Zeqin Lin, Guangming Pan, Zhixiang Zhang, Yinbing Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08704v1)