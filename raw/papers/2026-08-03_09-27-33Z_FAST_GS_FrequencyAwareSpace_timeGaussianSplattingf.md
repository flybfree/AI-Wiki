---
title: FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis
published: 2026-08-03T09:27:33Z
authors: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
url: http://arxiv.org/abs/2608.01958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FAST-GS: Frequency Aware Space-time Gaussian Splatting for Photorealistic Dynamic Novel View Synthesis

## Abstract
4D Gaussian Splatting (4DGS) excels in dynamic 3D reconstruction and real-time novel view synthesis via efficient 4D Gaussian representations and parallelizable rendering. However, existing 4DGS approaches rely on a single polynomial to model motion, which limits performance in complex dynamic scenes where high-frequency motion components are prevalent, and fails to ensure long-term stability due to cumulative trajectory drift. To address these issues, we propose a Fourier Motion Modeling module: this paradigm decomposes motion into frequency-based sinusoidal components, capturing both low-frequency global trajectories and high-frequency local details to model complex motion patterns accurately. It retains the real-time rendering capability of 4DGS while improving complex motion fitting and long-term coherence. Additionally, we integrate a motion-aware regularization strategy into the loss function: it uses frequency-dependent weights to suppress high-frequency jitter while preserving low-frequency motion coherence. Extensive experiments on N3V and Google Immersive datasets from multiple scenarios demonstrate the effectiveness of our method.

## Metadata
- **Published**: 2026-08-03T09:27:33Z
- **Authors**: Zhengyang Zhang, Ziyu Lu, PengCheng Li, Hongbo Duan, Yi Liu, Pengting Luo, Peiyu Zhuang, Xinghui Li, Shaohua Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01958v1)