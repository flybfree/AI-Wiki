---
title: ParaAgent: Reinforcing Parallel Acting in Open-World Tool Environments
published: 2026-09-27T14:34:22Z
authors: Shengbin Yue, Hongru Wang, Siyuan Wang, Xiaoxin Chen, Wei Chen, Zhongyu Wei
url: http://arxiv.org/abs/2609.33618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ParaAgent: Reinforcing Parallel Acting in Open-World Tool Environments

## Abstract
Language model agents are increasingly deployed in open-world tool environments, which require balancing exploring unknown capabilities and exploiting known ones. Existing methods face a performance-efficiency tradeoff: they either rigidly decouple exploration and execution or interleave them without coordination. We argue that the key lies not in whether to decouple or interleave them, but in how to coordinate them across granularities. We introduce ParaAct, a structured parallel-action loop that combines phase-level Exploration $\rightleftharpoons$ Execution with action-level parallelism. To learn this loop, ParaAgent combines multi-agent cold-start demonstrations with reinforcement learning under multi-level advantage decoupling, making planning structure explicit and supervising it with step-, phase-, and trajectory-level rewards. Learning is supported by our ToolEnv, a scalable simulator grounded in 50,011 realistic tool interfaces. On two open-world tool benchmarks, ParaAgent-4B achieves the best average success among all baselines, including GPT-4.1 systems, with the largest gains on multi-tool tasks. Behavioral analyses show that these gains stem from this action organization, highlighting its importance for capable and efficient open-world agents.

## Metadata
- **Published**: 2026-09-27T14:34:22Z
- **Authors**: Shengbin Yue, Hongru Wang, Siyuan Wang, Xiaoxin Chen, Wei Chen, Zhongyu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33618v1)