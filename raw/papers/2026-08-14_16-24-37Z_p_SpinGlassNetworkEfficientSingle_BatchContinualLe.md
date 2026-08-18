---
title: p-Spin Glass Network Efficient Single-Batch Continual Learning
published: 2026-08-14T16:24:37Z
authors: Vladimer Khasia
url: http://arxiv.org/abs/2608.14774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# p-Spin Glass Network Efficient Single-Batch Continual Learning

## Abstract
Modern sequence models heavily rely on massive memory footprints and large-batch stochastic optimization, barriers that restrict sample efficiency and continual learning. We introduce the $p$-Spin Glass Network, a novel architecture that overcomes these limitations, structurally manages optimization variance and yields four noticeable capabilities: 1. It enforces memory efficiency: native ternary quantization compresses internal parameters by $8\times$, while exact implicit gradients strictly bound activation memory to $\mathcal{O}(B \cdot T \cdot D)$. 2. it demonstrates sample efficiency, matching the asymptotic performance of a Transformer baseline while utilizing $8\times$ fewer training sequences. 3. Method enables single-batch stability and smooth, monotonic convergence at a stochastic micro-batch size of $1$. 4. Finally, this stability proves modality-agnostic, maintaining robust temporal credit assignment across both discrete subword and long horizon uncompressed raw byte streams. Ultimately, this work removes large batch requirement for stable deep learning, establishing a foundation for continuous learning and edge AI.

## Metadata
- **Published**: 2026-08-14T16:24:37Z
- **Authors**: Vladimer Khasia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14774v1)