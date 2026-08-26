---
title: Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments
published: 2026-08-25T05:57:25Z
authors: Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, Lin Fu, Hong Zhou
url: http://arxiv.org/abs/2608.24099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments

## Abstract
GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories. We propose a taxonomy organizing real-world anomalies into four layers (State, Thinking, Action and Round) with ten fine-grained subcategories, and develop a construction pipeline that preserves task solvability while introducing realistic adversarial conditions. Evaluating 16 leading GUI models, we reveal universal vulnerability to dynamic anomalies, with even the strongest models suffering significant performance degradation. Furthermore, we conduct GRPO training in both original and adversarial environments to validate our benchmark, separating environment-learnable anomalies from reasoning-bottlenecked ones. Our findings show that while single-step traps at state and action layers are largely addressable through adversarial reinforcement learning, deep contextual traps, like state deadlock, expose intrinsic limitations that cannot be resolved by training in environments with traps alone.

## Metadata
- **Published**: 2026-08-25T05:57:25Z
- **Authors**: Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, Lin Fu, Hong Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24099v1)