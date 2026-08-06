---
title: Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown Manifolds
published: 2026-08-05T13:28:08Z
authors: Yizhu Wang, Mu Niu, Xiaochen Yang
url: http://arxiv.org/abs/2608.04827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intrinsic-Hybrid Latent Diffusion Models for Generative Modeling on Unknown Manifolds

## Abstract
We introduce the Intrinsic Hybrid Latent Diffusion Model (ILDM), a generative framework that integrates probabilistic dimensionality reduction with geometry-aware diffusion on unknown manifolds. While diffusion models (DMs) have achieved state-of-the-art results in high-dimensional data synthesis, they rely on large training datasets and ignore intrinsic geometric structure. Latent diffusion models (LDMs) address the high dimensionality by learning a latent space, but they typically impose a Euclidean structure, failing to capture the underlying manifold geometry, especially problematic in data-sparse regimes. ILDM addresses these limitations by interpreting the latent space as a chart of an unknown Riemannian manifold, with geometry and uncertainty quantified through a probabilistic decoder. The forward process is a hybrid diffusion that switches between Riemannian and Euclidean dynamics based on local uncertainty, where the Riemannian component is governed by a probabilistic metric tensor derived from the decoder. To learn the generative dynamics, we introduce an approximate denoising score matching method tailored to the hybrid diffusion setting, enabling a backward process defined by hybrid Langevin dynamics. Experiments on COIL-100, MNIST, and cardiac MRI datasets demonstrate that ILDM significantly improves generation quality, achieving lower FID and LPIPS scores compared to standard diffusion and latent diffusion models.

## Metadata
- **Published**: 2026-08-05T13:28:08Z
- **Authors**: Yizhu Wang, Mu Niu, Xiaochen Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04827v1)