---
title: Do Neural Networks Really Beat the Curse of Dimensionality? A Bit-Complexity View
published: 2026-08-02T16:20:19Z
authors: Tong Mao, Jinchao Xu
url: http://arxiv.org/abs/2608.01357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Neural Networks Really Beat the Curse of Dimensionality? A Bit-Complexity View

## Abstract
Traditional approximation theory measures convergence rates in terms of the number of parameters or degrees of freedom. However, practical computation operates under finite precision: parameters must be encoded using a finite number of bits. Therefore, approximation efficiency should be evaluated in terms of computational bit complexity, which is intrinsically connected to the metric entropy of the underlying function class.   In this work, we develop a unified approximation framework based on binary encoding and metric entropy. We analyze classical methods (including polynomial approximation, sparse grids, and finite elements) as well as shallow and deep neural networks, and compare their approximation rates for function classes with comparable metric entropy. We observe that, when evaluated in terms of bits, most classical methods are in general suboptimal relative to the intrinsic limits dictated by metric entropy, while neural network methods may exhibit different behaviors. We show that when complexity is measured in bits rather than parameters, no method fundamentally exceeds the approximation order achieved by classical approaches.   Our results also indicate that many seeming advantages of neural networks, including dimension-independent rates and superconvergence phenomena, stem from differences in function class complexity rather than intrinsic architectural superiority. In this sense, the traditional curse of dimensionality can be misleading; the fundamental limitation is instead a curse of bit complexity, governed by metric entropy.

## Metadata
- **Published**: 2026-08-02T16:20:19Z
- **Authors**: Tong Mao, Jinchao Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01357v1)