---
title: RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search
published: 2026-08-31T07:40:57Z
authors: Rastislav Lenhardt, Teodora Dobos, Thomas Vecchiato, Jiri Isa, Igor Ginzburg
url: http://arxiv.org/abs/2608.30384v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RSLM: Training-Free Vector Quantization for Approximate Nearest Neighbor Search

## Abstract
By introducing RSLM (Rotated Scaled Lloyd-Max), a family of training-free vector quantization codecs compressing embeddings to 1--4 bits per dimension, we reduce memory cost and memory bandwidth of a typical large-scale Approximate Nearest Neighbor (ANN) search system, while reducing its complexity and keeping or improving recall across multiple benchmark datasets. State-of-the-art systems filter candidates using coarse partitions, approximately score them to narrow the set, and then rescore the best with higher precision representations (often >=8 bits per dimension). Our relativized codecs can bring this down to 2--4 bits per dimension.   We use the properties of the ANN system to encode residual vectors instead of full vectors, both for the approximate scoring phase and the rescoring phase. Since Maximum Inner Product Search (MIPS) is very sensitive to vector norms, we correct the $L_2$ norms of quantized vectors. Our major innovation is that we correct the $L_2$ norm of the final reconstructed vector rather than just the residual. Our rescaling replaces more complicated schemes, such as Anisotropic loss. The residualization scheme gives us a more favorable quality vs size trade-off than generic quantization methods.   Our high-performance implementation leverages a block-wise cascaded Fast Walsh-Hadamard Transform (FWHT) with linear-like complexity, AVX SIMD-optimized codebooks, and a steganographic encoding of scaling factors for perfect cache-line alignment.

## Metadata
- **Published**: 2026-08-31T07:40:57Z
- **Authors**: Rastislav Lenhardt, Teodora Dobos, Thomas Vecchiato, Jiri Isa, Igor Ginzburg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30384v1)