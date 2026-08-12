---
title: IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning
published: 2026-08-11T08:20:02Z
authors: Zefeng Liang, Jie Qiao, Ruichu Cai, Weilin Chen, Zhifeng Hao
url: http://arxiv.org/abs/2608.10634v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning

## Abstract
Model-based reinforcement learning (MBRL), which learns environment dynamics to generate synthetic experience, is a promising approach to sample-efficient decision making. Numerous methods have been developed to improve dynamics prediction and policy optimization for MBRL through uncertainty estimation, model regularization, and conservative value learning. However, these methods typically treat the transition model and critic as monolithic predictors, overlooking the policy-induced data bias. Consequently, action can become entangled with environmental evolution, while uneven action coverage may distort the counterfactual value estimates used for policy improvement. To address this, we propose IADD-TR, a unified framework combining Intervention-Aware Dynamics Decoupling (IADD) and Targeted Regularization (TR). IADD factorizes transitions into an action-intervention stage and an action-free natural evolution stage, using a zero-action anchor to resolve the non-uniqueness of this two-stage factorization for robust generalization. Its latent and state-aligned components are identifiable up to an invertible within-block transformation and pointwise, respectively. For policy learning, we derive TR from the efficient influence function of a replay-state policy-gradient functional. TR augments the critic with an action-density-scaled residual correction and optimizes a targeted loss, yielding doubly robust policy-gradient estimation when either the critic or the replay action density is consistently specified. Extensive experiments on five MuJoCo tasks show that IADD-TR achieves competitive returns with improved sample efficiency.

## Metadata
- **Published**: 2026-08-11T08:20:02Z
- **Authors**: Zefeng Liang, Jie Qiao, Ruichu Cai, Weilin Chen, Zhifeng Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10634v1)