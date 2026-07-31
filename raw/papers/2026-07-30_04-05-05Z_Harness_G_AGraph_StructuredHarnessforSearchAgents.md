---
title: Harness-G: A Graph-Structured Harness for Search Agents
published: 2026-07-30T04:05:05Z
authors: Yanning Hou, Haoyuan Chen, Sihang Zhou, Xiaoshu Chen, Xirui Liu, Duanyang Yuan, Lingyuan Meng, Quan Liu, Jian Huang
url: http://arxiv.org/abs/2607.27652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness-G: A Graph-Structured Harness for Search Agents

## Abstract
Reinforcement learning (RL) search agents commonly model retrieval as free-form natural-language query generation and optimize multi-turn interactions using final-answer rewards. Current studies mainly improve training with denser or more structured credit signals, but rarely examine whether retrieval is properly formulated at the policy-environment interface. We observe pronounced retrieval aliasing during Search-R1 training: rollouts for the same question continue to generate distinct query strings, yet their accumulated evidence sets increasingly overlap. We call this phenomenon retrieval-equivalence collapse; in this regime, trajectories approach utility equivalence with respect to retrieval decisions, leaving within-group returns with little effective retrieval contrast. To address this problem, we propose Harness-G, a graph-structured retrieval framework that redesigns this interface. It reformulates free-form query generation as finite action selection: the policy selects an evidence sentence or entity, or chooses to answer, while the environment constructs the menu, tracks retrieval state, and validates and executes each choice. This interface reduces linguistic aliasing and makes same-state alternatives directly comparable. Building on this interface, we introduce Structured Non-myopic Credit (SNC), which uses a frozen answer scorer to compare the selected action with its alternatives and assigns downstream gains to the earlier actions that enabled them. Across six QA benchmarks, Harness-G achieves the highest average F1 at both evaluated model scales, outperforming the strongest baseline, Graph-R1, by 10.74 points at 1.5B and 3.98 points at 3B.

## Metadata
- **Published**: 2026-07-30T04:05:05Z
- **Authors**: Yanning Hou, Haoyuan Chen, Sihang Zhou, Xiaoshu Chen, Xirui Liu, Duanyang Yuan, Lingyuan Meng, Quan Liu, Jian Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27652v1)