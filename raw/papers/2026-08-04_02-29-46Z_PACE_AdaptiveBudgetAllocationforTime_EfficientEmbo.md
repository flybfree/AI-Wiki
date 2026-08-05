---
title: PACE: Adaptive Budget Allocation for Time-Efficient Embodied Planning
published: 2026-08-04T02:29:46Z
authors: Yuchen Huang, Xijiang Ying, Zhenhua Ma, Xiaxiang Yuan, Zhijie Gao, Jiayi Huang, Ruichi Mao, Jiazheng Zhang, Hongsheng Ti, Maotao Tian, Rong Shi, Lu Zhao, Shizhuang Zhang, Zhuo Cui, He Wang, Ling Liu, Wei Zhang
url: http://arxiv.org/abs/2608.03034v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PACE: Adaptive Budget Allocation for Time-Efficient Embodied Planning

## Abstract
Reasoning-enhanced large language models have achieved remarkable improvements in planning tasks, yet their deployment in embodied systems remains impractical due to prohibitive inference delays-often exceeding minutes per planning instance. The fundamental bottleneck stems from the serial nature of existing paradigms: models must complete all reasoning before any action execution, leaving execution time windows entirely unexploited. We introduce PACE (Planning with Adaptive Cognitive Effort), a framework that enables interleaved reasoning and execution through two key innovations: an Interleaved Think-Act architecture that pipelines cognitive processing with action execution, and a Dynamic Budget Allocator that adapts reasoning token budgets to available execution time windows. On the Robotouille benchmark using Qwen3-8B-AWQ, PACE achieves a 10% success rate-representing a 67% improvement over the ReAct+Think baseline-while delivering 6.9 times acceleration in thinking time compared to unconstrained reasoning. The framework hides 66.8% of thinking time within execution windows, demonstrating that strategic cognitive effort allocation can simultaneously improve both planning quality and time efficiency. These results provide evidence that time-aware architectural innovations enable reasoning models to operate in latency-sensitive embodied domains where they were previously impractical.

## Metadata
- **Published**: 2026-08-04T02:29:46Z
- **Authors**: Yuchen Huang, Xijiang Ying, Zhenhua Ma, Xiaxiang Yuan, Zhijie Gao, Jiayi Huang, Ruichi Mao, Jiazheng Zhang, Hongsheng Ti, Maotao Tian, Rong Shi, Lu Zhao, Shizhuang Zhang, Zhuo Cui, He Wang, Ling Liu, Wei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03034v1)