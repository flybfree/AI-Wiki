---
title: AVQ-Attention: Adaptive Vector-Quantized Attention
published: 2026-07-14T14:02:22Z
authors: Winfried van den dool, Patrick Forré, Amir Habibian, Yuki M. Asano, Max Welling
url: http://arxiv.org/abs/2607.12789v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AVQ-Attention: Adaptive Vector-Quantized Attention

## Abstract
The $\mathcal{O}(N^2)$ complexity of attention over $N$ tokens remains a computational bottleneck in transformer models. Vector-Quantized (VQ) attention reduces this to $\mathcal{O}(MN)$ by representing keys with $M$ codewords, but applies uniform codebook capacity regardless of where attention mass concentrates: high-attention regions of key space may be coarsely approximated while low-attention regions waste representational capacity. We propose Adaptive Vector-Quantized (AVQ) Attention, which adaptively allocates codebook capacity based on attention importance. Starting from a small set of codewords, our method identifies the most important codes during the forward pass and refines them with pre-learned child codewords, achieving fine-grained quantization where it matters most while maintaining coarse quantization elsewhere. We develop an implementation using custom Triton kernels that enables the full adaptive refinement process, including importance scoring, child codeword insertion, and parent contribution replacement, to be carried out within the tiled computation paradigm of Flash Attention with minimal overhead. Our approach maintains $\mathcal{O}(MN)$ complexity while achieving improved accuracy-efficiency trade-offs compared to fixed-codebook VQ-attention.

## Metadata
- **Published**: 2026-07-14T14:02:22Z
- **Authors**: Winfried van den dool, Patrick Forré, Amir Habibian, Yuki M. Asano, Max Welling
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.12789v1)