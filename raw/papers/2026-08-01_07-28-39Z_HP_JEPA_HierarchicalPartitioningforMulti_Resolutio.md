---
title: HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning
published: 2026-08-01T07:28:39Z
authors: Ruichen Xu, Jingxiang Qu, Wenhan Gao, Jiaxing Zhang, Linsey Pang, Ravid Shwartz-Ziv, Yann LeCun, Yuefan Deng
url: http://arxiv.org/abs/2608.00491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HP-JEPA: Hierarchical Partitioning for Multi-Resolution Graph Joint-Embedding Predictive Learning

## Abstract
Graph self-supervised learning aims to learn transferable representations from large-scale unlabeled graph data. Joint-embedding predictive architectures (JEPAs) avoid explicit negative-pair construction and raw-input reconstruction by predicting masked targets directly in latent space. However, existing graph JEPAs typically rely on a single predefined graph partition, biasing the learned representations toward one structural granularity and limiting their ability to capture complementary patterns at different graph scales. To address this limitation, we propose HP-JEPA, a hierarchical partitioning framework for multi-resolution graph joint-embedding prediction. HP-JEPA organizes each graph into an ordered bank of coarse-to-fine partition resolutions and performs context-target latent prediction separately at each resolution using an online encoder, an exponential-moving-average target encoder, and a latent predictor. The resulting resolution-specific graph representations are subsequently integrated through concatenation or task-specific resolution weighting, allowing downstream models to combine complementary local, regional, and global structural information. Experiments on seven graph classification benchmarks and one graph regression benchmark show that HP-JEPA outperforms the fixed-resolution Graph-JEPA baseline on 6 of 8 tasks, improving upon Graph-JEPA on most evaluated benchmarks. Size-stratified analyses further show that HP-JEPA achieves higher accuracy than Graph-JEPA in most evaluated graph-size quartiles on three representative datasets. These results highlight the effectiveness of hierarchical multi-resolution partitioning for transferable graph representation learning.

## Metadata
- **Published**: 2026-08-01T07:28:39Z
- **Authors**: Ruichen Xu, Jingxiang Qu, Wenhan Gao, Jiaxing Zhang, Linsey Pang, Ravid Shwartz-Ziv, Yann LeCun, Yuefan Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00491v1)