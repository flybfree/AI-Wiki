---
title: TANGCO: Learning Topology-Aware Capacity Allocation for Overload-driven Cascading Failures
published: 2026-08-13T13:16:04Z
authors: Orkun Irsoy, Leman Akoglu, Osman Yagan
url: http://arxiv.org/abs/2608.13212v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TANGCO: Learning Topology-Aware Capacity Allocation for Overload-driven Cascading Failures

## Abstract
Networked systems, from power grids to traffic networks and cloud clusters, carry loads across nodes with limited capacity. A node whose load exceeds its capacity fails and sheds its load onto its neighbors, which can trigger a system-wide cascade. We study how to allocate a fixed capacity budget across nodes to resist these cascades under local load redistribution. The problem is difficult because no optimal allocation is known, and the fail-or-survive objective is non-differentiable and piecewise constant, so exact and gradient-based optimization methods do not directly apply. We introduce TANGCO (Topology-Aware Neural Graph-Guided Capacity Optimization), which uses a graph neural network policy trained through the cascade simulator with policy-gradient learning and a heuristic anchor. We evaluate TANGCO on five synthetic graph families and five real networks spanning power, road, air, and Internet topologies. The learned policy improves on the best of four hand-designed heuristics in all 450 synthetic instances and in 40 of 45 real-network conditions, with robustness gains ranging from 1.6% to 246%. The learned policies transfer to unseen graphs within a family and partially across related topologies, and TANGCO$^{pre}$, pre-trained on synthetic graphs, matches per-network training on unseen real networks. Training scales near-linearly with graph size, and TANGCO$^{pre}$ allocates on a new network with no per-target training, matching the deployment cost of a hand-designed heuristic. Free-vector variants without the GNN, stay close to the heuristics, so the graph representation carries the gain beyond numerical search. Finally, analysis of the learned allocations identifies when local risk is sufficient, leads to an improved closed-form heuristic, and reveals the regimes where a topology-aware learned policy remains necessary.

## Metadata
- **Published**: 2026-08-13T13:16:04Z
- **Authors**: Orkun Irsoy, Leman Akoglu, Osman Yagan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13212v1)