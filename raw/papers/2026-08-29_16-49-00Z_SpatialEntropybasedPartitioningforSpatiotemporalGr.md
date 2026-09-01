---
title: Spatial Entropy based Partitioning for Spatiotemporal Graph Unlearning
published: 2026-08-29T16:49:00Z
authors: Qiming Guo, Wenbo Sun, Ye Wang, Wenlu Wang
url: http://arxiv.org/abs/2608.29360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spatial Entropy based Partitioning for Spatiotemporal Graph Unlearning

## Abstract
Spatiotemporal graphs underpin applications such as traffic forecasting, weather forecasting, and healthcare monitoring. Privacy regulations such as the GDPR and the CCPA require the complete removal of unauthorized data from trained models, but achieving this on a spatiotemporal graph is difficult: because information propagates globally through both spatial and temporal message passing, fully erasing a node's influence forces costly full-graph retraining. ST-graph unlearning requires both exactness and efficiency. We propose IsleNet, which uses spatial-entropy-guided partitioning to create balanced, locally coherent subgraphs and reconnects them with lightweight virtual edges. Upon an unlearning request, only the affected subgraph encoder and virtual-edge layer are retrained, ensuring exact removal with low cost. Experiments on four real-world benchmarks show that IsleNet attains up to 94% of full-graph accuracy while reducing unlearning time by up to an order of magnitude. Our code is publicly available at https://github.com/wenlu-lab/STGraphUnlearning.

## Metadata
- **Published**: 2026-08-29T16:49:00Z
- **Authors**: Qiming Guo, Wenbo Sun, Ye Wang, Wenlu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29360v1)