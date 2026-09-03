---
title: PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks
url: http://arxiv.org/abs/2609.02236v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_07-44-16Z_PGPO_Potential_GuidedPolicyOptimizationforMulti_Tu.md
generated_at: 2026-09-02 20:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Potential‑Guided Policy Optimization (PGPO) to improve credit assignment in multi‑turn agentic tasks where terminal rewards are sparse. By estimating state potentials from anchor‑state‑group return statistics, PGPO derives action advantages that propagate across trajectories, yielding finer‑grained step‑level credit especially for actions within failed rolls.

## Key Takeaways
- PGPO estimates empirical state potentials using return statistics within each rollout group, allowing cross‑trajectory credit propagation.  
- The method provides more informative failure‑side credit signals while keeping training overhead negligible.  
- Experiments on ALFWorld and WebShop demonstrate strong overall performance compared to recent group‑based RL approaches.

## Context
Group‑based reinforcement learning has become a cornerstone for leveraging LLM post‑training, yet its credit assignment often fails to differentiate actions in long or failed trajectories. PGPO addresses this limitation by introducing a potential‑based mechanism that captures state‑level information without relying on terminal outcomes.

## Implications
For practitioners developing multi‑turn agents, PGPO offers a scalable way to refine policy learning and reduce the impact of erroneous actions. The approach can be integrated into existing RL pipelines with minimal computational cost, supporting more reliable decision making in complex interactive environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02236v1)
