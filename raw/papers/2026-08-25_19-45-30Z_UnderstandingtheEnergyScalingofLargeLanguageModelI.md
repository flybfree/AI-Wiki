---
title: Understanding the Energy Scaling of Large Language Model Inference Across Context Lengths and Attention Architectures
published: 2026-08-25T19:45:30Z
authors: Molka Chkir, Syed Muhammad Danish, Jos Höll, Arghavan Asad
url: http://arxiv.org/abs/2608.25096v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding the Energy Scaling of Large Language Model Inference Across Context Lengths and Attention Architectures

## Abstract
The growing adoption of large language models (LLMs) has raised increasing concerns about the energy consumption and environmental impact of inference. This paper presents a systematic empirical study of decode-phase energy consumption across representative open-source LLMs employing Multi-Head Attention (MHA), Grouped Query Attention (GQA), and Grouped Query Attention with Sliding Window Attention (SWA) to characterize how attention architecture influences decode-phase energy consumption under varying inference workloads. We evaluate four models across different context lengths, batch sizes, and generation workloads while measuring GPU energy using NVIDIA hardware counters. We examine the effects of context length, attention mechanism, Key-Value (KV) cache growth, and batching on decode-phase energy consumption. Results show that attention mechanism is the primary factor governing how decode energy scales with context length. MHA models exhibit substantially steeper energy growth than GQA models, whereas GQA with SWA maintains nearly constant energy consumption. We further show that model size primarily determines absolute energy consumption, while batching reduces both energy per generated token and request latency by up to 87%. These findings provide practical guidance for selecting energy-efficient LLM architectures and inference configurations.

## Metadata
- **Published**: 2026-08-25T19:45:30Z
- **Authors**: Molka Chkir, Syed Muhammad Danish, Jos Höll, Arghavan Asad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25096v1)