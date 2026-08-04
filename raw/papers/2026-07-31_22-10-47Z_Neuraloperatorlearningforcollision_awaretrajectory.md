---
title: Neural operator learning for collision-aware trajectory planning of spacecraft swarms
published: 2026-07-31T22:10:47Z
authors: Sidhdharth D. Sikka, Suyi Gao, Zehui Lu, Rongjie Lai, Shaoshuai Mou
url: http://arxiv.org/abs/2608.00320v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural operator learning for collision-aware trajectory planning of spacecraft swarms

## Abstract
Autonomous spacecraft swarms must plan fuel-efficient, collision-free maneuvers in increasingly congested orbits, yet classical trajectory optimization scales poorly as pairwise safety constraints multiply with swarm size, and learning-based planners rarely transfer across swarm sizes or debris densities. Here we introduce a permutation-equivariant neural operator that maps distributions of spacecraft, targets and debris to collision-aware trajectories for an entire swarm in a single forward pass, paired with a batched Gauss-Newton finish that enforces exact orbital dynamics. The operator is trained without optimal-trajectory labels, combining self-supervised physics objectives with adversarial threats generated against its own rollouts. Trained on ten spacecraft, it generalizes zero-shot to swarms of 1,000 amid more than 11,000 catalogued objects, matching a per-agent optimal-control solver's accuracy, evading worst-case threats that a debris-blind baseline cannot, and reducing proximity within the swarm several-fold. Physics-grounded operator learning thus offers a fast, scalable alternative to optimal control for crowded orbits.

## Metadata
- **Published**: 2026-07-31T22:10:47Z
- **Authors**: Sidhdharth D. Sikka, Suyi Gao, Zehui Lu, Rongjie Lai, Shaoshuai Mou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00320v1)