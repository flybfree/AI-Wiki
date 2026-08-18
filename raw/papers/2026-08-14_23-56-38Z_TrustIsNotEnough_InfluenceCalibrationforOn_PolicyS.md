---
title: Trust Is Not Enough: Influence Calibration for On-Policy Self-Distillation in Agentic RL
published: 2026-08-14T23:56:38Z
authors: Qizhen Lan, Xi Xiao, Xiangchen Guan, Mengchen Fan, Moule Lin, Jung Im Choi, Lijing Zhu
url: http://arxiv.org/abs/2608.14945v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trust Is Not Enough: Influence Calibration for On-Policy Self-Distillation in Agentic RL

## Abstract
On-policy self-distillation (OPSD) gives language agents dense token-level supervision from a privileged self-teacher on the policy's own trajectories. Existing methods allocate this supervision mainly by teacher trust, but trust does not reveal whether emphasizing a token supports the current policy objective. We call this the trust-utility mismatch and introduce Influence Calibration for Self-Distillation (ICSD). For each supervised token, ICSD measures the first-order response of its importance-weighted RL surrogate contribution to a teacher-directed output perturbation. Batch-adaptive calibration converts this non-stationary signal into a bounded allocation weight while preserving the original auxiliary-loss mass within each action turn. These detached weights affect only the distillation loss and require no additional model pass. Across ALFWorld, WebShop, and Search-QA, ICSD improves all matched aggregate metrics over trust-only allocation under Group Relative Policy Optimization (GRPO) and Group-in-Group Policy Optimization (GiGPO), across two model families spanning 1.5B to 7B. At 7B, it reaches 96.1% ALFWorld success and a WebShop score of 93.1. Frozen-batch analyses show that ICSD reduces teacher-supported mass assigned to objective-opposed tokens from 60.1% to 37.8% and raises cosine compatibility with the RL gradient by 0.192. A companion repository is avail- able at https://github.com/lanqz7766/Influence-Calibration-for-On-Policy-Self-Distillation-in-Agentic-RL.

## Metadata
- **Published**: 2026-08-14T23:56:38Z
- **Authors**: Qizhen Lan, Xi Xiao, Xiangchen Guan, Mengchen Fan, Moule Lin, Jung Im Choi, Lijing Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14945v1)