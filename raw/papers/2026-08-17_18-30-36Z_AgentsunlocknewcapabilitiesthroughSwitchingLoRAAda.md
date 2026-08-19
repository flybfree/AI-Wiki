---
title: Agents unlock new capabilities through Switching LoRA Adapters as a Tool (SLAaaT)
published: 2026-08-17T18:30:36Z
authors: Kenneth Ge
url: http://arxiv.org/abs/2608.17034v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agents unlock new capabilities through Switching LoRA Adapters as a Tool (SLAaaT)

## Abstract
Post-training can unlock new capabilities and improve performance on specialized tasks, but sometimes at the cost of catastrophic forgetting in other domains. This poses a problem in long agent trajectories that compose different capabilities. We reject this tradeoff by giving an agent a tool to switch between specialized LoRA adapters mid-trace. To test its effectiveness, we compose two synthetic coding tasks that are logically simple but require specialization. We find that this allows the model to solve problems it previously could not, that the model is able to switch autonomously (and find a new strategy that beats our human heuristic baseline on one task), and that this incurs an up to an 18x reduction in capability tax compared to an agent using only one specialized adapter. Our approach also substantially outperforms spawning subagents in both task capabilities and token usage.

## Metadata
- **Published**: 2026-08-17T18:30:36Z
- **Authors**: Kenneth Ge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17034v1)