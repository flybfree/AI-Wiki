---
title: S$^4$R: Selective Sampling, Subspaces, and Sparse Reconstruction for Compressed Long-Context KV Caching
published: 2026-08-01T08:41:29Z
authors: Jialong Han, You Wu, Kewei Tu
url: http://arxiv.org/abs/2608.00528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# S$^4$R: Selective Sampling, Subspaces, and Sparse Reconstruction for Compressed Long-Context KV Caching

## Abstract
The growth of context window lengths in Large Language Models (LLMs) significantly enhances their long-context capabilities but incurs prohibitive memory costs due to the Key-Value (KV) cache. Although low-rank compression of KV cache is a promising remedy, existing methods face a dilemma: offline approaches depend on external calibration data, whereas online approaches incur substantial compute for full-prompt decomposition and reconstruction. In this paper, we propose S$^4$R, which builds low-rank subspaces from selectively sampled tokens and computes attention over a sparsely reconstructed KV representation. S$^4$R uses prompt-aware initialization to build initial key/value bases from a representative prompt subset, trading off calibration-data dependence against prefilling cost. Because fully reconstructing the cache at every decoding step is prohibitively expensive and hurts throughput, we further adopt sparse reconstruction to retain only informative positions during decoding. Extensive experiments on LongBench and RULER with Llama and Qwen model families show that S$^4$R achieves up to 5$\times$ KV compression with near full-cache accuracy, combining the efficiency of fixed compression with the adaptability of prompt-dependent methods.

## Metadata
- **Published**: 2026-08-01T08:41:29Z
- **Authors**: Jialong Han, You Wu, Kewei Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00528v1)