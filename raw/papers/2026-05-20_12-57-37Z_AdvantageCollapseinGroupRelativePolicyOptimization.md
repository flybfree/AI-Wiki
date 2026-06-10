---
title: 'Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation'
published: 2026-05-20T12:57:37Z
authors: Xixiang He, Qiyao Sun, Ao Cheng, Xingming Li, Xuanyu Ji, Hailun Lu, Runke Huang, Qingyong Hu
url: http://arxiv.org/abs/2605.21125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation

## Abstract
Group Relative Policy Optimization (GRPO), a prominent algorithm within the Reinforcement Learning from Verifiable Rewards (RLVR) framework, has achieved strong results in improving the reasoning capabilities of large language models (LLMs). However, GRPO is prone to advantage collapse, a failure mode where homogeneous rewards within a group (e.g., all correct or all incorrect answers) yield near-zero advantages and vanishing gradients. To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients. Across models from 0.5B to 14B parameters on mathematical reasoning benchmarks, we show that ACR strongly predicts training stagnation and final performance. We then propose Adaptive Virtual Sample Policy Optimization (AVSPO), a lightweight extension of GRPO that injects virtual reward samples, guided by real-time ACR monitoring, to enable learning from homogeneous groups without additional model rollouts. AVSPO reduces advantage collapse by 58-63% relative to GRPO and yields consistent accuracy gains of 4-6 percentage points across all model scales, while maintaining generalization on the evaluated out-of-domain task. Code and datasets are available at https://qingyonghu.github.io/AVSPO.

## Metadata
- **Published**: 2026-05-20T12:57:37Z
- **Authors**: Xixiang He, Qiyao Sun, Ao Cheng, Xingming Li, Xuanyu Ji, Hailun Lu, Runke Huang, Qingyong Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.21125v1)