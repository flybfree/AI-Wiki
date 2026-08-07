---
title: GSBF: Gaussian Splatting for Environment-Aware Beamforming
published: 2026-08-06T11:22:34Z
authors: Yijie Bian, Wei Guo, Zixin Wang, Shenghui Song, Jun Zhang, Khaled B. Letaief
url: http://arxiv.org/abs/2608.05896v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GSBF: Gaussian Splatting for Environment-Aware Beamforming

## Abstract
Beamforming plays a key role in multiple-input-multiple-output (MIMO) communication systems. However, conventional beamforming design normally requires accurate instantaneous channel state information (CSI) and iterative optimization, which incur substantial pilot overhead and computational complexity. Recognizing that radio propagation is intrinsically governed by the physical geometry, we develop a 3D Gaussian splatting for environment-aware beamforming (GSBF) pipeline based on multi-modal data, which characterizes the environment through a persistent 3D Gaussian representation. Specifically, GSBF models the environmental scattering response with reciprocity-preserving bidirectional spherical Gaussian (Bi-SG) kernels and performs two-sided electromagnetic rasterization to render an angular propagator map. The rendered map is then aggregated through an over-complete array-manifold dictionary and projected to the constant-modulus beamformers, thereby synthesizing beams directly from the access point (AP) pose and user position without online instantaneous CSI. Simulations demonstrate that GSBF consistently outperforms baselines such as exhaustive beam alignment (EBA) with lower latency.

## Metadata
- **Published**: 2026-08-06T11:22:34Z
- **Authors**: Yijie Bian, Wei Guo, Zixin Wang, Shenghui Song, Jun Zhang, Khaled B. Letaief
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05896v1)