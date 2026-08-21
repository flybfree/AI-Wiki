---
title: ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control
published: 2026-08-20T08:58:28Z
authors: Xu Yang, Kailai Sun, Dianyu Zhong, Qianchuan Zhao
url: http://arxiv.org/abs/2608.19804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control

## Abstract
Buildings account for roughly one-third of global energy consumption and CO$_2$ emissions. Optimizing indoor climate systems plays a critical role for urban climate mitigation aligned with UN Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors, especially for out-of-distribution environments. In practice, these challenges are further exacerbated by the high cost and privacy burden of dense indoor sensing, forcing operators to collect only limited data in a single operating regime while expecting controllers to generalize reliably across unseen seasons and climate regions. To address this problem, we propose ADAPT, a physics-aware conditional diffusion indoor environmental world model for HVAC control. The model predicts a short-horizon held-action thermal baseline to capture the latent thermal inertia of the buildings. The diffusion backbone utilizes the robustness of generative models, while a learnable multi-zone heat-balance regularizer constrains generated trajectories to satisfy transferable building thermodynamics without requiring known building geometry or manually calibrated thermal parameters. A credit assignment is then design for the downstream reinforcement learning. Extensive experiments on SemibuildingSim and Sinergym demonstrate that ADAPT reduces HVAC energy consumption by 7.3\% and occupant discomfort by 30.2\% compared with state-of-the-art baselines under IID control. Under OOD control scenarios spanning unseen seasons and climate regions, ADAPT maintains robust performance with only marginal degradation relative to its IID performance, substantially outperforming existing methods in transfer robustness.

## Metadata
- **Published**: 2026-08-20T08:58:28Z
- **Authors**: Xu Yang, Kailai Sun, Dianyu Zhong, Qianchuan Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19804v1)