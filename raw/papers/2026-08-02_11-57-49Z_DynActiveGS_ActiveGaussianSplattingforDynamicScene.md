---
title: DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction
published: 2026-08-02T11:57:49Z
authors: Hongbo Duan, Pengting Luo, Chengzhi Zhao, Yuanhao Chiang, Fangming Liu, Xueqian Wang
url: http://arxiv.org/abs/2608.01178v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DynActiveGS: Active Gaussian Splatting for Dynamic Scene Reconstruction

## Abstract
We present DynActiveGS, a dynamic-aware active reconstruction framework based on 3D Gaussian Splatting (3DGS) for autonomous exploration in dynamic environments. The framework incrementally reconstructs a 3D Gaussian scene representation while suppressing motion-corrupted observations through online uncertainty prediction and uncertainty-weighted Gaussian optimization. A key component of DynActiveGS is the explicit decomposition of uncertainty into structural uncertainty and motion-induced uncertainty, which enables the system to distinguish under-reconstructed static regions from dynamically unreliable areas. Based on these uncertainty fields, DynActiveGS performs dynamic-aware viewpoint selection and dynamic-constrained path planning to favor informative yet stable observations during exploration. The resulting system forms a unified closed-loop pipeline for robust active reconstruction in dynamic scenes. Extensive experiments on challenging dynamic benchmarks demonstrate consistent improvements over existing active reconstruction baselines in reconstruction accuracy, completeness, rendering quality, and exploration efficiency.

## Metadata
- **Published**: 2026-08-02T11:57:49Z
- **Authors**: Hongbo Duan, Pengting Luo, Chengzhi Zhao, Yuanhao Chiang, Fangming Liu, Xueqian Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01178v1)