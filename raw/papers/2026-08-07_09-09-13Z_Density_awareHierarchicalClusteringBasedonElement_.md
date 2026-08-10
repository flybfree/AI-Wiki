---
title: Density-aware Hierarchical Clustering Based on Element-Categorized Connection Subgraphs
published: 2026-08-07T09:09:13Z
authors: Yuning Yu, José Rodríguez-Piñeiro, Xuefeng Yin, Bin Feng
url: http://arxiv.org/abs/2608.06990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Density-aware Hierarchical Clustering Based on Element-Categorized Connection Subgraphs

## Abstract
Clustering is a fundamental data mining technique for pattern recognition through unsupervised learning. Among various clustering methods, hierarchical clustering, density-based clustering, and graph clustering stand out as representative approaches. For hierarchical clustering, it can be categorized into agglomerative and divisive modes to construct clusters in a recursive manner. The key aspect of both modes is the calculation of inter-cluster similarity, which determines whether to merge the sub-clusters into one cluster or divide a current cluster into sub-clusters. Traditionally, the similarity is derived from pairwise distances, often overlooking density variations and structural connectivity in graphs. To address this, we propose a density-aware hierarchical clustering method based on element-categorized connection subgraphs (DHC-ECS), which effectively integrates the hierarchical clustering, density-based clustering, and graph clustering. Particularly, a novel inter-cluster similarity metric is introduced that considers not only distances but also the element categorization in the KNN connection subgraphs, kernel density estimation, and local connectivity within sub-clusters. Extensive evaluations on heterogeneous benchmark datasets demonstrate that DHC-ECS exhibits superior overall performance in terms of clustering accuracy and parameter robustness compared with the baseline methods (including AChameleon, RNN-DBSCAN, McDPC, and G-RMS). The work indicates the great potential of the proposed clustering algorithm for low-dimensional datasets by leveraging local density and graph-structured connectivity (i.e., the duality of vertices and edges), as well as the possibility to determine an intrinsic threshold, reducing the reliance on manual parameter tuning.

## Metadata
- **Published**: 2026-08-07T09:09:13Z
- **Authors**: Yuning Yu, José Rodríguez-Piñeiro, Xuefeng Yin, Bin Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06990v1)