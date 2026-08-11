---
title: Multi-Agent Reinforcement Learning via Agent-Specific Preference
published: 2026-08-09T09:38:41Z
authors: Ni Mu, Yao Luan, Yiqin Yang, Qing-Shan Jia
url: http://arxiv.org/abs/2608.08604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Reinforcement Learning via Agent-Specific Preference

## Abstract
Multi-agent reinforcement learning (MARL) is a powerful framework for solving complex collaborative tasks, but it relies heavily on well-defined global reward functions. Designing such rewards is challenging, especially in systems with heterogeneous agents, where a single scalar objective may fail to capture diverse behaviors. In this paper, we introduce Multi-AGent Preference-Integrated lEarning (MAGPIE), which addresses these challenges through agent-specific preference modeling. Each agent is evaluated by a dedicated expert through preference signals, eliminating the need for global evaluation. We theoretically prove that optimizing these decentralized preferences converges to a Nash equilibrium policy. To integrate local preferences into a coherent global objective, we construct agent-specific reward models from preference data and combine them via a monotonic aggregation mechanism. We further prove that optimizing this aggregate reward model is equivalent to training the Nash equilibrium policy. Extensive experiments on benchmark multi-agent tasks and a sequential production line task show that MAGPIE achieves performance comparable to reward-engineered baselines, demonstrating its potential to facilitate policy learning in scenarios where precise reward engineering is impractical.

## Metadata
- **Published**: 2026-08-09T09:38:41Z
- **Authors**: Ni Mu, Yao Luan, Yiqin Yang, Qing-Shan Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08604v1)