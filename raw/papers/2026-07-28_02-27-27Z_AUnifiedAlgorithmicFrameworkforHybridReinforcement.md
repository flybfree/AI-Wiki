---
title: A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics
published: 2026-07-28T02:27:27Z
authors: Zheshun Wu, Renjie Zheng, Jinhang Zuo, Zenglin Xu, Fang Kong
url: http://arxiv.org/abs/2607.25207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics

## Abstract
This paper investigates a hybrid reinforcement learning setting in tabular Markov Decision Processes (MDPs), where an agent aims to learn an optimal policy by combining online interactions with a target environment and offline data from a source environment. A central challenge is that offline data may be collected from outdated environments with shifted transition dynamics, making naive integration of historical data ineffective. To address this, we propose a unified algorithmic framework featuring two algorithms: MIN-UCB-VI for regret minimization and MAX-LCB-VI for best policy identification. Both algorithms leverage fine-grained bias information to more effectively exploit offline data under general transition shifts. We provide theoretical guarantees for our framework, including both instance-dependent and independent upper bounds on regret and sub-optimality gap. Furthermore, we establish matching lower bounds to demonstrate the optimality of our approach and validate our theoretical findings through extensive experiments.

## Metadata
- **Published**: 2026-07-28T02:27:27Z
- **Authors**: Zheshun Wu, Renjie Zheng, Jinhang Zuo, Zenglin Xu, Fang Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25207v1)