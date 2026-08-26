---
title: RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards
published: 2026-08-25T09:01:33Z
authors: Houcheng Jiang, Boxuan Zhang, Qiyong Zhong, Junfeng Fang, Xiang Wang, Xiangnan He
url: http://arxiv.org/abs/2608.24275v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards

## Abstract
Safeguarding language model agents requires assessing complete execution trajectories under context-dependent safety policies. Existing policy-aware safeguards mainly rely on prompting or supervised fine-tuning, limiting their ability to adapt to unseen trajectories and changing policy contexts. We propose RePolicy, an agent safeguard that learns safety-policy invocation through reinforcement learning. Given an agent trajectory and a dynamic policy library, RePolicy invokes the applicable policy and uses its content to produce a policy-grounded rationale and safety judgment. We construct PolicyTraj-20K to support supervised initialization, followed by GRPO with verifiable rewards and policy-context perturbation. Experiments across six agent safety benchmarks show that RePolicy achieves strong overall safety-detection performance and robust policy invocation under varying policy contexts.

## Metadata
- **Published**: 2026-08-25T09:01:33Z
- **Authors**: Houcheng Jiang, Boxuan Zhang, Qiyong Zhong, Junfeng Fang, Xiang Wang, Xiangnan He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24275v1)