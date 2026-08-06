---
title: Multimodal Alignment Through Joint Kernel Entropic Gromov--Wasserstein Optimal Transport
published: 2026-08-04T21:21:09Z
authors: Yixuan Florence Wu, Yilun Zhu, Naichen Shi
url: http://arxiv.org/abs/2608.04234v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multimodal Alignment Through Joint Kernel Entropic Gromov--Wasserstein Optimal Transport

## Abstract
We study the problem of aligning data from multiple modalities into a shared representation space, focusing on settings where strong pretrained unimodal encoders are available but cross-modal paired data are scarce. We propose a structure-preserving alignment framework, joint kernel entropic Gromov--Wasserstein Optimal Transport (JK-EGW), which maps multiple modalities into a common latent space by minimizing a quadratic optimal transport objective. JK-EGW leverages fine-grained similarity relationships within and across modalities to construct a global affinity kernel instead of relying on raw feature-space distances. Our framework naturally provides explicit control over the geometry and distribution of the latent embedding. On the theory side, we establish parametric sample complexity rate of $n^{-1/2}$, matching the corresponding rates for standard, entropic and Gromov--Wasserstein optimal transport. On the algorithmic side, we derive a scalable alternating procedure to solve JK-EGW with entropic optimal transport (EOT) updates through a low-rank kernel approximation and a variational lifting. This lifting scheme effectively relieves the burden of a quadratic objective, and allowing us to take the advantage of existing EOT solvers. Empirically, we focus on post-hoc alignment of embeddings from pretrained encoders in data-scarce regimes, and show that our proposed method achieves improved multimodal retrieval performance compared to existing alignment baselines.

## Metadata
- **Published**: 2026-08-04T21:21:09Z
- **Authors**: Yixuan Florence Wu, Yilun Zhu, Naichen Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04234v1)