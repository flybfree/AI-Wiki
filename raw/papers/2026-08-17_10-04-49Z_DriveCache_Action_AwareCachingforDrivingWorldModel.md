---
title: DriveCache: Action-Aware Caching for Driving World Model Inference
published: 2026-08-17T10:04:49Z
authors: Jianchun Yang, Jian Liang, Xianda Guo, Pinhan Fu, Yanlun Peng, Conglang Zhang, Wenke Huang, Mang Ye
url: http://arxiv.org/abs/2608.16354v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DriveCache: Action-Aware Caching for Driving World Model Inference

## Abstract
Driving video generation models support autonomous-driving development by predicting controllable future scenes for simulation, planning evaluation, and offline data generation. Diffusion-based driving generators repeatedly evaluate large backbones across denoising steps, which limits generation throughput. Existing diffusion acceleration methods reduce this cost, but general-purpose designs omit driving signals available before generation, such as ego speed and planned trajectories. Experiments across driving motions show that cache tolerance varies with ego translation and rotation, denoising progress, and consecutive reuse length. We propose DriveCache, a training-free, action-aware controller that uses planned motion to allocate reuse across scenes and dynamic programming to place it across denoising steps under a calibrated response budget. A causal drift check refreshes features and replans the remaining schedule when generation departs from calibration. Across three generator configurations, DriveCache improves the overall fidelity-efficiency trade-off over evaluated cache methods. Our code will be publicly available.

## Metadata
- **Published**: 2026-08-17T10:04:49Z
- **Authors**: Jianchun Yang, Jian Liang, Xianda Guo, Pinhan Fu, Yanlun Peng, Conglang Zhang, Wenke Huang, Mang Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16354v1)