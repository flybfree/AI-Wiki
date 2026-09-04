---
title: PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing
url: http://arxiv.org/abs/2609.03503v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_08-04-30Z_PPO_STGNN_AProximalPolicyOptimizationApproachwithS.md
generated_at: 2026-09-03 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents PPO‑STGNN, a reinforcement‑learning based scheduling algorithm that combines proximal policy optimization with spatio‑temporal graph neural networks to solve DAG task scheduling in cloud‑edge‑end environments. The method learns a policy that balances computational load and energy use while minimizing makespan and schedule length ratio, achieving state‑of‑the‑art performance on benchmark tasks.

## Key Takeaways
- PPO‑STGNN uses an STGNN to fuse the DAG topology with the heterogeneous resource graph, extracting features for scheduling decisions.
- A multi‑teacher behavior‑cloning pretraining accelerates policy convergence in a complex, dynamic setting.
- The algorithm improves CPU and memory load balancing without significantly increasing completion time.

## Context
The integration of graph neural networks with reinforcement learning is emerging as a powerful tool for modeling spatial dependencies in distributed computing. This work demonstrates how such hybrid models can address the NP‑hard nature of scheduling under resource constraints. These findings highlight the importance of dynamic adaptation in resource allocation.

## Implications
For cloud‑edge‑end operators, PPO‑STGNN offers a scalable approach to maintain performance across heterogeneous nodes. Practitioners can leverage the method to design policies that adapt to real‑time changes in capacity and energy budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03503v1)
