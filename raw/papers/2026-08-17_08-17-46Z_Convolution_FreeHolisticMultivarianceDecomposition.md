---
title: Convolution-Free Holistic Multivariance Decomposition Layer for Efficient Hyperspectral Image Classification Tensor Networks
published: 2026-08-17T08:17:46Z
authors: Süha Tuna, Ülker Başar
url: http://arxiv.org/abs/2608.16241v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Convolution-Free Holistic Multivariance Decomposition Layer for Efficient Hyperspectral Image Classification Tensor Networks

## Abstract
Feature extraction for hyperspectral image classification is conventionally addressed using rigid tensor decompositions that fail to capture complex spatio-spectral interdependencies, or heavily parameterized convolutional neural networks that are computationally expensive. To overcome these limitations, this work introduces the Holistic Multivariance Decomposition (HMD) framework as a novel, end-to-end differentiable neural network layer. By explicitly separating independent single mode variations from cooperative higher dimensional interactions via learnable, matrix valued supports, the proposed HMD-0, HMD-1 and HMD-2 approximants are optimized jointly with a downstream classifier via backpropagation. Comprehensive evaluations across three benchmark HS datasets demonstrate that the higher level HMD layers achieve superior classification accuracy compared to classical learnable tensor baselines, including Tucker, Canonical Polyadic, and Tensor Train decompositions. Furthermore, HMD-1 and HMD-2 achieve a generalization capacity and training stability comparable to standard 2D and 3D-CNNs while requiring significantly fewer feature extractor parameters. These results demonstrate that the HMD framework provides a structurally robust substitute for traditional convolution in multidimensional HS image classification, offering high parameter efficiency and stability throughout the optimization process.

## Metadata
- **Published**: 2026-08-17T08:17:46Z
- **Authors**: Süha Tuna, Ülker Başar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16241v1)