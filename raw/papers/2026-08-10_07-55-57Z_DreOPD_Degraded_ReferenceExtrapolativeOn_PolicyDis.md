---
title: DreOPD: Degraded-Reference Extrapolative On-Policy Distillation for Flow-matching Models
published: 2026-08-10T07:55:57Z
authors: Mingfeng Lin, Chengfei Cai, Lin Xu, Yuxiang Wei, Liang Han
url: http://arxiv.org/abs/2608.09233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DreOPD: Degraded-Reference Extrapolative On-Policy Distillation for Flow-matching Models

## Abstract
Flow-matching models are now a mainstream method to image generation, but its adaptation to diverse downstream scenarios typically relies on post-training, which may cause conflicts among task-specific optimization objectives. Reinforcement learning enables direct optimization of task-specific rewards beyond the original models, yet trajectory-level optimization may incur high-variance gradients and cross-task interference. On-policy distillation (OPD) offers dense and stable supervision on student rollouts, but conventional teacher matching remains imitation-based. We propose DreOPD, a Degraded-reference extrapolative OPD method for flow-matching models that bridges these two paradigms. Our DreOPD converts implicit reward extrapolation into closed-form velocity regression, enabling extrapolative post-training with the stability of OPD. It further uses a mildly degraded reference to strengthen the teacher-reference contrast, yielding a clearer extrapolation direction. Experiments on single- and multi-teacher settings show that DreOPD outperforms OPD and multi-task RL baselines in average performance, while surpassing specialized teachers on most metrics.

## Metadata
- **Published**: 2026-08-10T07:55:57Z
- **Authors**: Mingfeng Lin, Chengfei Cai, Lin Xu, Yuxiang Wei, Liang Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09233v1)