---
title: PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression
published: 2026-08-24T21:30:11Z
authors: Zizhong Wang, Jieying Wang, Zhao Zhang, Jiajia Li
url: http://arxiv.org/abs/2608.23843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression

## Abstract
Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache. KV cache compression addresses this problem by reducing the storage cost of previous tokens. Among existing approaches, low-rank compression is particularly attractive because it represents every token in reduced dimensions. Previous low-rank methods typically derive fixed projection spaces from model weights, construct fixed spaces from calibration activations, or construct a shared basis over a broad cache region. Such representations may not capture detailed but important information. We partition each per-head KV cache into fixed-length logical pages and observe substantial low-rank structure within individual pages. Based on this observation, we propose PuzzleKV, a training- and calibration-free method that treats each completed page as an independent compression unit. PuzzleKV decomposes pages within each layer and KV head, computes attention directly over dense and factorized pages, and incrementally compresses newly eligible pages during autoregressive decoding. Experiments across models, context lengths, and benchmarks demonstrate the effectiveness of PuzzleKV under matched storage budgets. At approximately 60% of the original KV cache storage, PuzzleKV achieves more than 96% of Full KV performance across both evaluated models and all benchmark settings, with substantial gains over Global SVD on RULER and competitive performance on LongBench. To achieve a more aggressive compression ratio, PuzzleKV can be further combined with quantization while retaining more than 93% of Full KV performance using only 18.7% of the original storage.

## Metadata
- **Published**: 2026-08-24T21:30:11Z
- **Authors**: Zizhong Wang, Jieying Wang, Zhao Zhang, Jiajia Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23843v1)