---
title: GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving
published: 2026-09-03T07:53:05Z
authors: Qiankun Ma, Yanjiang Zhou, Zinan Xiong, Haofei Wang, Zhen Song, Yang Xiang, Ziyao Zhang, Hairong Zheng
url: http://arxiv.org/abs/2609.03494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving

## Abstract
Long-output reasoning has made the key--value (KV) cache a critical memory bottleneck for efficient LLM serving. Existing KV compression methods usually rely on a predefined per-request budget and adjust only which KV states are retained, leaving the total capacity fixed throughout decoding. However, reasoning workloads exhibit substantial demand variation: different requests require different KV capacities, and the attention demand of an individual request evolves during generation. We introduce \textbf{GrowPage}, an on-demand KV budgeting framework that treats KV capacity as a runtime resource. GrowPage maintains lightweight dual-timescale query summaries to capture recent and long-term attention behaviors, and uses their relative attention working sets to estimate demand evolution. At each capacity boundary, GrowPage either compresses KV states within the current allocation or acquires an additional physical page when broader demand emerges. By integrating with PagedAttention's page-level memory abstraction, GrowPage preserves continuous batching and prefix caching. Experiments on reasoning benchmarks across multiple models show that GrowPage achieves a superior performance--throughput trade-off over existing approaches.

## Metadata
- **Published**: 2026-09-03T07:53:05Z
- **Authors**: Qiankun Ma, Yanjiang Zhou, Zinan Xiong, Haofei Wang, Zhen Song, Yang Xiang, Ziyao Zhang, Hairong Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03494v1)