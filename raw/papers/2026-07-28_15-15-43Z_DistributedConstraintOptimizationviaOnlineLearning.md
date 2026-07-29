---
title: Distributed Constraint Optimization via Online Learning and Iterative Pricing with Application to Large-Scale Satellite Scheduling
published: 2026-07-28T15:15:43Z
authors: Itai Zilberstein, Pranav Rajbhandari, Steve Chien, Tuomas Sandholm
url: http://arxiv.org/abs/2607.25835v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distributed Constraint Optimization via Online Learning and Iterative Pricing with Application to Large-Scale Satellite Scheduling

## Abstract
Distributed constraint optimization problems (DCOPs) provide a popular framework for distributed decision making under limited communication, but many real-world instances are too large to solve monolithically. We address this challenge from two complementary directions. We revisit the connection between DCOPs and potential games, and adapt modern online learning algorithms for equilibrium finding to DCOPs. We show that these algorithms are competitive with representative incomplete DCOP algorithms. We then turn to decomposition frameworks for large-scale DCOPs, motivated by large-scale decentralized satellite scheduling. We propose a new framework that separates a DCOP into two interacting subproblems: a high-level meta-DCOP for task allocation, and independent local optimization problems for scheduling. To couple the two levels, we develop a novel iterative pricing method that updates the meta-level utilities using feedback from the local optimizers. Combining our online learning methods with our iterative pricing framework, we obtain near-optimal performance on real-world decentralized satellite scheduling problem instances, fulfilling over 99% of observation requests compared with 87% for state-of-the-art baselines.

## Metadata
- **Published**: 2026-07-28T15:15:43Z
- **Authors**: Itai Zilberstein, Pranav Rajbhandari, Steve Chien, Tuomas Sandholm
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25835v1)