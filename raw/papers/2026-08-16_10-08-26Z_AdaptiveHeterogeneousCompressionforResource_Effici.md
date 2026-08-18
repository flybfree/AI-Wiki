---
title: Adaptive Heterogeneous Compression for Resource-Efficient Federated Knowledge Distillation
published: 2026-08-16T10:08:26Z
authors: Chenwang Liu, Yijun Liu, Chang Liu, Xu Zhang, Pengchao Han
url: http://arxiv.org/abs/2608.15660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Heterogeneous Compression for Resource-Efficient Federated Knowledge Distillation

## Abstract
Federated learning (FL) enables privacy-preserving distributed model training but faces challenges from heterogeneous model architectures and limited communication resources at the network edge. Federated knowledge distillation (FedKD) alleviates model heterogeneity by combining prototype-wise parameter aggregation and knowledge transfer across heterogeneous models. However, transmitting gradients still introduces considerable communication overhead, while existing compression approaches typically apply a uniform strategy across clients and ignore their diverse model characteristics and resource capacities. To address this issue, we propose a heterogeneous compression framework for FedKD that enables each client to select a compression strategy from a candidate strategy set. We formulate the compression strategy selection problem as a non-stationary stochastic multi-armed bandit (MAB), where each arm corresponds to a compression strategy. An efficiency-aware reward is designed by jointly considering local optimization improvement, global knowledge alignment, and execution time. Based on this formulation, we develop an Adaptive heterogeneouS Compression algorithm for fEderated kNowledge Distillation (ASCEND), which employs an exponential moving average (EMA)-enhanced $ε$-greedy policy to balance exploration and exploitation. Experimental results on multiple datasets demonstrate that ASCEND effectively adapts to heterogeneous model and resource settings, reducing communication overhead and training time while maintaining competitive model accuracy.

## Metadata
- **Published**: 2026-08-16T10:08:26Z
- **Authors**: Chenwang Liu, Yijun Liu, Chang Liu, Xu Zhang, Pengchao Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15660v1)