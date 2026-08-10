---
title: When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series
published: 2026-08-07T15:28:45Z
authors: Chen Shao, Yue Wang, Zhenyi Zhu, Zhanbo Huang, Tobias Käfer, Zonghan Wu, Danai Koutra
url: http://arxiv.org/abs/2608.07333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series

## Abstract
Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static graph topology and aggregating information from neighboring series. In this work, we investigate the representa- tional power of GNNs for forecasting under both static and dynamic settings (i.e., when pairwise correlations evolve drastically over time) and identify critical limitations in current architectures. To formalize this, we first propose Temporal Correlation Volatility (TCV), a model- agnostic metric designed to quantify the distributional evolution of these latent structures. We establish a clear connection between TCV and performance degradation, demonstrating that many popular models, including Transformers, generalize poorly in high-TCV settings and are often outperformed by simple structure-agnostic baselines. To address these limitations, we propose Graph Layer for Inference in Dynamic En- vironments (GLIDE), a novel GNN layer enhanced by two theoretically grounded design mechanisms: (D1) Path-based Message Passing, which captures path-based neighborhoods and (D2) Static and Dynamic Propagation Separation, which identifies optimal dynamics via local static approximation. These components significantly improve learning under dynamic topology while preserving robustness in static scenarios. Ex- tensive experiments on synthetic and real-world benchmarks show that GLIDE improves average performance by up to 45.6% across static and dynamic settings, with the largest gain reaching 85.7%. The source code is available at https://github.com/ChenS676/GLIDE.

## Metadata
- **Published**: 2026-08-07T15:28:45Z
- **Authors**: Chen Shao, Yue Wang, Zhenyi Zhu, Zhanbo Huang, Tobias Käfer, Zonghan Wu, Danai Koutra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07333v1)