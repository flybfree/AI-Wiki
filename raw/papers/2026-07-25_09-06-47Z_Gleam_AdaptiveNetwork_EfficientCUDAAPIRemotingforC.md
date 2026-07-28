---
title: Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs
published: 2026-07-25T09:06:47Z
authors: Zhihao Xu, Hao Zhong, Zeting Zhou, Yuhang Xu, Haoyu Tong, Wei Wang, Jinshan Chen, Keqiang He, Chong Zhu, Shengzhong Liu, Fan Wu, Guihai Chen
url: http://arxiv.org/abs/2607.23115v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs

## Abstract
This paper aims to enable computation- and communication-efficient GPU sharing across devices within local area networks (LANs), facilitating ubiquitous AI inference on heterogeneous personal devices. We achieve distributed task offloading via CUDA API remoting. However, beyond raw computation, network constraints emerge as the primary bottleneck: limited bandwidth, high-frequency API invocations, and cross-task contention significantly hinder performance. To address these challenges, we propose Gleam, a novel and network-efficient framework for task-generic GPU sharing across local-area CUDA devices, with three key contributions. First, we reduce bandwidth overhead in CUDA API remoting through automatic model weight caching, and mitigate accumulated latency from frequent API calls by asynchronous execution. Second, we design a runtime task scheduler that dynamically determines API remoting pairs between LAN clients and servers, explicitly accounting for both network conditions and GPU resource contention under parallel workloads. Finally, we introduce dedicated mechanisms to ensure CUDA context consistency across distributed executions. Extensive experiments on heterogeneous NVIDIA GPUs and diverse AI workloads show Gleam consistently outperforms state-of-the-art baselines, achieving 1.4-24.2 times improvements in API remoting efficiency and up to 1.79 times higher system throughput.

## Metadata
- **Published**: 2026-07-25T09:06:47Z
- **Authors**: Zhihao Xu, Hao Zhong, Zeting Zhou, Yuhang Xu, Haoyu Tong, Wei Wang, Jinshan Chen, Keqiang He, Chong Zhu, Shengzhong Liu, Fan Wu, Guihai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23115v1)