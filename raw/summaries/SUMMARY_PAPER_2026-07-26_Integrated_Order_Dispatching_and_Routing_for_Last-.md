---
title: Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement Learning
url: http://arxiv.org/abs/2607.22356v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_14-37-02Z_IntegratedOrderDispatchingandRoutingforLast_MilePi.md
generated_at: 2026-07-26 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an integrated order dispatching and routing framework that jointly learns a routing oracle and uses real-time heuristics for last-mile pickup decisions. It combines a dynamic residual graph attention network with a personalized look‑ahead decoder to solve the routing subproblem, while the dispatching heuristic leverages the learned solution to select couriers via local search. Experiments on Cainiao Logistics data show faster solving times and higher quality solutions compared to existing benchmarks.

## Key Takeaways
- The framework jointly optimizes routing and dispatching instead of treating them separately, addressing their tight coupling.
- A dynamic residual graph attention network encoder with a personalized look‑ahead decoder provides near‑optimal routing solutions.
- Dispatching uses the learned oracle to guide local search, preserving real‑time scalability on large instances.

## Context
Recent advances in reinforcement learning have enabled complex decision‑making tasks, yet last‑mile logistics remains challenging due to sparse rewards and high dimensionality. This work demonstrates how deep neural architectures can be combined with heuristic search to produce scalable solutions for real‑world scheduling problems.

## Implications
The integrated approach offers a practical model that logistics companies can adopt to improve delivery efficiency without sacrificing responsiveness. By reducing solving time while maintaining solution quality, the method supports broader adoption of AI in operational routing and dispatching.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22356v1)
