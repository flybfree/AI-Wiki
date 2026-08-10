---
title: MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents
published: 2026-08-07T03:13:43Z
authors: Zhisheng Chen, Bingfan Zeng, Bangde Cao, Zhengwei Xie, Yuxuan Li, Jinhan Li, Zheng Lu, Xiangchen Guan, Zikai Xiao, Rui Qian, Jingwei Song
url: http://arxiv.org/abs/2608.06745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents

## Abstract
Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation. This leads to representation mismatch, where relevant information is available but not organized for the current decision. To this end, we propose MemPrism, a task-conditioned relational memory framework that separates persistent experience storage from decision-time working memory. MemPrism records interactions as the event stream and dynamically constructs relational views according to the current task context. A lightweight view policy selects the relation structure, evidence range, outcome condition, and granularity, while a deterministic composer and render transform historical facts into a temporary optical working-memory view for a frozen task policy. Experiments on long-horizon embodied and web-agent benchmarks show that MemPrism consistently improves the task performance, especially as trajectories become longer, while reducing memory token consumption. Furthermore, the learned view policy transfers across different VLMs without additional adaptation, demonstrating the effectiveness of task-conditioned relational views as a general memory interface for agents.

## Metadata
- **Published**: 2026-08-07T03:13:43Z
- **Authors**: Zhisheng Chen, Bingfan Zeng, Bangde Cao, Zhengwei Xie, Yuxuan Li, Jinhan Li, Zheng Lu, Xiangchen Guan, Zikai Xiao, Rui Qian, Jingwei Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06745v1)