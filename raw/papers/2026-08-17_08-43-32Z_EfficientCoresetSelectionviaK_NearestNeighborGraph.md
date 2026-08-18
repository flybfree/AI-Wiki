---
title: Efficient Coreset Selection via K-Nearest Neighbor Graphs
published: 2026-08-17T08:43:32Z
authors: Yingfan Liu, Leiyu Zhang, Jiadong Xie, Mingzhe Wang, Jeffrey Xu Yu, Jiangtao Cui
url: http://arxiv.org/abs/2608.16270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Coreset Selection via K-Nearest Neighbor Graphs

## Abstract
Coreset selection reduces the cost of model training by replacing a large training set with a small representative subset. Existing gradient-approximation coreset methods such as CRAIG and cluster-based variants can preserve model accuracy. Still, their selection stages often rely on dense pairwise distances or large item-cluster bound matrices, leading to high time and memory costs on large datasets. This paper proposes KNNG-CS, a lightweight coreset selection method based on a $K$-nearest neighbor graph. KNNG-CS exploits local neighborhood structures to estimate the importance of each data item and greedily selects representative nodes without maintaining a quadratic distance matrix. The method requires only linear storage in the number of edges. Experiments on four real-world datasets show that KNNG-CS achieves accuracy comparable to representative gradient-approximation coreset methods, while reducing selection time by $2.3\times$-$41.2\times$ and peak memory to $0.3\%$-$7.5\%$ of the baselines.

## Metadata
- **Published**: 2026-08-17T08:43:32Z
- **Authors**: Yingfan Liu, Leiyu Zhang, Jiadong Xie, Mingzhe Wang, Jeffrey Xu Yu, Jiangtao Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16270v1)