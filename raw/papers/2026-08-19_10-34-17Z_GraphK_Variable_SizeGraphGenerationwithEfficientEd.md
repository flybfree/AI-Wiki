---
title: GraphK: Variable-Size Graph Generation with Efficient Edge Construction
published: 2026-08-19T10:34:17Z
authors: Resul Tugay, Eren Oluğ, Elif Ak, Sule Gunduz Oguducu
url: http://arxiv.org/abs/2608.18777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphK: Variable-Size Graph Generation with Efficient Edge Construction

## Abstract
Graph generation models have advanced significantly with deep learning, yet they remain limited in scalability, flexibility, and ability to model underlying structures. We present GraphK, a novel encoder-sampler-decoder framework for graph generation that overcomes these challenges through structural flexibility and computational efficiency. Unlike autoregressive approaches constrained by vocabulary size (i.e. number of nodes in graph generation), GraphK allows for both upscaling (generating graphs with more nodes than the input) and downscaling, providing a flexible control over output graph size. By learning permutation-invariant latent representations and sampling new node embeddings via maximum likelihood estimation, GraphK generalizes across graph sizes and structures. For edge generation, we employ edge prediction with a KDTree-based top-k neighbor search in the latent space, reducing computational cost. Based on the manifold smoothness assumption, our method effectively captures graph properties. Experiments on synthetic and real-world datasets show that GraphK outperforms existing methods, accurately learns graph structures, and generates synthetic graphs without explicit definitions.

## Metadata
- **Published**: 2026-08-19T10:34:17Z
- **Authors**: Resul Tugay, Eren Oluğ, Elif Ak, Sule Gunduz Oguducu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18777v1)