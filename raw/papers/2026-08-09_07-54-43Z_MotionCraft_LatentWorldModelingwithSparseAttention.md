---
title: MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling
published: 2026-08-09T07:54:43Z
authors: Rong Fu, Chunlei Meng, Yangchen Zeng, Xiaowen Ma, Yongtai Liu, Wangyu Wu, Shuo Yin, Zijian Zhang, Sicheng Li, Yingrui Ji, Chenhao Wang, Simon Fong
url: http://arxiv.org/abs/2608.08553v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling

## Abstract
Video super-resolution (VSR) aims to recover high-fidelity high-resolution videos from low-resolution inputs and is central to applications ranging from mobile capture to streaming and archival restoration. Existing approaches trade off among local-detail fidelity, long-range spatio-temporal modeling, perceptual realism, and efficiency: convolutional alignment techniques preserve local structure but suffer when motion is large or degradations are complex; transformer-based methods capture long-range dependencies yet require architectural or algorithmic adaptations to remain computationally feasible; and recent latent or diffusion-based generators synthesize rich texture but require specialized temporal constraints to maintain coherence. We present MotionCraft, a controllable VSR framework that formulates restoration as motion-aware latent state prediction inspired by world models and integrates adaptive sparse attention with an explicit user-accessible control interface. MotionCraft combines robust motion fusion, a Latent World Transformer that balances locality and targeted non-local interactions, and a compact conditional decoder to deliver temporally consistent, high-quality reconstructions under streaming constraints. Empirical evaluations show that MotionCraft achieves strong reconstruction and perceptual performance while enabling predictable trade-offs between temporal smoothness and reconstruction fidelity.

## Metadata
- **Published**: 2026-08-09T07:54:43Z
- **Authors**: Rong Fu, Chunlei Meng, Yangchen Zeng, Xiaowen Ma, Yongtai Liu, Wangyu Wu, Shuo Yin, Zijian Zhang, Sicheng Li, Yingrui Ji, Chenhao Wang, Simon Fong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08553v1)