---
title: Variance-Preserving Orthogonal Selection (VPOS): Greedy Feature Selection via Orthogonal Deflation in PCA Loading Space
published: 2026-07-25T13:26:48Z
authors: Baran Koseoglu, Berrin Yanikoglu
url: http://arxiv.org/abs/2607.23198v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Variance-Preserving Orthogonal Selection (VPOS): Greedy Feature Selection via Orthogonal Deflation in PCA Loading Space

## Abstract
We propose Variance-Preserving Orthogonal Selection (VPOS), a greedy framework for unsupervised feature selection that operates in the weighted PCA loading space. After each selection, VPOS projects out the chosen feature's variance direction via null-space deflation, forcing subsequent selections to cover orthogonal parts of the covariance structure. Each step provably reduces the loading matrix rank by one, and the greedy objective connects to monotone submodular maximization. The single hyperparameter $d$ is selected via a reproducible rule: the value minimising reconstruction MSE in a sensitivity sweep. On eight benchmarks, VPOS achieves the lowest reconstruction MSE on all eight while running 10-140x faster than graph-based methods at scale. Comparing against PCA (no deflation) at matched $d$ confirms deflation as the primary driver, reducing MSE by 10-73%.

## Metadata
- **Published**: 2026-07-25T13:26:48Z
- **Authors**: Baran Koseoglu, Berrin Yanikoglu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23198v1)