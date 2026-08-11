---
title: SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization
published: 2026-08-10T06:16:24Z
authors: Gyudong Kim, Wonjun Han, Young Geun Kim
url: http://arxiv.org/abs/2608.09160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization

## Abstract
Query-Key Normalization (QK-Norm) improves the training stability and quality of modern Large Language Models (LLMs). However, under Tensor Parallelism (TP), layerwise QK-Norm introduces additional cross-GPU communication because the normalization factor depends on the full hidden vector. We present SwiftQK, a multi-GPU RMSNorm kernel that exchanges only scalar normalization statistics and overlaps the remaining Peer-to-Peer reduction with independent element-wise computation in a deadlock-safe persistent kernel. Evaluations on recent LLMs show that SwiftQK reduces QK-Norm latency by 81.4--93.9% relative to the standard TP QK-Norm using full-vector All-Gather. In end-to-end serving, SwiftQK reduces TPOT on average by 29.5% over the All-Gather-based baseline and by 14.3% over an optimized scalar-aggregation implementation.

## Metadata
- **Published**: 2026-08-10T06:16:24Z
- **Authors**: Gyudong Kim, Wonjun Han, Young Geun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09160v1)