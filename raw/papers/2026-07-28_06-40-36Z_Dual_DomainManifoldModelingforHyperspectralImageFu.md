---
title: Dual-Domain Manifold Modeling for Hyperspectral Image Fusion
published: 2026-07-28T06:40:36Z
authors: Chengxin Xie, Qiya Song, Yangbangyan Jiang, Renwei Dian, Xudong Kang
url: http://arxiv.org/abs/2607.25338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual-Domain Manifold Modeling for Hyperspectral Image Fusion

## Abstract
Achieving a coherent integration of spectral richness and spatial fidelity remains a central objective in hyperspectral image fusion. However, existing hyperspectral image fusion methods struggle to effectively model geometric constraints. In the spatial domain, weak spatial-spectral interaction limits geometry-aware feature learning and suppresses high-frequency structural information, resulting in low-frequency bias and structural degradation. In the spectral domain, local manifold structures induced by spectral similarity are insufficiently exploited, limiting intrinsic pixel relationship modeling and fine-grained spectral reconstruction. To address these challenges, we propose a dual-domain manifold modeling (DDMM) framework. Specifically, we introduce a Topology-Aware Transformer (TPFormer) that combines global attention with neighborhood propagation, jointly modeling spatial topology and pixel-level feature manifold relationships to capture intrinsic spatial-spectral structures and improve topology-aware representation learning. Furthermore, a Frequency-Decoupled Spatial-Spectral Collaborative Fusion (FDSCF) module is devised, in which features are projected into the frequency domain via the discrete cosine transform and explicitly decoupled into low- and high-frequency components. Guided by a low-rank structural prior and spectral-driven spatial enhancement, FDSCF selectively enhances geometry-aware high-frequency features, strengthening spatia-spectral coupling and recovering sharper edges and finer textures. Extensive experiments on multiple benchmark datasets demonstrate that DDMM achieves superior overall performance over SoTA methods in terms of spatial structure preservation and spectral reconstruction.

## Metadata
- **Published**: 2026-07-28T06:40:36Z
- **Authors**: Chengxin Xie, Qiya Song, Yangbangyan Jiang, Renwei Dian, Xudong Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25338v1)