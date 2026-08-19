---
title: How smoothing the affinity matrix affects neighborhood preservation in t-SNE
published: 2026-08-17T23:05:51Z
authors: Shirin Mohebi, Guillaume Bied, Jefrey Lijffijt
url: http://arxiv.org/abs/2608.17190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How smoothing the affinity matrix affects neighborhood preservation in t-SNE

## Abstract
Dimensionality reduction methods are instrumental to visualize high-dimensional data, and t-SNE stands as one of the most widely used methods due to its emphasis on local neighborhood preservation. A central component of t-SNE is the affinity matrix, which expresses pairwise similarities in the form of symmetrized probabilities, over which the optimization problem of t-SNE is defined. We study how the sharpness of this probability distribution affects neighborhood preservation at different scales. We introduce a row-wise power transform controlled by a parameter gamma that can smooth or sharpen each row of the affinity matrix while preserving sparsity and rank order. We show that this transform is equivalent to rescaling the Gaussian bandwidth and thus to changing the perplexity. However, as the sharpness of the probability distribution varies per point, a fixed gamma leads to point-dependent effective perplexities, making it distinct from changing the global perplexity. Empirically, we find that sharpening improves preservation of the very nearest neighbors, while smoothing improves preservation of broader local neighborhoods, outperforming alternative affinity constructions including multiscale methods in the mid-local range.

## Metadata
- **Published**: 2026-08-17T23:05:51Z
- **Authors**: Shirin Mohebi, Guillaume Bied, Jefrey Lijffijt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17190v1)