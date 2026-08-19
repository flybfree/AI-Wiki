---
title: Dijkstra as an Oracle for Online Stochastic Shortest Path Navigation with Provable Guarantees
url: http://arxiv.org/abs/2608.17703v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_12-26-17Z_DijkstraasanOracleforOnlineStochasticShortestPathN.md
generated_at: 2026-08-18 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes DORA, an online learner that uses Dijkstra as an oracle to navigate stochastic environments while guaranteeing low-cost paths. It demonstrates that nonnegative reduced costs allow exact planning without solving full value iteration. The approach also adds a logarithmic survival weight to bound the probability of contact with dynamic obstacles. Experiments show planner work reduction and lower contact rates compared to deterministic replanning.

## Key Takeaways
- The algorithm remains exact under a weaker condition than causality, namely nonnegativity of a reduced cost defined on the determinized map.
- It calls a shortest path oracle a fixed number of times per episode and never estimates a transition kernel.
- Learner reduces contacts during learning by a factor of seventeen relative to determinize and replan while keeping contact rates within budgets spanning two orders of magnitude.

## Context
The field seeks planners that handle unknown true traversal costs and imperfect actuation without prohibitive computation. Traditional methods like value iteration scale with map diameter, making them impractical for real‑time robot navigation. This work shows a fast alternative can match optimal performance under mild assumptions. This reduces reliance on large‑scale simulations.

## Implications
For autonomous robots operating alongside humans, this approach enables safe, efficient online navigation with minimal planning overhead. Practitioners can implement Dijkstra‑based oracles to reduce latency and maintain contact budgets in dynamic settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17703v1)
