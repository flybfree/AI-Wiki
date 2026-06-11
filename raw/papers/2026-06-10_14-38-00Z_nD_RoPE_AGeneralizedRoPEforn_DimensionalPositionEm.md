---
title: nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding
published: 2026-06-10T14:38:00Z
authors: Boyang Li, Yulin Wu, Sizhe Xu, Nuoxian Huang, Zhonghang Yuan, Shangyi Guo, Shu Yang, Takahiro Yabe
url: http://arxiv.org/abs/2606.12146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding

## Abstract
Rotary Position Embedding (RoPE) is widely adopted in Transformer models, yet its extension to high-dimensional domains lacks a unified theoretical formulation. Most existing approaches either apply rotations independently along each axis or empirically mix frequencies, which limits cross-dimensional interactions and yields direction-dependent representations. To address these limitations, we propose nD-RoPE, a decomposition-free generalization of RoPE to arbitrary dimensions. From a translation-invariant formulation in continuous Hilbert space, we derive a spectral condition for isotropy that requires treating positions and frequencies as coupled \(n\)-dimensional vectors. We instantiate this formulation with a multi-scale regular-simplex wave-vector design, which provides non-degenerate spatial coverage and a symmetric, directionally balanced second-order response. Experiments across images, videos, and point clouds demonstrate consistent performance gains and improved generalization in high-dimensional settings.

## Metadata
- **Published**: 2026-06-10T14:38:00Z
- **Authors**: Boyang Li, Yulin Wu, Sizhe Xu, Nuoxian Huang, Zhonghang Yuan, Shangyi Guo, Shu Yang, Takahiro Yabe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12146v1)