---
title: Understanding Human-like Solutions in Combinatorial Optimization via Learning and Search
published: 2026-07-26T21:44:08Z
authors: Haijiang Yan, Jian-Qiao Zhu, Liqiang Huang, Ming Meng
url: http://arxiv.org/abs/2607.23854v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Human-like Solutions in Combinatorial Optimization via Learning and Search

## Abstract
Humans often find good solutions to combinatorial optimization problems that are computationally hard even for advanced computer algorithms. In the Euclidean traveling salesman problems (TSP), people rapidly produce tours that are near-optimal, despite severe limits on time and computation. What makes a tour human-like, and how might such solutions be learned? Here we address these questions through a large-scale behavioral and computational investigation of human performance in Euclidean TSP. We sampled a broad space of TSP instances, collected human solutions, and compared them with neural policies based on Pointer Networks, which are recurrent neural networks with an attention-based pointing mechanism that define probability distributions over valid tours. We trained these networks under multiple objectives, including reinforcement learning (RL), supervised learning from optimal tours, supervised learning from human tours, and RL fine-tuning after optimal-supervised pretraining. Human tours were not identical to optimal tours, but occupied a near-optimal geometric basin: they shared many structural properties with optimal solutions while preserving systematic human-specific deviations. The best account of human tours was not direct imitation of optimal tours, but a model pretrained on optimal tours, fine-tuned by RL, and decoded through $\text{Best-of-}N$ sampling. These findings suggest that human-like solutions may emerge from a combination of structured supervised learning, RL, and test-time search, echoing computational principles underlying many modern artificial intelligence systems.

## Metadata
- **Published**: 2026-07-26T21:44:08Z
- **Authors**: Haijiang Yan, Jian-Qiao Zhu, Liqiang Huang, Ming Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23854v1)