---
title: Balancing Expressivity and Learnability in Quantum Kernel Bandit Optimization
published: 2026-07-01T15:38:00Z
authors: Yuqi Huang, Vincent Y. F. Tan, Sharu Theresa Jose
url: http://arxiv.org/abs/2607.01080v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Balancing Expressivity and Learnability in Quantum Kernel Bandit Optimization

## Abstract
We investigate Gaussian process (GP) bandit optimization with quantum kernels, assuming the mean reward function lies in the reproducing kernel Hilbert space (RKHS) induced by the quantum kernel. This setting is motivated by NISQ-era tasks such as quantum control, state preparation and variational quantum algorithms. While quantum kernels can offer a `quantum advantage' via domain-specific inductive biases, naïvely using full, high-dimensional kernels increases model complexity and information gain, leading to higher cumulative regret and poor learnability. To address this, we propose projected quantum kernels and classical kernel approximation techniques that reduce feature dimensionality while preserving key quantum properties. Using these approximate kernels, we develop misspecified GP bandit algorithms and derive regret bounds that characterize the trade-off between approximation error and information gain. The regret bounds provide principled guidance for selecting the optimal model complexity. Empirically, our methods outperform full quantum kernels in sample efficiency, while substantially reducing computational overhead, enabling scalable GP optimization for quantum-native applications.

## Metadata
- **Published**: 2026-07-01T15:38:00Z
- **Authors**: Yuqi Huang, Vincent Y. F. Tan, Sharu Theresa Jose
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01080v1)