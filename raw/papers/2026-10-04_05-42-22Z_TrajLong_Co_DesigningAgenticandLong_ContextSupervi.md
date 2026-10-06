---
title: TrajLong: Co-Designing Agentic and Long-Context Supervision for Mid-Training
published: 2026-10-04T05:42:22Z
authors: Miao Peng, Qintong Zhang, Nuo Chen, Yuhan Li, Guochen Yan, Xinran Gu, Hongqiu Wu, Hai Wang, Lydell Huang, Wentao Zhang, Jia Li
url: http://arxiv.org/abs/2610.04973v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrajLong: Co-Designing Agentic and Long-Context Supervision for Mid-Training

## Abstract
LLM agents for coding, search, and workplace tasks increasingly rely on long-context capabilities to effectively aggregate and reason over extended interaction histories. Recent work has incorporated agent trajectories into mid-training stage, drawing on their naturally long and interaction-rich structure. Yet how to organize the information within these trajectories into effective mid-training supervision remains underexplored. In this work, we investigate the relationship between long-context and agent atomic capabilities and introduce TrajLong, a novel framework that compiles trajectories into long-context training tasks with dense supervision, targeting three representative atomic capabilities: evidence grounding, cross-evidence aggregation, and temporal state maintenance. We mid-train Qwen3-14B-Base and Qwen3-30B-A3B-Base with data compiled by TrajLong, followed by supervised fine-tuning. Experiments on 6 long-context and 12 agent benchmarks demonstrate broad performance gains, with controlled ablations showing improvements over raw and masked trajectory baselines. Capability-level analyses further reveal task-dependent associations between long-context and agent atomic capabilities. These findings suggest that the shared capability demands of long-context reasoning and agent execution provide a principled basis for designing mid-training data to develop downstream agent capabilities.

## Metadata
- **Published**: 2026-10-04T05:42:22Z
- **Authors**: Miao Peng, Qintong Zhang, Nuo Chen, Yuhan Li, Guochen Yan, Xinran Gu, Hongqiu Wu, Hai Wang, Lydell Huang, Wentao Zhang, Jia Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04973v1)