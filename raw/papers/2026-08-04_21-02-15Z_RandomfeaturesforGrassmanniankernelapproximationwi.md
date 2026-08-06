---
title: Random features for Grassmannian kernel approximation with bounded rank-one projections
published: 2026-08-04T21:02:15Z
authors: Rémi Delogne, Laurent Jacques
url: http://arxiv.org/abs/2608.04227v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Random features for Grassmannian kernel approximation with bounded rank-one projections

## Abstract
We propose a family of random feature maps for scalable kernel machines on low-dimensional subspaces, ie on the Grassmannian manifold. Such representations are useful when data classes or clusters are well described by the span of a few samples. Classical Grassmannian kernels, including the projection and Binet-Cauchy kernels, require full Gram matrices, which leads to prohibitive computational and memory costs for large high-dimensional subspace datasets. We address this limitation using random features based on rank-one projections of subspace projection matrices followed by bounded non-linear transforms, either periodic or binary, to control the resulting distributions.   We show that inner products in the random feature space approximate well-defined rotation-invariant Grassmannian kernels that depend only on the principal angles between subspaces. When the number of features is sufficiently large relative to the intrinsic subspace dimension, the approximation holds uniformly over all fixed-dimensional subspaces with high probability. For periodic transforms, the approximated kernel has a closed-form expression with tunable behaviour between inverse Binet-Cauchy and Gaussian-type regimes. Binary transforms yield compact one-bit subspace features, although no closed-form kernel is known. Structured rank-one projections based on randomised fast Fourier transforms further reduce computation without sacrificing practical accuracy. Experiments on synthetic data and ETH-80 classification tasks show that these features accurately preserve Grassmannian geometry while reducing computation, memory, and storage. Rank-one embeddings therefore provide a practical and scalable alternative to classical Grassmannian kernels.

## Metadata
- **Published**: 2026-08-04T21:02:15Z
- **Authors**: Rémi Delogne, Laurent Jacques
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04227v1)