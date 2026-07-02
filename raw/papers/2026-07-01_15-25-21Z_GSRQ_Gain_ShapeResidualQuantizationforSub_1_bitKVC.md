---
title: GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache
published: 2026-07-01T15:25:21Z
authors: Soosung Kim, Minjae Park, Eui-Young Chung, Jaeyong Chung
url: http://arxiv.org/abs/2607.01065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache

## Abstract
The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit regime by progressively encoding residuals with small codebooks. However, most VQ methods still rely on standard $\ell_2$ $K$-means as the core codebook-learning primitive. We identify a subtle high-dimensional issue of this primitive: Euclidean centroid averaging can induce centroid shrinkage, which weakens the angular alignment term in the $\ell_2$ distortion and makes directional preservation harder. To address this issue, we propose Gain-Shape $K$-means (GSKM), a drop-in replacement for $K$-means that improves directional fidelity while matching, and in some regimes improving, $\ell_2$ distortion. We then build Gain-Shape Residual Quantization (GSRQ) by incorporating a weighted extension of GSKM into an RQ pipeline. On LLaMA-3-8B, GSRQ substantially improves over strong KV cache quantization baselines across bit rates. At 1-bit, it improves the average accuracy across LongBench tasks from 11.34 to 33.54, a gain of 22.20 percentage points over VQLLM.

## Metadata
- **Published**: 2026-07-01T15:25:21Z
- **Authors**: Soosung Kim, Minjae Park, Eui-Young Chung, Jaeyong Chung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01065v1)