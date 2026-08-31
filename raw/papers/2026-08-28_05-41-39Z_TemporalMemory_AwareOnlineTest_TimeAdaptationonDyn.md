---
title: Temporal Memory-Aware Online Test-Time Adaptation on Dynamic Graphs
published: 2026-08-28T05:41:39Z
authors: Bo Li, Xin Zheng, Ming Jin, Can Wang, Shirui Pan
url: http://arxiv.org/abs/2608.27948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Memory-Aware Online Test-Time Adaptation on Dynamic Graphs

## Abstract
Test-time adaptation (TTA) on graphs aims to adapt a graph neural network (GNN) that is well-trained on the training graph to the test graph, which involves potential distribution shifts that may harm model generalization and test-time inference. While recent efforts have investigated TTA on static graphs, there is still a research gap on dynamic graphs learned with dynamic GNN (DGNN) models, where both structural connectivity and node semantics evolve continuously over time. This makes adapting a DGNN model for reliable test-time performance substantially challenging. To fill this gap, in this work, we propose a novel framework of temporal memory-aware Online Test-Time Adaptation on Dynamic Graphs, named DGOTTA, to effectively adapt well-trained DGNNs during test time. Specifically, the proposed DGOTTA contains three modules: (1) temporal-aware augmentation, to extend the diversity of test dynamic graphs for addressing complex temporal and spatial shifts; (2) memory-aware model prediction, to alleviate catastrophic forgetting; (3) consistency-guided online adaptation, to enforce temporal alignment and memory smoothness. Extensive experiments on three real-world datasets and four DGNN backbones demonstrate that DGOTTA significantly improves generalization under diverse distribution shifts and multiple model architectures.

## Metadata
- **Published**: 2026-08-28T05:41:39Z
- **Authors**: Bo Li, Xin Zheng, Ming Jin, Can Wang, Shirui Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27948v1)