---
title: SGD-KV: Summarization Guided KV Cache Compression
published: 2026-09-03T00:31:11Z
authors: Zeyu Liu, Woomin Song, Xuandi Fu, Sai Muralidhar Jayanthi, Vivek Govindan, Aram Galstyan, Sravan Babu Bodapati, Srikanth Ronanki
url: http://arxiv.org/abs/2609.03235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SGD-KV: Summarization Guided KV Cache Compression

## Abstract
Large language models (LLMs) face severe memory bottlenecks in long-context inference due to the linearly growing size of key-value (KV) caches. Existing KV cache compression techniques typically rely on simple heuristics, overlooking the distinct functional roles of different attention heads. We present SGD-KV (Summarization-Guided KV Cache Compression), a head-aware framework that leverages a novel chunk-summarization diagnostic task to systematically identify and prioritize attention heads specialized in hierarchical information aggregation. Experiments on Qwen2.5-7B-1M and Qwen3-32B across diverse long-context benchmarks demonstrate that SGD-KV achieves state-of-the-art performance with contexts up to 1M tokens, while reducing KV cache memory usage by up to 75%. Our findings show that strategically allocating the KV cache budget based on the summarization score distribution of attention heads yields a superior efficiency-accuracy trade-off for long-context inference.

## Metadata
- **Published**: 2026-09-03T00:31:11Z
- **Authors**: Zeyu Liu, Woomin Song, Xuandi Fu, Sai Muralidhar Jayanthi, Vivek Govindan, Aram Galstyan, Sravan Babu Bodapati, Srikanth Ronanki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03235v1)