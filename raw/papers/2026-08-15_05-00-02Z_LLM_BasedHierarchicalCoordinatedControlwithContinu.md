---
title: LLM-Based Hierarchical Coordinated Control with Continuation-Aware Policy Learning
published: 2026-08-15T05:00:02Z
authors: Changhong He, Jinda Gao, Xinkuan Liu, Le Zhang, Xizi Luo, Yu Mei
url: http://arxiv.org/abs/2608.15041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Based Hierarchical Coordinated Control with Continuation-Aware Policy Learning

## Abstract
Coordinating multiple interacting units in complex engineering systems is challenging when system interactions are difficult to model, operational information is heterogeneous, and low-level actions must satisfy strict constraints. We propose an LLM-based hierarchical framework in which the LLM coordinates interacting units based on heterogeneous operational context, while task-specific controllers or optimizers generate executable and constraint-aware actions. We further introduce Continuation-Aware GRPO to capture the consequences of coordination decisions over subsequent control intervals. Rather than judging a decision only by its immediate outcome, the method also evaluates how the system evolves afterward under the current policy. We validate the framework on multi-ramp traffic control and virtual power plant (VPP) energy management, using simplified system models for training and more realistic simulators for evaluation. Across both tasks, the proposed method consistently outperforms direct task-specific control and optimization, end-to-end reinforcement learning, rule-based and RL-based hierarchical coordination, and prompting-only LLM coordinators, demonstrating the value of heterogeneous-context reasoning, hierarchical execution, and continuation-aware policy learning.

## Metadata
- **Published**: 2026-08-15T05:00:02Z
- **Authors**: Changhong He, Jinda Gao, Xinkuan Liu, Le Zhang, Xizi Luo, Yu Mei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15041v1)