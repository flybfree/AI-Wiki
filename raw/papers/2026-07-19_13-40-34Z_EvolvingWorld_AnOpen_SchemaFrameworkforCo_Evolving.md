---
title: EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World
published: 2026-07-19T13:40:34Z
authors: Qing Zong, Yue Guo, Mengxin Yang, Yiwen Guo, Yangqiu Song
url: http://arxiv.org/abs/2607.17250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World

## Abstract
This paper introduces EvolvingWorld, a framework and benchmark for character and world co-evolution in interactive literary worlds. Existing systems either treat interactive literary simulation as static persona imitation or isolated scene generation, failing to capture how characters and worlds evolve together over time. To address this, EvolvingWorld models literary simulation as a long-horizon process where characters interact, scenes progress, and character and world states are persistently updated. Unlike prior systems relying on fixed schemas, EvolvingWorld adopts an open-schema framework to support simulation across diverse literary worlds. The framework consists of two coupled modules: a Character Agent for multi-character role-play and persistent profile evolution, and an LLM-based World Model for global and location/entity-level state maintenance and scene progression. Based on this architecture, we formulate 7 trainable tasks for scene initialization, interaction generation, and state update. We construct a dataset from 57 books, producing 138,596 supervised training samples and 222 snapshots for testing. Furthermore, we introduce a trajectory-level LLM-as-Judge evaluation protocol spanning 10 dimensions and 20 metrics. Experiments show that EvolvingWorld can improve long-horizon simulation by effectively maintaining persistent, coherent character and world development.

## Metadata
- **Published**: 2026-07-19T13:40:34Z
- **Authors**: Qing Zong, Yue Guo, Mengxin Yang, Yiwen Guo, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17250v1)