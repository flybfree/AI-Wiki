---
title: VFold: Symmetry-Aware Cross-Layer Value Cache Compression
published: 2026-10-08T17:14:28Z
authors: Neha Verma, Sungwon Kim, Kenton Murray, Kevin Duh
url: http://arxiv.org/abs/2610.12338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VFold: Symmetry-Aware Cross-Layer Value Cache Compression

## Abstract
While caching key-value (KV) states accelerates Large Language Model (LLM) decoding, this cache can dominate memory usage at long context lengths. One solution is to compress this memory by exploiting inter-layer cache similarities. However, most existing techniques necessitate architectural changes to LLMs and incur substantial overhead. In this work, we propose a symmetry-aware value cache merging strategy that reduces cache memory while avoiding both harmful performance degradation and architectural overhead during decoding. Furthermore, we show that this approach can be exploited alongside existing cache compression techniques, composing with high-ratio quantization or key cache pruning to reach compression ratios that neither method reaches alone, with minimal additional cost. Ultimately, our findings reveal a major source of underutilized capacity in the value cache, offering a simple yet highly effective direction for scaling context windows under memory constraints.

## Metadata
- **Published**: 2026-10-08T17:14:28Z
- **Authors**: Neha Verma, Sungwon Kim, Kenton Murray, Kevin Duh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12338v1)