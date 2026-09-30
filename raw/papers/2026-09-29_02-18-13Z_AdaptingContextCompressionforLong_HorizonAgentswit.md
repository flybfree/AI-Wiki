---
title: Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations
published: 2026-09-29T02:18:13Z
authors: Guanghui Min, Liang Wu, Mingjia Shi, Yinhan He, Mayank Darbari, Liangjie Hong, Chen Chen
url: http://arxiv.org/abs/2609.36526v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations

## Abstract
Long-horizon agents require context compression to manage growing interaction histories. Compression quality, however, is ultimately determined by downstream execution. Existing prompt-adaptation methods infer compression errors by comparing full-context and compressed trajectories. Such comparisons cannot isolate individual compressions and are confounded by agent stochasticity. We first find that compression degrades reliability before solvability. Using matched counterfactual continuations that compare execution from the same agent state with versus without compression, we further show that severe degradation concentrates at isolated compression events. Motivated by this finding, we propose PAIR (Prompt Adaptation using Interventional Rollouts) for adapting structured compression prompts. PAIR identifies individual compressions that degrade subsequent execution, diagnoses their effects, and revises the relevant sections of a fixed compression template. PAIR achieves the strongest cross-run reliability among compressed methods in every main benchmark-scope combination, consistently exceeding the competing prompt-adaptation baseline. Without modifying the downstream agent, PAIR brings compressed execution close to the no-compression baseline and sometimes numerically exceeds it.

## Metadata
- **Published**: 2026-09-29T02:18:13Z
- **Authors**: Guanghui Min, Liang Wu, Mingjia Shi, Yinhan He, Mayank Darbari, Liangjie Hong, Chen Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36526v1)