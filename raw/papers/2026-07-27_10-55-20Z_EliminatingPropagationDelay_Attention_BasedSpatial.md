---
title: Eliminating Propagation Delay: Attention-Based Spatial-Temporal Fusion Graph Convolution Network for Traffic Flow Prediction
published: 2026-07-27T10:55:20Z
authors: Jinpeng Chen, Ziyu Yu, Tao Wang, Jun Ma, Hongbo Gao, Senzhang Wang, Zufeng Zhang, Kaimin Wei
url: http://arxiv.org/abs/2607.24885v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Eliminating Propagation Delay: Attention-Based Spatial-Temporal Fusion Graph Convolution Network for Traffic Flow Prediction

## Abstract
Predicting traffic flow is crucial to optimizing transportation systems and improving urban mobility. Many graph convolution-based models have been proposed to extract spatial-temporal features and predict traffic flow. However, most focus on spatial-temporal and semantic correlation in topological relationships. There are two primary problems to address. Firstly, the convolutional structure in the model focuses on utilizing static spatial dependencies and spatial-temporal relationships in topological structures, while neglecting the different information propagation delays between adjacent nodes in the convolution. Secondly, these methods often stack a large number of complex structures, resulting in a substantial increase in computational time during the model training phase, thereby disregarding the model's requirements for timeliness. In this paper, we propose a novel network called the Attention-Based Spatial-Temporal Fusion Graph Convolution Network (A-STFGCN). We design a spatial-temporal fusion block to extract the spatial-temporal feature correlations with propagation delay errors removed and to capture both long-term and short-term temporal characteristics of the data within a multi-head self-attention mechanism based on a mask matrix. Extensive experiments on five real-world datasets demonstrate that our method achieves the best overall performance while having good computation and data utilization efficiency compared with the eight baseline methods.

## Metadata
- **Published**: 2026-07-27T10:55:20Z
- **Authors**: Jinpeng Chen, Ziyu Yu, Tao Wang, Jun Ma, Hongbo Gao, Senzhang Wang, Zufeng Zhang, Kaimin Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24885v1)