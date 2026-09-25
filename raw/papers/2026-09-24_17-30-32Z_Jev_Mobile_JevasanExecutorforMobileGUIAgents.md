---
title: Jev-Mobile: Jev as an Executor for Mobile GUI Agents
published: 2026-09-24T17:30:32Z
authors: Linghua Zhang
url: http://arxiv.org/abs/2609.30186v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jev-Mobile: Jev as an Executor for Mobile GUI Agents

## Abstract
Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interaction step, leading to substantial latency and model-serving cost. We introduce Jev-Mobile, which shifts this paradigm to low-frequency VLM planning and high-frequency lightweight execution: the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev, a fast typed decision model, repeatedly selects actions within this space. This design allows multiple GUI actions to be executed under a single VLM decision, reducing expensive VLM inference while preserving adaptive interaction. On the full AndroidWorld task suite, Jev-Mobile achieves 79% task success, compared with 78% for SeeAct-V and 84% for a Step-wise VLM baseline. Among successful trajectories, it reduces mean end-to-end execution time by 32.7% and mean model API cost by 73.4% relative to Step-wise VLM. These results show that decoupling high-level VLM reasoning from low-level action execution can substantially improve mobile GUI agent efficiency while maintaining competitive task performance.

## Metadata
- **Published**: 2026-09-24T17:30:32Z
- **Authors**: Linghua Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30186v1)