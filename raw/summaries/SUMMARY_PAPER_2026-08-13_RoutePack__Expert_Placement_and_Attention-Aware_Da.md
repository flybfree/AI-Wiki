---
title: RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning
url: http://arxiv.org/abs/2608.12146v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_15-07-15Z_RoutePack_ExpertPlacementandAttention_AwareDataPac.md
generated_at: 2026-08-13 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RoutePack, a hierarchical planner for MoE reinforcement learning that jointly optimizes expert placement and attention-aware data packing across an optimizer-step window. It improves token throughput on two benchmark models by up to 14.89% compared with baselines. The method coordinates state-consistent routing and packing while preserving existing kernels.

## Key Takeaways
- RoutePack places experts independently per layer using aggregate demand, then packs samples into the smallest certified number of token-capped execution rows.
- It optimizes a projected EDP-shard-aware objective that combines attention proxy with EP-rank peaks to minimize slowest shard cost.
- Parallel population annealing maintains fixed-row feasible layouts while respecting coverage, capacity, nonempty cells, equal microbatch counts, and communicator topology.

## Context
Mixture-of-experts models face dual load balancing challenges in reinforcement learning where sequence composition and token routing compete. Existing solutions treat each problem separately, often causing bottlenecks that degrade throughput. This work addresses the interaction between attention and expert demand within a single planning horizon.

## Implications
For practitioners, RoutePack offers a practical way to boost MoE efficiency without redesigning hardware or software stacks. The gains translate into lower compute costs and faster training cycles, making large-scale RL models more viable for industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12146v1)
