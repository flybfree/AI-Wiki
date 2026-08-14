---
title: Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach
published: 2026-08-12T14:15:35Z
authors: Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, Zhenyu Wang
url: http://arxiv.org/abs/2608.12436v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach

## Abstract
Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized coordination through centralized training, existing methods suffer from high-dimensional joint state-action modeling, noise-sensitive policy generation, leading to unstable training and degraded tracking. To address these issues, we propose VGG-MADiffRL, a value-gradient-guided multi-agent diffusion RL algorithm, and MDCA, a diffusion?based hierarchical control architecture. Leveraging underwater mission characteristics, we model sonar detection mechanisms and ocean current disturbances, formulating cooperative tracking for multi-AUV ad-hoc networks as an MDP. The proposed MDCA constitutes a three-tier closed-loop control framework: a global intelligent control layer, a local online training layer, and a physical action execution layer. This structure enables synergistic optimization across task allocation, local decision processes, and execution feedback. Within MDCA, the local online training layer is the policy learning framework; VGG-MADiffRL builds on diffusion policies and incorporates value gradients to guide action generation in the reverse denoising process, steering the generated actions towards higher expected returns. It employs twin value networks with joint optimization and soft target updates to mitigate overestimation and training oscillations, promoting more stable convergence. Experimental results show that VGG-MADiffRL consistently achieves faster convergence, higher tracking accuracy, and smoother training dynamics in cooperative tracking scenarios, validating its effectiveness and practical engineering value in dynamic underwater settings.

## Metadata
- **Published**: 2026-08-12T14:15:35Z
- **Authors**: Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, Zhenyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12436v1)