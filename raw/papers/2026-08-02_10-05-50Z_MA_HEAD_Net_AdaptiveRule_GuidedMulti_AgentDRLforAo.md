---
title: MA-HEAD-Net: Adaptive Rule-Guided Multi-Agent DRL for AoI Minimization in UAV-Assisted Emergency Networks
published: 2026-08-02T10:05:50Z
authors: Yixin Zhang, Zhuohui Yao, Wenchi Cheng, Walid Saad
url: http://arxiv.org/abs/2608.01128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MA-HEAD-Net: Adaptive Rule-Guided Multi-Agent DRL for AoI Minimization in UAV-Assisted Emergency Networks

## Abstract
In post-disaster scenarios, unmanned aerial vehicles (UAVs) are critical for establishing emergency communication networks. For time-critical rescue missions, information freshness is crucial because decisions based on outdated data may lead to ineffective control actions. This paper investigates age of information (AoI) minimization for UAV-assisted emergency communications with heterogeneous emergency services. We model bursty packet arrivals using a Markov-modulated Poisson process and adopt finite blocklength theory to capture the coupling among transmission duration, packet completion, and AoI evolution. To balance delay-tolerant long-packet transmission and urgent short-packet response, we propose a mini-slot-embedded scheduling mechanism with adaptive checkpoint-interval selection. We formulate the joint optimization of UAV trajectory control, user scheduling, and checkpoint-interval selection as a multi-agent decision problem, and develop MA-HEAD-Net, an adaptive rule-guided multi-agent deep reinforcement learning framework. MA-HEAD-Net incorporates communication-domain rule priors into a gated multi-head policy, where adaptive gates regulate the contributions of rule-prior and learned-policy logits for different subtasks. The policy and gating components are jointly optimized under multi-agent proximal policy optimization. Simulation results show that MA-HEAD-Net improves policy-formation efficiency compared with representative multi-agent deep reinforcement learning baselines and achieves lower AoI than both learning-based and heuristic methods in dynamic UAV-assisted emergency communication scenarios.

## Metadata
- **Published**: 2026-08-02T10:05:50Z
- **Authors**: Yixin Zhang, Zhuohui Yao, Wenchi Cheng, Walid Saad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01128v1)