---
title: Consistent Plan-Act for Long-Horizon Agentic Tasks
published: 2026-09-30T03:38:49Z
authors: Heng-Zhuang Li, Yi-Kai Zhang, Yu Wang, Yueqing Sun, Jiayuan Zhang, Qi Gu, Han-Jia Ye
url: http://arxiv.org/abs/2609.38891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Consistent Plan-Act for Long-Horizon Agentic Tasks

## Abstract
Long-horizon agentic tasks demand strong reasoning and efficient execution across successive interactions with dynamic environments. A common approach decouples high-level planning from low-level execution through separate planner and actor roles. To investigate coordination failures in these tasks, we prompt both agents for structured state assertions and compare their reports programmatically to detect explicit contradictions. Our analyses reveal systematic disagreement about the same task-relevant state facts, a phenomenon we term planner-actor state mismatch. We further find that providing agents with task-relevant state information reduces mismatch and improves coordination and task performance. Based on the systematic analysis of the state mismatch, we propose Consistent Plan-Act (ConPAct), which feeds detected contradictions back to both agents to form consistent state interpretations and fine-tunes them on curated consistent interactions for better coordination. ConPAct improves performance across various environments and model configurations, e.g., increasing MiniGrid success rate from 38.6% to 54.4% with GPT-5.6-sol/terra as planner and actor respectively, demonstrating that state consistency can guide both inference-time correction and coordination training.

## Metadata
- **Published**: 2026-09-30T03:38:49Z
- **Authors**: Heng-Zhuang Li, Yi-Kai Zhang, Yu Wang, Yueqing Sun, Jiayuan Zhang, Qi Gu, Han-Jia Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38891v1)