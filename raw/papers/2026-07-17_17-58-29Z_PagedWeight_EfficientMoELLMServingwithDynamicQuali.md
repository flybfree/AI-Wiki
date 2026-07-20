---
title: PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization
published: 2026-07-17T17:58:29Z
authors: Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
url: http://arxiv.org/abs/2607.16184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

## Abstract
Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances expert-weight precision with the KV cache sizes. PagedWeight exposes and effectively navigates the complex tradeoff between the model's task accuracy, memory consumption, and throughput/latency. Across several memory-sensitive MoE serving scenarios, PagedWeight improves the quality-memory tradeoff over several existing quantization baselines. PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss.

## Metadata
- **Published**: 2026-07-17T17:58:29Z
- **Authors**: Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16184v1)