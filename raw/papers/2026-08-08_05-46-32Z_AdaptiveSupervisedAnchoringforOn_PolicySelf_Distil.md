---
title: Adaptive Supervised Anchoring for On-Policy Self-Distillation
published: 2026-08-08T05:46:32Z
authors: Meilin Yang, Zixuan Ding, Jianhao Nie, Weite Zhang, Yuxin Zhang, Zhiming Shao, Li Yu, Zhe Fu
url: http://arxiv.org/abs/2608.07935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Supervised Anchoring for On-Policy Self-Distillation

## Abstract
On-policy self-distillation (OPSD) adapts a language model by distilling guidance from a frozen teacher on trajectories sampled from the student. Its effectiveness, however, depends critically on the quality of those trajectories. We show that when student rollouts drift from target trajectories, conditioning the teacher on off-target prefixes substantially weakens its task-relevant supervision. Controlled prefix-corruption experiments expose this failure mode, which we term rollout-conditioned signal degradation. To address this problem, we propose a unified training framework that separates two complementary supervision pathways. The first retains rollout-conditioned distribution matching, providing guidance on states the student actually visits. The second applies supervised cross-entropy on canonical ground-truth contexts, avoiding the incompatibility of imposing target tokens on erroneous rollout prefixes. Token-level rollout-target alignment is used to adapt the strength of the canonical-context anchor, emphasizing it during cold start and relaxing it as rollout quality improves. Experiments across multiple model scales, two task families, and general-reasoning benchmarks show that the proposed approach improves task acquisition over OPSD while preserving general capabilities, resulting in a more favorable empirical plasticity-stability trade-off. These findings identify context quality as a central bottleneck in on-policy self-distillation and demonstrate the value of separating rollout-conditioned guidance from canonical supervision.

## Metadata
- **Published**: 2026-08-08T05:46:32Z
- **Authors**: Meilin Yang, Zixuan Ding, Jianhao Nie, Weite Zhang, Yuxin Zhang, Zhiming Shao, Li Yu, Zhe Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07935v1)