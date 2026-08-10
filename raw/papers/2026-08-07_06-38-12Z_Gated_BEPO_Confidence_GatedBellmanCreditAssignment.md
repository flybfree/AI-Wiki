---
title: Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents
published: 2026-08-07T06:38:12Z
authors: Hongxi Yan, Ziyue Huang, Shichao Fan, Qingjie Liu
url: http://arxiv.org/abs/2608.06861v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents

## Abstract
Training large language model agents in long-horizon environments requires assigning credit from sparse terminal outcomes to individual actions. Existing critic-free methods propagate trajectory-level rewards uniformly across steps, while recent approaches construct step-level groups by matching repeated states and compare actions within each group. The former cannot distinguish useful actions in failed trajectories from ineffective actions in successful ones. The latter rely on step credit derived directly from individual trajectory outcomes and fixed-weight fusion with episode-level credit. We propose Gated-BEPO, which derives step-level credit from empirical rollout graphs. For each rollout group, Gated-BEPO constructs an empirical graph and estimates node values through a mean-backup Bellman fixed point that reflects the empirical action distribution of the current policy. We then accumulate these temporal-difference residuals along each sampled trajectory using generalized advantage estimation, yielding step-level Bellman advantages that capture both immediate and downstream effects. To adaptively fuse episode- and step-level credit, a confidence gate incorporates Bellman credit only at states with multiple observed successors and otherwise uses episode-level credit. Experiments on WebShop, ALFWorld, and visual Sokoban show consistent improvements across language and vision-language models, while diagnostic ablations support the effectiveness of Bellman fixed-point value estimation and show that step-level credit should be incorporated selectively rather than uniformly into the final advantage.

## Metadata
- **Published**: 2026-08-07T06:38:12Z
- **Authors**: Hongxi Yan, Ziyue Huang, Shichao Fan, Qingjie Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06861v1)