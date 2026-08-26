---
title: Contrastive Branch Policy Optimization
published: 2026-08-25T09:25:55Z
authors: Ying Wang, Changlin Qiu, Bang Lin, Linbo Jin, Wen Jiang, Zhe Sun, Jingli Yang
url: http://arxiv.org/abs/2608.24300v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contrastive Branch Policy Optimization

## Abstract
Reinforcement learning with verifiable rewards (RLVR) enables language models to learn multi-turn interaction with external tools, yet its sparse outcome rewards provide no signal for identifying which intermediate decisions are responsible for success. Branch sampling induces local comparisons among alternative continuations, but existing methods tend to conflate two distinct problems: allocating a fixed rollout budget and translating branch outcomes into token-level credit. We introduce Contrastive Branch Policy Optimization (CBPO), which disentangles these two problems and assigns a dedicated mechanism to each. Generation entropy screens candidate branch positions across the entire response, while path-level and node-level decay distribute a fixed budget across trajectories and positions to prevent exploration from collapsing onto a few paths or adjacent tokens. A parent trajectory together with the branches that share an identical token prefix forms an exact-prefix group, and the reward variation within this controlled group defines the Contrastive Branch Value (CBV), an outcome-based estimate of local decision sensitivity that rescales continuation advantages without altering their sign. When multiple nodes are selected along the same trajectory, CBPO partitions it into non-overlapping credit segments, thereby avoiding duplicated gradients on shared tokens. Requiring only outcome rewards and no process-level annotation, CBPO provides a practical solution for fine-grained credit assignment in tool-integrated agent training. Extensive experiments on ten benchmarks, including five for mathematical reasoning and five for knowledge-intensive search, show that CBPO consistently outperforms state-of-the-art policy-optimization and branch-based methods, attaining the highest macro-average accuracy in both domains and across two model scales.

## Metadata
- **Published**: 2026-08-25T09:25:55Z
- **Authors**: Ying Wang, Changlin Qiu, Bang Lin, Linbo Jin, Wen Jiang, Zhe Sun, Jingli Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24300v1)