---
title: CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting
published: 2026-07-28T10:56:52Z
authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
url: http://arxiv.org/abs/2607.25569v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORF-GS: Real-Time Wireless Radiance Field Reconstruction via Coupled Optical-RF Gaussian Splatting

## Abstract
Recent advances in 3D Gaussian Splatting (3DGS)-based wireless radiance field (WRF) reconstruction provide an efficient solution for wireless channel modeling. However, existing WRF reconstruction methods rely on pre-collected observations and offline optimization, and thus struggle to provide real-time channel knowledge. To bridge this gap, we propose CORF-GS, a real-time WRF reconstruction framework that processes sequential optical and radio frequency (RF) keyframes. Specifically, CORF-GS constructs a unified Gaussian representation for optical and RF with shared geometry and modality-specific appearance, allowing high-resolution optical images to provide structural priors for WRF reconstruction. When a new keyframe arrives, CORF-GS first employs optical-guided Gaussian sampling to densify the WRF in under-represented regions. Since light and radio waves may respond differently to the same object surfaces due to wavelength mismatch, relying solely on optical guidance may neglect RF-informative areas. Therefore, CORF-GS performs coupled optical-RF optimization to jointly refine the shared Gaussians. Compared with the existing two-stage training pipelines, this prevents WRF from passively adapting to a frozen optical geometry and encourages the shared Gaussians to adapt to both optical structures and RF power distributions. Simulations show that CORF-GS achieves state-of-the-art RF spectrum synthesis quality and reduces the reconstruction time by $6.4\times$ compared with existing WRF methods.

## Metadata
- **Published**: 2026-07-28T10:56:52Z
- **Authors**: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25569v1)