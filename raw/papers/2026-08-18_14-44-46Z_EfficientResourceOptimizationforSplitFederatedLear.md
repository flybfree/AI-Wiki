---
title: Efficient Resource Optimization for Split Federated Learning
published: 2026-08-18T14:44:46Z
authors: Wei Wei, Xianhao Chen
url: http://arxiv.org/abs/2608.17849v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Resource Optimization for Split Federated Learning

## Abstract
Split federated learning (SFL) has emerged as a powerful paradigm for model training at the edge. However, SFL inherently involves discrete decision variables for model splitting and resource allocation, resulting in a challenging mixed-integer problem. Consequently, prior optimization schemes for SFL are either \textit{heuristic} or \textit{computationally inefficient}, which cannot handle large-scale user populations. To address this limitation, this work establishes an efficient optimization framework for SFL under resource-constrained networks. Our framework jointly optimizes model splitting and resource allocation to minimize training cost, which is defined as the weighted sum of latency and energy costs. We first study the model splitting problem and develop a polynomial-time algorithm that achieves the global optimum. Then, we extend the approach to the joint model splitting and resource allocation problem. In this case, we formulate it as a two-dimensional master problem and develop an efficient approximation method with a $(1+ε)$-approximation guarantee. Extensive experiments show that the proposed approach provides efficient solutions to strike the optimal energy--latency tradeoff.

## Metadata
- **Published**: 2026-08-18T14:44:46Z
- **Authors**: Wei Wei, Xianhao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17849v1)