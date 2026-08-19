---
title: Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents
published: 2026-08-18T16:55:46Z
authors: Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
url: http://arxiv.org/abs/2608.18008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents

## Abstract
Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.

## Metadata
- **Published**: 2026-08-18T16:55:46Z
- **Authors**: Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18008v1)