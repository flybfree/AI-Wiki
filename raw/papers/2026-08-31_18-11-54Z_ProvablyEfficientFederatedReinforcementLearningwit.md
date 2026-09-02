---
title: Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost
published: 2026-08-31T18:11:54Z
authors: Zihang Liang, Haochen Zhang, Lingzhou Xue
url: http://arxiv.org/abs/2609.00193v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Provably Efficient Federated Reinforcement Learning with Linear Function Approximation and Logarithmic Communication Cost

## Abstract
We study federated online reinforcement learning with linear function approximation. While recent multi-agent reinforcement learning algorithms achieve strong regret guarantees, they typically require sharing raw trajectories. This reliance incurs a communication cost that scales linearly with the number of episodes and violates the privacy constraints of federated settings. To address these limitations, we propose Fed-LSVI, the first provably efficient federated algorithm for online reinforcement learning with linear function approximation in episodic Markov decision processes. By integrating a determinant-based event-triggered synchronization with a stepwise backward update mechanism, Fed-LSVI enables agents to collaboratively learn an optimal policy by exchanging only compressed sufficient statistics. We prove that Fed-LSVI achieves a regret bound of $\widetilde{\mathcal O}(\sqrt{Md^3H^4T})$, where $d$ is the feature dimension, $H$ is the horizon length, $M$ is the number of agents, and $T$ is the number of episodes per agent, matching the best-known regret for multi-agent online reinforcement learning with linear function approximation. Moreover, by following the stringent communication and privacy constraints of the federated setting, Fed-LSVI reduces the communication cost to only logarithmic dependence on $T$, representing a significant improvement over prior methods.

## Metadata
- **Published**: 2026-08-31T18:11:54Z
- **Authors**: Zihang Liang, Haochen Zhang, Lingzhou Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00193v1)