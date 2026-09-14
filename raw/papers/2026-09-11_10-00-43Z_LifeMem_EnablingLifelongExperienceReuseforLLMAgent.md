---
title: LifeMem: Enabling Lifelong Experience Reuse for LLM Agents
published: 2026-09-11T10:00:43Z
authors: Yuli Qiu, Yutong Li, Wei Su, Zeming Liu, Wanxiang Che, Heyan Huang, Haifeng Wang, Yuang Guo
url: http://arxiv.org/abs/2609.12655v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LifeMem: Enabling Lifelong Experience Reuse for LLM Agents

## Abstract
Large language model agents are expected to continuously adapt to new tasks and environments over their lifetime by reusing past experience. However, existing memory-based agents struggle to transfer reusable experience across environments and suffer from catastrophic forgetting as experience accumulated. To address these challenges, we propose LifeMem, a lifelong learning framework that enables agents to transfer knowledge across multiple environments. During learning, LifeMem clusters accumulated interaction trajectories based on underlying workflows to extract reusable skills. When solving a new task at inference time, the agent recalls relevant skills and trajectories to guide actions. To validate our method, we conduct experiments across 10 environments and over 13k tasks with 2k newly annotated interaction trajectories. Results show that LifeMem enables effective experience reuse in lifelong learning, achieving both reduced forgetting on learned tasks and superior cross-task transfer. Further analysis reveals that task streaming impacts learning, while consolidating structurally similar trajectories within memory boosts performance.

## Metadata
- **Published**: 2026-09-11T10:00:43Z
- **Authors**: Yuli Qiu, Yutong Li, Wei Su, Zeming Liu, Wanxiang Che, Heyan Huang, Haifeng Wang, Yuang Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12655v1)