---
title: IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents
url: http://arxiv.org/abs/2608.24588v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_14-14-36Z_IAPO_Influence_AwarePolicyOptimizationforCreditAss.md
generated_at: 2026-08-25 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Influence-Aware Policy Optimization (IAPO), a method for credit assignment in multi-turn service agents where task information emerges over time. IAPO models each rollout as an influence-dependency graph that captures how user and tool observations guide actions, redistributing trajectory-level rewards to individual steps. Experiments show IAPO outperforms existing RL baselines on three benchmarks with Qwen3 models.

## Key Takeaways
- The paper proposes a typed influence-dependency graph representation for rollouts, turning support-use and failed-use patterns into routing weights that allocate the same trajectory advantage across actions.
- It demonstrates superior performance over multi-turn reinforcement learning approaches on τ^2‑Bench, UserBench, and AgentChangeBench using Qwen3‑4B and Qwen3‑8B models.
- The gains do not affect function‑calling capabilities in BFCL‑v4 Multi-Turn, showing that credit assignment can be learned without degrading multi‑turn tool usage.

## Context
Multi‑turn service agents face sparse feedback because user goals evolve and tools provide partial information. Traditional RL methods struggle to assign credit when the final reward does not reflect intermediate contributions. This work addresses the need for a principled way to learn from rollout traces rather than relying on external signals or resampling.

## Implications
IAPO offers practitioners a scalable framework for training agents that can adapt to dynamic user instructions and tool responses. By improving credit assignment, it enhances task completion accuracy and reduces unnecessary actions, which is crucial for real‑world deployment of conversational AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24588v1)
