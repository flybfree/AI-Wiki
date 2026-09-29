---
title: ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents
published: 2026-09-27T05:30:01Z
authors: Song-Li Wu, Jingyi Wang, Zhaocheng Du, Weinan Gan
url: http://arxiv.org/abs/2609.33244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ActiveMem: Dynamic Latent Memory Trees for Long-Horizon Agents

## Abstract
Large Language Model (LLM) agents increasingly rely on external memory to support long-horizon reasoning and decision making. Existing memory systems typically retrieve historical trajectories or summaries as independent context fragments, overlooking the procedural dependencies underlying multi-step execution. As memory scales, such flat retrieval introduces context fragmentation and cross-task interference, leading to structurally inconsistent reasoning trajectories. We propose ActiveMem, a hierarchical memory framework that recursively organizes agent experiences into dependency-aware latent execution trees. ActiveMem abstracts trajectories into reusable subtask nodes while explicitly preserving execution transitions, enabling coherent reasoning-path retrieval conditioned on the current execution state. To support continual adaptation, ActiveMem further learns dynamic memory expansion, retrieval, and pruning policies through reinforcement learning. Experiments across various agent benchmarks demonstrate that ActiveMem consistently improves task completion, reasoning stability, and memory efficiency over existing memory-based agents. Moreover, ActiveMem enables compact open-weight models to achieve competitive performance with substantially larger proprietary systems.

## Metadata
- **Published**: 2026-09-27T05:30:01Z
- **Authors**: Song-Li Wu, Jingyi Wang, Zhaocheng Du, Weinan Gan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33244v1)