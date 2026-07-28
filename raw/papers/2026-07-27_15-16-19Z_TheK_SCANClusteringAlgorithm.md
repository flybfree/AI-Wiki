---
title: The K-SCAN Clustering Algorithm
published: 2026-07-27T15:16:19Z
authors: Filip Kosiorowski, Grzegorz Sroka
url: http://arxiv.org/abs/2607.24537v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The K-SCAN Clustering Algorithm

## Abstract
In the Big Data era, the scalability of clustering algorithms constitutes a key challenge. Traditional density-based methods (e.g., DBSCAN) offer robustness to noise and the ability to detect non-linear clusters, yet their quadratic time complexity $O(N^2)$ drastically limits their applicability. Conversely, partitional algorithms (e.g., K-Means), with their linear complexity $O(N)$, impose sphericity on the resulting groups and fail in the presence of outliers. This paper presents K-SCAN -- a novel hybrid algorithm that optimizes this trade-off. The method integrates preliminary vector quantization (stochastic Mini-Batch K-Means) to extract a reduced set of weighted micro-clusters, followed by a subsequent density-based structural analysis. Empirical evaluation on datasets of up to $10^6$ samples confirms the linear computational complexity of the proposed solution. K-SCAN achieves more than a 3-fold speed-up over the hierarchical BIRCH algorithm, avoiding the costly management of tree-based structures. The method precisely identifies non-linear manifolds while maintaining structural stability (Adjusted Rand Index > 0.99), even with noise levels reaching 55\% of the data volume. The main limitation of the proposed algorithm, which could not be fully eliminated in the present study, remains its susceptibility to over-smoothing and its difficulty in separating clusters with highly heterogeneous local density. In complex visual spaces, this can lead to the loss of the finest topological details.

## Metadata
- **Published**: 2026-07-27T15:16:19Z
- **Authors**: Filip Kosiorowski, Grzegorz Sroka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24537v1)