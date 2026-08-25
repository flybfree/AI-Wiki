---
title: A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design
published: 2026-08-23T06:13:10Z
authors: Yiming Wang, Jiale Zhu, Zhichen Ye, Yandong Lv, Shiqi Wang, Jinlong Liu, Yucheng Fan
url: http://arxiv.org/abs/2608.22235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design

## Abstract
Pore-scale flow governs transport and permeability behaviour in porous media engineering applications, yet repeated lattice Boltzmann method (LBM) simulation across many geometries and design queries remains costly for repeated deployment. This study formulates transient pore-scale flow prediction as a geometry-conditioned query-time operator and introduces QSGS-Transient-7606, a benchmark of 7,606 two-dimensional porous structures each paired with 30 logarithmically sampled LBM states. The proposed continuous-time pore-scale flow surrogate model (CT-PoreFlow) integrates topology-aware geometry encoding, compressed spectral mixing, and log-time conditioning with a late-time flux-calibration objective. On unseen test geometries, CT-PoreFlow achieves a velocity relative L2 of 0.2248 and a terminal permeability error of 12.81%. Frozen morphology and computed tomography image audits confirm reasonable cross-geometry robustness without fine-tuning. The surrogate is then embedded in an inverse design workflow, screening 9,216 generative adversarial network and diffusion candidates across 18 property targets prior to LBM verification. Guided GAN sampling attains 98.11% through-connectivity and 72.28% conditional design success, exceeding diffusion-based generation. The framework unifies transient flow prediction, transport-aware screening, and LBM-verified inverse design for porous media.

## Metadata
- **Published**: 2026-08-23T06:13:10Z
- **Authors**: Yiming Wang, Jiale Zhu, Zhichen Ye, Yandong Lv, Shiqi Wang, Jinlong Liu, Yucheng Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22235v1)