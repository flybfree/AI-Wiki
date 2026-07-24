---
title: Offline RL with Hierarchical Action Chunking
published: 2026-07-23T01:48:46Z
authors: Ahad Jawaid
url: http://arxiv.org/abs/2607.20834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Offline RL with Hierarchical Action Chunking

## Abstract
Offline goal-conditioned reinforcement learning (RL) holds the promise of learning general-purpose policies from static datasets. However, scaling these methods to long-horizon tasks remains a challenge due to the curse of horizon, where value estimation errors can compound through long chains of bootstrapped Bellman backups. Existing hierarchical approaches mitigate this by decomposing tasks into subgoals, yet they often rely on low-level controllers that suffer from myopic execution and biased value estimates. In this work, we propose Hierarchical Implicit Q-Chunking (HiQC), an offline goal-conditioned RL algorithm that combines high-level latent planning with low-level action chunking. By conditioning the low-level critic on temporally extended action sequences, HiQC enables unbiased k-step value backups, compressing the horizon at both the planning and execution levels. We theoretically demonstrate that this dual decomposition results in a tighter bound on value error under a bounded per-backup error model compared to standard hierarchy or flat chunking alone. Empirically, HiQC achieves the highest aggregate performance among the compared methods on the OGBench suite, with its largest gains on long-horizon navigation tasks such as humanoid-giant.

## Metadata
- **Published**: 2026-07-23T01:48:46Z
- **Authors**: Ahad Jawaid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20834v1)