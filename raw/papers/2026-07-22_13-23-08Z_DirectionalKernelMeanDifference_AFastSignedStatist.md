---
title: Directional Kernel Mean Difference: A Fast Signed Statistic for Univariate Distribution Comparison
published: 2026-07-22T13:23:08Z
authors: Shijie Zhong, Jiangfeng Fu
url: http://arxiv.org/abs/2607.20119v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Directional Kernel Mean Difference: A Fast Signed Statistic for Univariate Distribution Comparison

## Abstract
We introduce the Directional Kernel Mean Difference (DKMD), a signed statistic for univariate distribution comparison that preserves the direction of distributional shifts. Unlike the squared Maximum Mean Discrepancy (MMD), which discards directional information by squaring the RKHS distance, DKMD integrates the difference of kernel mean embeddings against a fixed odd weighting function. This construction yields three structural properties: antisymmetry, immunity to symmetric distributional differences, and directional monotonicity under stochastic dominance. We derive a data-driven Riemann estimator that ensures asymptotic consistency with the continuous formulation, strictly preserving the theoretical guarantees of the signed statistic in empirical evaluations. To overcome the quadratic computational cost of kernel methods, we develop an $O(N \log N)$ prefix--suffix scanning algorithm that exploits the total order of the real line while requiring only $O(N)$ memory. Experiments on synthetic benchmarks demonstrate that DKMD correctly isolates directional shifts from symmetric perturbations, remains robust to heavy-tailed outliers that can flip the sign of the mean difference, and scales to millions of samples in seconds.

## Metadata
- **Published**: 2026-07-22T13:23:08Z
- **Authors**: Shijie Zhong, Jiangfeng Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20119v1)