---
title: SWE-MILE: Asynchronous Potential-Induced Milestone Credit Assignment for Long-Horizon Software Engineering Agents
published: 2026-09-26T13:49:14Z
authors: Chaoqun Cui, Hao Zhou, Meiqi Chen, Fandong Meng, Wenji Mao
url: http://arxiv.org/abs/2609.32631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-MILE: Asynchronous Potential-Induced Milestone Credit Assignment for Long-Horizon Software Engineering Agents

## Abstract
Long-horizon software engineering (SWE) agents trained with reinforcement learning with verifiable rewards (RLVR) typically receive only terminal outcome supervision, making it difficult to distinguish productive actions from redundant exploration or functional regressions. We propose SWE-MILE, an asynchronous potential-induced milestone credit assignment framework that derives fine-grained process supervision from workflow runtime, without auxiliary reward models or external evaluators. SWE-MILE quantifies task-relevant file exposure and test-state alignment as navigation and verification potentials, respectively. Differences in these potentials attribute milestone progress and regressions to individual actions, while discounted backward credit propagates supervision to preceding steps. To efficiently acquire intermediate verification states, SWE-MILE further introduces asynchronous shadow probing, which replays repository-changing actions in an isolated sandbox and runs verification in parallel with the agent's primary interaction, largely hiding verification latency. The resulting process credit augments terminal outcome advantages and provides informative learning signals. Experiments on two representative long-horizon SWE tasks demonstrate substantial improvements in agent performance, highlighting workflow runtime signals as a practical source of process supervision for long-horizon SWE agents.

## Metadata
- **Published**: 2026-09-26T13:49:14Z
- **Authors**: Chaoqun Cui, Hao Zhou, Meiqi Chen, Fandong Meng, Wenji Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32631v1)