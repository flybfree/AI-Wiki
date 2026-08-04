---
title: Gram-Space: Structure-Preserving Codebook Compression for Memory-Efficient Neuro-Symbolic AI
published: 2026-08-02T22:37:34Z
authors: Weilun Wang, Wantong Li
url: http://arxiv.org/abs/2608.01528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gram-Space: Structure-Preserving Codebook Compression for Memory-Efficient Neuro-Symbolic AI

## Abstract
Vector symbolic architectures (VSA) are widely used for reasoning in neuro-symbolic (NeSy) AI, yet high-dimensional codebooks often create severe memory bottlenecks that limit scalability and deployment. In this paper, we propose Gram-Space, a compression framework that applies Gram-Schmidt orthogonalization to represent codebook vectors in a compact orthonormal coordinate system. Gram-Space preserves the dot-product structure required by matrix-based VSA operators, which supports numerically equivalent execution of matrix similarity, probability vectorization, and attention score computations. We provide a correctness analysis showing that inner products are preserved under the orthonormal basis representation. Using modern GPU hardware, we benchmark the Gram-Space framework on standard neuro-symbolic reasoning datasets. Experimental evaluations across state-of-the-art VSA models show that Gram-Space reduces model-level GPU memory usage by up to 15.75x and improves inference latency by up to 3.62x. Profiling results further indicate that Gram-Space reduces allocation-heavy overhead in codebook-associated stages and improves hardware utilization for NeSy workloads.

## Metadata
- **Published**: 2026-08-02T22:37:34Z
- **Authors**: Weilun Wang, Wantong Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01528v1)