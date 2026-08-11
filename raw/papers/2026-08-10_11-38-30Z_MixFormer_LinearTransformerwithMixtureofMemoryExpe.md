---
title: MixFormer: Linear Transformer with Mixture of Memory Experts
published: 2026-08-10T11:38:30Z
authors: Yu Guo, Lei Duan
url: http://arxiv.org/abs/2608.09468v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MixFormer: Linear Transformer with Mixture of Memory Experts

## Abstract
State Space Models (SSMs), as a mainstream research direction of linear Transformers, aim to achieve higher efficiency than standard Transformers in long-context modeling. However, existing SSMs suffer from limited input adaptivity and constrained memory capacity, leading to information loss when modeling ultra-long sequences. To address these limitations, we propose MixFormer, a novel linear Transformer that integrates a Mixture-of-Memory-Experts (MoE) mechanism. Specifically, the model maintains differentiated memory states through multiple collaborating memory experts and employs a novel Time-Aware Linear Attention (TALA) mechanism, which leverages learnable exponential decay functions and positional biases to dynamically update memory. This design enables the model to selectively reinforce important historical information while effectively mitigating memory dilution, substantially improving long-range dependency modeling. Experiments on long-sequence text and image generation tasks demonstrate that MixFormer not only achieves significant performance gains but also provides a more sustainable computational backbone for the next generation of web infrastructure.

## Metadata
- **Published**: 2026-08-10T11:38:30Z
- **Authors**: Yu Guo, Lei Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09468v1)