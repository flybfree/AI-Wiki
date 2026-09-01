---
title: CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration
published: 2026-08-31T06:02:37Z
authors: Haoyun Jiang, Haolin Li, Jianwei Zhang, Fei Huang, Qiang Hu, Minmin Sun, Shuai Xiao, Yong Li, Junyang Lin, Jiangchao Yao
url: http://arxiv.org/abs/2608.30295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration

## Abstract
Large language models (LLMs) have demonstrated strong capabilities in handling long-context tasks, but processing such long contexts remains challenging due to the substantial memory requirements and inference latency. In this work, we discover that certain attention heads exhibit sequential consistency in their attention patterns, which can be persistently identified using a coefficient-of-variation-based algorithm. Inspired by this observation, we propose CateKV, a hybrid KV cache method that retains only critical token information for consistent heads, thereby reducing KV cache size and computational overhead, while preserving the majority of KV pairs in adaptive heads to ensure high accuracy. We show the unique characteristics of our algorithm and its extension with existing acceleration methods. Comprehensive evaluations on long-context benchmarks show that, while maintaining accuracy comparable to full attention, CateKV reduces memory usage by up to $2.72\times$ and accelerates decoding by $2.18\times$ in single-sample inputs, and boosts throughput by $3.96\times$ in batch scenarios.

## Metadata
- **Published**: 2026-08-31T06:02:37Z
- **Authors**: Haoyun Jiang, Haolin Li, Jianwei Zhang, Fei Huang, Qiang Hu, Minmin Sun, Shuai Xiao, Yong Li, Junyang Lin, Jiangchao Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30295v1)