---
title: Variance-Reduced Q-Learning over Static and Time-Varying Networks
published: 2026-07-24T00:24:09Z
authors: Sreejeet Maity, Feng Zhu, Aritra Mitra, Robert W. Heath
url: http://arxiv.org/abs/2607.21876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Variance-Reduced Q-Learning over Static and Time-Varying Networks

## Abstract
We investigate a decentralized reinforcement learning problem involving multiple agents that interact with the same Markov Decision Process (MDP). The agents can exchange information over a network to collectively learn the optimal state-action value function. For this setting, we introduce a novel epoch-based distributed $Q$-learning algorithm called VRDQ, where within each epoch, agents locally estimate the Bellman optimality operator and diffuse information using a consensus-based protocol. For both static and time-varying networks, we establish high-probability finite-time convergence rates for VRDQ that enjoy linear speedups from collaboration. Crucially, we prove that such speedups in sample-complexity require only $\tilde{O}(1)$ communication, substantially improving upon the communication costs in prior work.

## Metadata
- **Published**: 2026-07-24T00:24:09Z
- **Authors**: Sreejeet Maity, Feng Zhu, Aritra Mitra, Robert W. Heath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21876v1)