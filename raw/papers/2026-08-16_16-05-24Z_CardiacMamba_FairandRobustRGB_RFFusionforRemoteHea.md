---
title: CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling
published: 2026-08-16T16:05:24Z
authors: Bo Zhao, Zheng Wu, Yiping Xie, Zitong YU
url: http://arxiv.org/abs/2608.15831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling

## Abstract
Remote photoplethysmography (rPPG) enables non-contact heart rate (HR) monitoring from facial videos, but RGB-only methods are vulnerable to illumination changes, motion artifacts, and skin-tone-dependent optical reflectance. We propose CardiacMamba, a fair and robust RGB-RF fusion framework that integrates optical facial cues and radio-frequency cardiac motion cues through state space modeling. CardiacMamba introduces a Temporal Difference Mamba Module (TDMM) to enhance subtle RF temporal variations, a bidirectional SSM-based interaction mechanism to align heterogeneous RGB-RF dynamics, and a Channel-wise Fast Fourier Transform (CFFT) module for channel-domain spectral refinement. On the EquiPleth dataset, CardiacMamba achieves state-of-the-art performance with 0.96 bpm MAE, 3.06 bpm RMSE, and 0.97 Pearson correlation, while reducing the observed light-dark skin-tone MAE gap to 0.26 bpm and maintaining robustness under RGB degradation and RF-missing conditions

## Metadata
- **Published**: 2026-08-16T16:05:24Z
- **Authors**: Bo Zhao, Zheng Wu, Yiping Xie, Zitong YU
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15831v1)