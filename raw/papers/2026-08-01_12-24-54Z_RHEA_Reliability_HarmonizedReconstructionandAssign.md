---
title: RHEA: Reliability-Harmonized Reconstruction and Assignment for Robust Multimodal-Attributed Graph Clustering
published: 2026-08-01T12:24:54Z
authors: Yinlin Zhu, Di Wu, Ziyu Han, Zekai Chenm, Wang Luo, Miao Hu, Guocong Quan
url: http://arxiv.org/abs/2608.00621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RHEA: Reliability-Harmonized Reconstruction and Assignment for Robust Multimodal-Attributed Graph Clustering

## Abstract
Multimodal-attributed graphs (MAGs), whose nodes carry heterogeneous attributes such as text and images over a relational structure, have become a fundamental substrate for label-free entity grouping tasks, including community discovery and product segmentation. Existing MAG clustering methods effectively integrate complementary modalities when attributes are clean and complete, but degrade substantially under noisy or missing attributes because they implicitly assume equal modality reliability across all nodes. In practice, modality reliability is inherently node-specific: images may be corrupted or absent, while textual descriptions are incomplete or noisy. We argue that, under attribute homophily, graph neighborhoods naturally provide supervision-free evidence for estimating node-specific modality reliability. Based on this insight, we propose RHEA, a reliability-aware framework for MAG clustering that estimates node-specific modality reliability from neighborhood consensus and propagates this signal throughout the clustering pipeline. RHEA reconstructs unreliable or missing modalities from graph neighborhoods, adaptively weights modalities during reliability-aware fusion, and performs topology-aware optimal transport clustering with reliability-aware transport assignment and neighbor-consensus assignment distillation. Furthermore, the confidence of reconstructed representations is incorporated into the clustering objective, allowing uncertain reconstructions to contribute proportionally during optimization. Experiments on four MAG benchmarks under five attribute conditions show that RHEA consistently outperforms the strongest baseline, with NMI gains increasing as attribute quality deteriorates.

## Metadata
- **Published**: 2026-08-01T12:24:54Z
- **Authors**: Yinlin Zhu, Di Wu, Ziyu Han, Zekai Chenm, Wang Luo, Miao Hu, Guocong Quan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00621v1)