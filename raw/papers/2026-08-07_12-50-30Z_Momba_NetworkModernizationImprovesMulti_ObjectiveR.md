---
title: Momba: Network Modernization Improves Multi-Objective Reinforcement Learning
published: 2026-08-07T12:50:30Z
authors: Adam Štafa, Santeri Heiskanen, Petr Novotný, Joni Pajarinen
url: http://arxiv.org/abs/2608.07180v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Momba: Network Modernization Improves Multi-Objective Reinforcement Learning

## Abstract
Recent advances in deep reinforcement learning (RL) have shown that improving neural network architectures can yield substantial gains in sample efficiency and asymptotic performance without altering the underlying algorithms. In contrast, work on multi-objective reinforcement learning (MORL), which aims to discover a set of policies that balance trade-offs among conflicting objectives, has predominantly focused on algorithmic innovations, leaving the area of architectures underexplored. While the optimal policies and value functions can differ significantly depending on the trade-offs, MORL algorithms commonly represent them with simple feedforward networks conditioned on the trade-off. This raises the question of whether the performance of the algorithms could be improved with more expressive function approximators. In this paper, we integrate recent advances in neural network design: (i) observation and feature normalization, (ii) weight normalization, and (iii) modeling of distributional returns with an entropy-regularized MORL algorithm. The empirical results across standard continuous control benchmarks demonstrate that these changes substantially improve the quality of the produced solution sets without requiring major changes to the underlying algorithm.

## Metadata
- **Published**: 2026-08-07T12:50:30Z
- **Authors**: Adam Štafa, Santeri Heiskanen, Petr Novotný, Joni Pajarinen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07180v1)