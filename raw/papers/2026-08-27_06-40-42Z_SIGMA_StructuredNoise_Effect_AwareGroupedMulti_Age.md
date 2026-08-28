---
title: SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation
published: 2026-08-27T06:40:42Z
authors: Li Mingqian
url: http://arxiv.org/abs/2608.26683v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation

## Abstract
Cooperative multi-agent reinforcement learning (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making can become structured through underlying cooperation structures. We characterize this phenomenon as structured noise effects, where noise-induced decision effects exhibit local correlation among agents with stronger task-related dependencies while remaining globally heterogeneous across different agents and local structures. Existing robust MARL methods, however, rarely explicitly characterize or exploit such structure-dependent noise effects. To address this limitation, we propose SIGMA, a hierarchical collaboration framework that exploits cooperation structures to learn robust representations under noisy observations. SIGMA first organizes agents into adaptive local structures through density-based grouping and performs intra-group consensus aggregation to preserve shared task-relevant information while smoothing agent-specific representation deviations. Inter-group attention then adaptively integrates information across different groups to preserve global coordination while accommodating their heterogeneous contributions. Experiments on noisy-observation tasks in StarCraft II empirically validate the structured noise effects and demonstrate that SIGMA consistently improves robustness under observation noise while maintaining competitive performance in noise-free environments.

## Metadata
- **Published**: 2026-08-27T06:40:42Z
- **Authors**: Li Mingqian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26683v1)