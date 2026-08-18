---
title: RagGAD: Rationale-Aware Conditional Gaussian Mixture Normalizing Flow for Unsupervised Graph Anomaly Detection
published: 2026-08-17T02:20:25Z
authors: Junxin Lu, Jing Zhao, Shiliang Sun
url: http://arxiv.org/abs/2608.16018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RagGAD: Rationale-Aware Conditional Gaussian Mixture Normalizing Flow for Unsupervised Graph Anomaly Detection

## Abstract
Graph anomaly detection aims to identify nodes that deviate from normal behavioral patterns within graphs. However, existing methods largely rely on the homophily assumption, which makes it difficult to distinguish spurious affinities and to capture the diverse behaviors of normal nodes,limiting their robustness in complex real-world scenarios. To address this problem, we propose RagGAD, an unsupervised graph anomaly detection framework based on rationale-aware conditional Gaussian mixture normalizing flow. RagGAD introduces an adaptive rationale disentangler to disentangle stable rationales from spurious correlations within node interrelationships, and further decomposes stable rationales into robust and fragile components. The learned rationales capture underlying interaction patterns that characterize normal behaviors under varying conditions, while anomalies emerge as deviations associated with unstable or spurious correlations. To model the intricate distributions of normal and abnormal nodes, RagGAD integrates rationale-non-rationale Gaussian mixture modeling with a robust-fragile rationale mixture learning strategy. By mitigating spurious homophilic correlations and embracing the heterogeneity of normal patterns, RagGAD identifies anomalies as low-density regions within a structure-aware distribution space. Extensive experiments on multiple benchmark datasets demonstrate that RagGAD outperforms state-of-the-art methods.

## Metadata
- **Published**: 2026-08-17T02:20:25Z
- **Authors**: Junxin Lu, Jing Zhao, Shiliang Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16018v1)