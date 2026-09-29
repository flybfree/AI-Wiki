---
title: DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory
published: 2026-09-28T05:55:33Z
authors: Xuan Truong Nguyen, Tien Son Pham, Tuan Duc Chu, Wookeun Jung, Thanh Tuan Dao
url: http://arxiv.org/abs/2609.34380v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory

## Abstract
Existing LLM serving systems virtualize and optimize KV-cache memory, but treat model-weight memory as fixed throughout execution. Recent work on multi-precision model representations challenges this design by allowing a single stored model to support both full-accuracy and lower-precision execution, making the effective weight footprint runtime-dependent. This creates an opportunity under bursty workloads, where temporary spikes in KV-cache demand often determine throughput and SLO compliance. We present DPS, a dual-precision LLM serving system that turns weight memory into an elastic resource: under normal load, DPS serves the full-accuracy model; under KV pressure, it switches to a nested, lower-precision variant and repurposes unused weight memory for KV cache blocks. DPS is built on Semi-Unified Memory (SUM), which partitions the weight region into a persistent lower-precision sub-region and a shared region that alternates between residual weight tensors and KV-cache blocks, preserving compatibility with paged KV-cache management. We implement DPS on top of vLLM and evaluate it across both dense and MoE models and various production workload traces. Our results show that \sysname improves sustained throughput by $2.1$--$3.3\times$ and effective pass@1 by up to $+41$\,pp over Static FP16, while preserving FP16-class accuracy.

## Metadata
- **Published**: 2026-09-28T05:55:33Z
- **Authors**: Xuan Truong Nguyen, Tien Son Pham, Tuan Duc Chu, Wookeun Jung, Thanh Tuan Dao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34380v1)