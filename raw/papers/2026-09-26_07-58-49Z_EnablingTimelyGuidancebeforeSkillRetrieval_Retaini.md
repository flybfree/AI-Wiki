---
title: Enabling Timely Guidance before Skill Retrieval: Retaining Helpful Warm Tips in Agent Context
published: 2026-09-26T07:58:49Z
authors: Feng Liang, Yupeng Li, Runhao Zeng, Francis C. M. Lau, Xiping Hu
url: http://arxiv.org/abs/2609.32339v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enabling Timely Guidance before Skill Retrieval: Retaining Helpful Warm Tips in Agent Context

## Abstract
Reusable skills help LLM-based agents solve complex tasks, but the agent must receive guidance before it commits to an ineffective approach. Existing skill mechanisms often expose only metadata and load full content on demand, leaving useful guidance unavailable until the agent decides to retrieve it. General memory methods can incur substantial maintenance overhead, while keeping guidance in conversation context risks repeatedly exposing the agent to irrelevant or harmful advice. We propose TipsWarm, a mechanism that complements existing skill mechanisms by maintaining a budgeted pool of skill-derived keypoints, or \textit{warm tips}, for selective injection into the context of every message turn. By separating event-triggered LLM assessment from inexpensive per-turn screening, it makes transferable skill guidance readily available while controlling maintenance costs. In three coding and iterative task-execution benchmarks, TipsWarm achieves the highest task success rate while remaining time-efficient, compared to recent skill and general memory baselines.

## Metadata
- **Published**: 2026-09-26T07:58:49Z
- **Authors**: Feng Liang, Yupeng Li, Runhao Zeng, Francis C. M. Lau, Xiping Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32339v1)