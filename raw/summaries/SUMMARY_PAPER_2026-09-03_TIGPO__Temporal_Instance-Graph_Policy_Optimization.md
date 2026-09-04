---
title: TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2609.03383v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_05-32-43Z_TIGPO_TemporalInstance_GraphPolicyOptimizationforL.md
generated_at: 2026-09-03 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
TIGPO introduces a method for improving long‑horizon language model agents by extending graph‑based credit assignment across policy updates. By keeping a persistent transition graph and using both exploration and revisit slots, the approach enables more accurate advantage estimation than previous group‑local methods. Experiments on ALFWorld and WebShop show consistent gains over earlier approaches.

## Key Takeaways
- TIGPO maintains a persistent transition graph that links transitions from different policy versions, allowing joint credit assignment for current rollouts.
- It allocates a fixed rollout budget between ordinary task sampling and revisit slots to reconnect exploration with historical experience through cross‑temporal reference groups.
- The enlarged reference stabilizes advantage estimation while the comparison captures direct policy improvement across training stages.

## Context
Long‑horizon reinforcement learning for language models suffers from credit assignment problems where only recent rollouts influence updates. Traditional graph methods fail because they discard earlier transitions, limiting performance gains. TIGPO addresses this by integrating past and present experiences within a unified framework.

## Implications
This work offers practitioners a scalable way to refine agent policies without sacrificing sample efficiency. By leveraging historical data as structural references rather than replayable actions, it can be applied to diverse domains where long‑term planning is critical, such as robotics and autonomous decision making.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03383v1)
