---
title: Fast Gauss Sums via Flash Attention
published: 2026-09-04T09:11:45Z
authors: Nicolaj Rux, Sebastian Neumayer
url: http://arxiv.org/abs/2609.04910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast Gauss Sums via Flash Attention

## Abstract
Gaussian kernel sums are the computational core of maximum mean discrepancies (MMDs), kernel gradient flows, Stein variational gradient descent (SVGD), and many other kernel methods. At the same time, softmax attention has received an extraordinary amount of hardware-aware code engineering, culminating in flash attention. We show that Gauss kernel sums with arbitrary, signed weights can be evaluated via flash attention: two small input augmentations turn the normalized softmax reduction into the unnormalized Gauss sum, without writing a single line of custom GPU code. For feature dimension D>8 in fp16, this approach beats compiled PyTorch code as well as PyKeOps kernels (often significantly) in speed, memory-overhead and accuracy. Indeed, its memory scaling remains linear.

## Metadata
- **Published**: 2026-09-04T09:11:45Z
- **Authors**: Nicolaj Rux, Sebastian Neumayer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04910v1)