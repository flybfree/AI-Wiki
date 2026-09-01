---
title: PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents
published: 2026-08-31T13:26:16Z
authors: Ziyi Bai, Siqi Li, Tinglei Huang, Börje F. Karlsson
url: http://arxiv.org/abs/2608.30760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents

## Abstract
Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans. However, building agents that can continually improve through interaction and rapidly adapt to their environments remains challenging. Summing up experience from past interaction trajectories provides a promising solution, but existing experience-based methods often rely on manually designed prompting workflows to extract and update skills. Such fixed procedures may struggle to learn updated skills from new and diverse experiences. We introduce PRACTICE, which trains a skill learner to discover and maintain a persistent skill library from past interaction trajectories while keeping the task executor frozen. Given the historical accumulated skills and incoming trajectories, the skill learner produces structured batch-edits that add, refine, merge, or remove skills, and then hierarchical consolidate all collected edits into a consistent updated skill library. We train the learner with a two-stage curriculum. First, it learns basic skill generation and library maintenance from oracle trajectories. Then, by contrasting successful and failed trajectories from heterogeneous executors on the same tasks, it learn to identify invalid action patterns and recovery strategies. Finally, we apply online skill-edit distillation to align the skill learner with a stronger teacher on its current edit distribution to further improves the policy. Experiments demonstrate that a compact skill learner delivers consistent performance improvements across successive library-update rounds for multiple frozen executors. On EB-ALFRED and EB-Habitat, PRACTICE further outperforms the strongest experience-based baselines. Project resources are publicly available at: https://baai-agents.github.io/PRACTICE

## Metadata
- **Published**: 2026-08-31T13:26:16Z
- **Authors**: Ziyi Bai, Siqi Li, Tinglei Huang, Börje F. Karlsson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30760v1)