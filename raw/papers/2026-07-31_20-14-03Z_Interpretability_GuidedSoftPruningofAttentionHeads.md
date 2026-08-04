---
title: Interpretability-Guided Soft Pruning of Attention Heads in Vision Transformers
published: 2026-07-31T20:14:03Z
authors: Kamil Książek, Piotr Suszyński, Michał Jan Włodarczyk, Jacek Tabor, Przemysław Biecek
url: http://arxiv.org/abs/2608.00264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretability-Guided Soft Pruning of Attention Heads in Vision Transformers

## Abstract
Vision foundation models, such as DINOv2, learn highly expressive representations but rely on massive, opaque architectures that demand substantial computational power and memory. To provide an interpretable-guided and efficient solution to this issue, we first propose a spectral analysis and new visualization technique for individual attention heads based on the Laplacian eigenvectors of their attention maps. Building upon recent observations regarding the block structure of Vision Transformers, we perform semantic clustering of attention heads and identify functional redundancies. Leveraging these insights, we introduce SAPER (Soft Attention PrunER), an end-to-end differentiable pruning framework based on the LapSum Soft Top-K approach. Extensive experiments on ImageNet-1K demonstrate that SAPER achieves a highly favorable accuracy-efficiency trade-off, outperforming the competitive RAPTOR baseline in FLOPs reduction while preserving strong classification performance.

## Metadata
- **Published**: 2026-07-31T20:14:03Z
- **Authors**: Kamil Książek, Piotr Suszyński, Michał Jan Włodarczyk, Jacek Tabor, Przemysław Biecek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00264v1)