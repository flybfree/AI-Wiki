---
title: FraQ: Efficient Coordinate-Space Recompression for Federated Low-Rank Adaptation
published: 2026-08-04T12:57:08Z
authors: Shenghui Li, Thiemo Voigt
url: http://arxiv.org/abs/2608.03605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FraQ: Efficient Coordinate-Space Recompression for Federated Low-Rank Adaptation

## Abstract
Federated fine-tuning with Low-Rank Adaptation (LoRA) enables efficient collaborative adaptation of Large Language Models (LLMs) without centralizing private data. However, LoRA's two-factor parameterization creates an aggregation mismatch across clients: naively averaging the factors does not recover the average of their induced updates. This mismatch can be avoided by forming the exact aggregate in the full weight space and then recompressing it, but decomposing the resulting dense matrix is computationally expensive and memory-intensive. We propose FraQ, an efficient coordinate-space recompression method for federated LoRA. Starting from stacked factors that exactly represent the aggregate, FraQ factorizes it into an orthonormal basis and a compact coordinate matrix. It then recovers the singular spectrum from a small Gram matrix, selects the smallest rank satisfying a prescribed energy threshold, and maps the selected coordinate subspace back through the basis to construct the global adapter. Experiments on text classification and commonsense reasoning benchmarks show that FraQ achieves accuracy close to uncompressed baselines while substantially reducing downlink communication with low server-side recompression overhead.

## Metadata
- **Published**: 2026-08-04T12:57:08Z
- **Authors**: Shenghui Li, Thiemo Voigt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03605v1)