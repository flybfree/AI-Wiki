---
title: From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention
published: 2026-09-18T14:03:49Z
authors: Sichang Su, Benjamin Yang, Zhiyun Deng, Boyuan Liang, Yip Fun Yeung, Zelin Wang, Lingfeng Sun
url: http://arxiv.org/abs/2609.21788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention

## Abstract
A pretrained robot foundation policy may execute most of a long-horizon task yet repeatedly fail at a few critical subtasks. Collecting additional full-task demonstrations for supervised fine-tuning (SFT) requires operators to repeat behaviors the policy already performs well. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches struggle to solve long-horizon tasks using only sparse rewards. We present PARTS (Policy Adaptation with RL on Targeted Subtasks), a real-world subtask RL framework that concentrates practice at these bottlenecks while allowing training rollouts to proceed with minimal human intervention. The frozen pretrained policy supplies nominal actions throughout execution, while agent-generated selectors and success verifiers activate residual corrections and provide local outcome rewards. These rewards support learning from successful subtasks even when complete-task successes are scarce. Training combines online RL with success-reweighted retraining, and each retrained residual policy is redeployed to collect further experience. Humans identify bottlenecks during setup and perform physical resets when needed. On bimanual YAM and single-arm Franka tasks, PARTS improves complete-task success from 32% to 61% and from 50% to 95%, respectively, using tens of minutes of real-world RL rollouts per task on average. Compared with existing real-world RL fine-tuning methods, PARTS raises full-task success by more than 25% under the same robot-rollout budget while requiring less human involvement.

## Metadata
- **Published**: 2026-09-18T14:03:49Z
- **Authors**: Sichang Su, Benjamin Yang, Zhiyun Deng, Boyuan Liang, Yip Fun Yeung, Zelin Wang, Lingfeng Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21788v1)