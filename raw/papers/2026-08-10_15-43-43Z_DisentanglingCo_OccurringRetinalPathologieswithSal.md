---
title: Disentangling Co-Occurring Retinal Pathologies with Saliency-Guided Sparse Expert Routing
published: 2026-08-10T15:43:43Z
authors: Nagur Shareef Shaik, Jeongwoo Park, Yeong-Jin Kim, Jaeuk Jung, Hyunjung Oh, Dong Hye Ye
url: http://arxiv.org/abs/2608.09752v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Co-Occurring Retinal Pathologies with Saliency-Guided Sparse Expert Routing

## Abstract
Retinal fundus images frequently exhibit multiple co-occurring pathologies, yet standard deep learning classifiers apply static, identical computation to every image regardless of the underlying disease distribution. We propose a novel architecture that resolves this via sparse conditional computation, pairing a Guided Context Gating (GCG) spatial attention front-end with a sparsely-routed Mixture-of-Experts (MoE) block operating over feature tokens. Crucially, this routing yields an interpretable, data-driven decomposition. Expert allocation is significantly disease-dependent (p < 0.001), with the healthy Normal state and morphologically distinct pathologies (e.g., ERM, AMD) isolating to dedicated experts. On a five-class, patient-disjoint 5-fold cross-validation benchmark, our model achieves 0.912 +/- 0.008 macro AUC and 0.653 +/- 0.014 macro F1. Furthermore, Grad-CAM++ and post-MoE t-SNE visualizations confirm that expert routing aligns with localized lesions and geometrically maps co-occurring cases between their constituent clusters, positioning sparse MoE as an interpretable approach to multi-disease retinal screening.

## Metadata
- **Published**: 2026-08-10T15:43:43Z
- **Authors**: Nagur Shareef Shaik, Jeongwoo Park, Yeong-Jin Kim, Jaeuk Jung, Hyunjung Oh, Dong Hye Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09752v1)