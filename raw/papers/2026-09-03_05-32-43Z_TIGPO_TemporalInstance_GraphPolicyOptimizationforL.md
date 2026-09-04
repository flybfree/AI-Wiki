---
title: TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents
published: 2026-09-03T05:32:43Z
authors: Jinwei Gan
url: http://arxiv.org/abs/2609.03383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents

## Abstract
Graph-based policy optimization improves credit assignment for long-horizon LLM agents by organizing rollout trajectories into state-transition graphs. However, existing methods construct graphs independently within each policy update, discarding transitions discovered by earlier policies and limiting advantage estimation to small, batch-local rollout groups. We propose \emph{Temporal Instance-Graph Policy Optimization} (TIGPO), which extends graph-based credit assignment across policy updates. TIGPO maintains a persistent transition graph for each task, allowing valid transitions discovered by different policy versions to jointly determine credit for current rollouts. To actively reconnect current exploration with historical experience, TIGPO allocates a fixed rollout budget between Exploration slots for ordinary task sampling and Revisit slots for delayed reattempts of previously explored tasks. For each revisit, TIGPO pairs the current rollout group with its corresponding earlier Exploration group to construct a cross-temporal reference. The enlarged reference is designed to stabilize relative advantage estimation under small rollout groups, while comparison on the same task directly captures policy improvement across training stages. Historical transitions and scores serve only as structural and detached statistical references and are never replayed in the policy loss. Experiments on ALFWorld and WebShop demonstrate that TIGPO consistently outperforms prior group-based and graph-based policy optimization methods.

## Metadata
- **Published**: 2026-09-03T05:32:43Z
- **Authors**: Jinwei Gan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03383v1)