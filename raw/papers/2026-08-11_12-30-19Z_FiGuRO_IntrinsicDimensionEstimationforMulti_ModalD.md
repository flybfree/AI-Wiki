---
title: FiGuRO: Intrinsic Dimension Estimation for Multi-Modal Data
published: 2026-08-11T12:30:19Z
authors: Viktoria Schuster, Sana Tonekaboni, Caroline Uhler
url: http://arxiv.org/abs/2608.10857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FiGuRO: Intrinsic Dimension Estimation for Multi-Modal Data

## Abstract
Determining the complexity, or Intrinsic Dimension (ID), of data is fundamental to efficient and interpretable representation learning. This is particularly challenging in multi-modal settings when trying to learn disentangled representations for shared and private information. Existing techniques leave a critical gap: they are often static, uni-modal, or in the case of contrastive methods, adapt only to the shared ID implicitly. We introduce Fidelity-Guided Rank Optimization (FiGuRO), a framework for approximating the ID of uni- and multi-modal data under constraints of model capacity and hyperparameters. FiGuRO learns the dimensions of low-rank projections using truncated singular value decomposition and an algorithm that determines when to reduce or increase dimension and in which latent space. Disentanglement of shared and private information arises as an emergent property of this optimization, eliminating the need for complex auxiliary loss functions. We demonstrate that FiGuRO outperforms existing ID estimation techniques and is more robust to hyperparameter changes. Across simulations and real-world data, FiGuRO captures distinct ID scales and varying subspace ratios, and decomposes shared and private information successfully. Furthermore, we show that FiGuRO can be applied to modern uni-modal pretrained models, enabling efficient, post-hoc disentanglement of multi-modal representations.

## Metadata
- **Published**: 2026-08-11T12:30:19Z
- **Authors**: Viktoria Schuster, Sana Tonekaboni, Caroline Uhler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10857v1)