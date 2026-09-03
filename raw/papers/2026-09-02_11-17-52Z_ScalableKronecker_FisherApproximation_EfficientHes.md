---
title: Scalable Kronecker-Fisher Approximation: Efficient Hessian Analysis for Billion-Parameter Language Models Compression
published: 2026-09-02T11:17:52Z
authors: Viacheslav Yusupov, Daria Cherniuk, Evgeny Frolov
url: http://arxiv.org/abs/2609.02451v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable Kronecker-Fisher Approximation: Efficient Hessian Analysis for Billion-Parameter Language Models Compression

## Abstract
In this paper, we propose a scalable Kronecker-based approximation that captures cross-layer interactions without storing the entire Fisher matrix, enabling practical Hessian analysis for billion-parameter networks where full computation is infeasible. Our approach reveals consistent vulnerability patterns: value projection layers exhibit the highest sensitivity and strongest cross-layer correlations across multiple model families, while other components exhibit architecture-specific behaviors. Through extensive experiments on quantization, sparsification, inter-layer corruption, and post-corruption fine-tuning, we demonstrate that our approximation strongly correlates with both performance degradation and recovery. Our framework provides a practical, theoretically grounded tool for identifying fragile components in large models, opening new avenues for guided compression and optimization strategies, such as mixed-precision allocation, layer-wise sparsity, and adaptive low-rank decomposition across layers and even individual weight groups.

## Metadata
- **Published**: 2026-09-02T11:17:52Z
- **Authors**: Viacheslav Yusupov, Daria Cherniuk, Evgeny Frolov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02451v1)