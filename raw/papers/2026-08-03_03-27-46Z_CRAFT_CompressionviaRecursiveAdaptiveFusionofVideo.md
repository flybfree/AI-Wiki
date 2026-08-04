---
title: CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens for Vision-Language Models
published: 2026-08-03T03:27:46Z
authors: Yu Chen, Xiaohong Li, Xiaole Wang, Jianjin Zhang, Jun Sun, Yafeng Deng
url: http://arxiv.org/abs/2608.01644v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens for Vision-Language Models

## Abstract
In video understanding, vision-language models (VLMs) must ingest massive numbers of visual tokens, causing the computational and memory cost of the prefill stage to rise sharply. Such visual sequences are highly redundant along the spatio-temporal dimension, yet a high compression ratio is often accompanied by the loss of critical details. Existing token-compression methods either employ heuristic, training-free compression with limited content adaptivity or introduce additional modules that require expensive alignment training, leaving the trade-off between efficiency and adaptivity unresolved. To alleviate this limitation, we propose CRAFT: Compression via Recursive Adaptive Fusion of Video Tokens. CRAFT recursively merges tokens by decoupling parameter-free token selection from learnable token fusion: global similarity determines which tokens to merge, while a position-aware weighting module and a content-adaptive channel-wise gate learn how to fuse them. The whole compression pipeline is query-agnostic. Because every retained token is a linear combination of the original tokens, CRAFT preserves their true spatio-temporal coordinates and stays aligned with the pre-trained language model's input distribution. Experiments on multiple representative video benchmarks show that CRAFT consistently outperforms prior state-of-the-art token-compression methods. At about $8\times$ compression, it retains roughly $97\%$ of the backbone's average accuracy and shows significant efficiency improvement.

## Metadata
- **Published**: 2026-08-03T03:27:46Z
- **Authors**: Yu Chen, Xiaohong Li, Xiaole Wang, Jianjin Zhang, Jun Sun, Yafeng Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01644v1)