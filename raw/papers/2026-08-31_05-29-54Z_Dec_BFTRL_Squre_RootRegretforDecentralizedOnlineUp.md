---
title: Dec-BFTRL: Squre-Root Regret for Decentralized Online Upper-Linearizable Optimization under Separation Access with Application to Continuous Submodular Maximization
published: 2026-08-31T05:29:54Z
authors: Yiyang Lu, Mohammad Pedramfar, Vaneet Aggarwal
url: http://arxiv.org/abs/2608.30271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dec-BFTRL: Squre-Root Regret for Decentralized Online Upper-Linearizable Optimization under Separation Access with Application to Continuous Submodular Maximization

## Abstract
We study decentralized online optimization of upper-linearizable payoffs over an action set under efficient separation access, with applications to online continuous diminishing-return (DR) submodular maximization. We propose Decentralized Barrier Follow-the-Regularized-Leader (Dec-BFTRL), and evaluate each agent's played action against the average of all local objectives. Each agent maps an internal iterate to a feasible action through an approximate gauge projection, communicates only a cumulative surrogate-gradient dual state, and invokes the local HybridNewton procedure to approximately minimize its post-communication BFTRL potential. For every agent, we achieve expected network-aggregate regret of $\widetilde O(\sqrt{T})$. Over $T$ rounds, each agent uses $T$ neighbor-mixing steps and $\widetilde O(T)$ separation-oracle calls. We give four wrapper instantiations covering three DR-submodular maximization problems.

## Metadata
- **Published**: 2026-08-31T05:29:54Z
- **Authors**: Yiyang Lu, Mohammad Pedramfar, Vaneet Aggarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30271v1)