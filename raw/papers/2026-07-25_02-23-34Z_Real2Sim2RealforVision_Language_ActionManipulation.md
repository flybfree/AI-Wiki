---
title: Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline
published: 2026-07-25T02:23:34Z
authors: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng
url: http://arxiv.org/abs/2607.22997v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline

## Abstract
Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI ... this is where AI enters the real world,' CES 2026). This paper presents an end-to-end, fully AMD-accelerated technology stack for embodied manipulation, spanning data-center training silicon, Radeon PRO simulation/rendering GPUs, and Ryzen AI edge compute, unified by the open ROCm software stack. We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem. Four progressive demonstrations are presented: (1) a Sim-to-Real manipulation pipeline trained with SmolVLA and deployed on a physical Franka arm; (2) a semantic, language-grounded object-selection task (`one-of-three'); (3) a Real2Sim synthetic-data generation pipeline that fuses 3D Gaussian Splatting (3DGS) reconstructions of real scenes with the Genesis physics engine; and (4) large-scale reinforcement learning for quadruped and humanoid locomotion benchmarked across multiple hardware platforms. All pipelines run natively on ROCm + PyTorch on RDNA4 (Radeon AI PRO R9700) and RDNA3.5 (Radeon PRO W7900) hardware and are reproducible on the free Radeon Cloud Platform.

## Metadata
- **Published**: 2026-07-25T02:23:34Z
- **Authors**: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22997v1)