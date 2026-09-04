---
title: LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL
published: 2026-09-03T08:24:56Z
authors: Sijie Wang, Zhiqiang Tan, Xinrui Yang, Shaohuai Shi
url: http://arxiv.org/abs/2609.03528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL

## Abstract
Diffusion reinforcement learning (RL) has recently achieved significant success in post-training image and video generative models. However, most diffusion RL methods, including DanceGRPO and FlowGRPO, recompute selected timesteps with gradient tracking after rollout. Under on-policy training with the same backend for rollout and update, this recomputation is mathematically redundant. Intuitively, the rollout and policy update steps can reuse the same feed-forward backbone to avoid redundant computation, but doing so can incur a large memory overhead during rollout. To address the issue, we present LeanGRPO by restructuring the data-parallel layout and introducing two recompute-free training schedules for trajectory-logprob diffusion RL: (1) LeanGRPO-Retain enables gradient tracking during rollout and directly reuses the resulting computation graphs and saved activations for backward during update, requiring no recomputation; and (2) LeanGRPO-Reweight also enables gradients during rollout, but immediately backpropagates each selected step using a provisional advantage and delays gradient synchronization, then corrects the provisional gradients with the true advantage after the trajectory is completed. These schedules target different model scales and input sizes. Across FlowGRPO/DanceGRPO with FLUX.1-dev and Wan, LeanGRPO achieves up to 1.83x end-to-end speedup while preserving the original optimization objective.

## Metadata
- **Published**: 2026-09-03T08:24:56Z
- **Authors**: Sijie Wang, Zhiqiang Tan, Xinrui Yang, Shaohuai Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03528v1)