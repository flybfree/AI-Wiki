---
title: Goodput Maximization for Large Language Model Edge Inference: A Two-Phase Maskable PPO Approach
url: http://arxiv.org/abs/2608.25543v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_08-55-37Z_GoodputMaximizationforLargeLanguageModelEdgeInfere.md
generated_at: 2026-08-26 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces TP‑MPPO, a two‑phase maskable proximal policy optimization algorithm that maximizes goodput for large language model inference on edge devices while meeting strict service level objectives. It combines an MPPO phase with action masking to prune invalid offloading decisions and a closed‑form bandwidth allocation in the second phase. Simulation results show up to 87.5 % improvement over baselines.

## Key Takeaways  
- The first phase uses maskable PPO to optimize task offloading by restricting actions, which reduces exploration of infeasible solutions.  
- A second phase employs greedy downlink allocation for uplink bandwidth, providing immediate rewards that guide the next MPPO iteration.  
- Alternating phases converge quickly, delivering high goodput and SLO compliance.

## Context  
LLM inference on edge devices faces challenges of limited bandwidth and strict latency requirements. Traditional reinforcement learning approaches often explore invalid actions, degrading performance. This work addresses these issues with a structured two‑phase policy optimization that balances exploration and exploitation.

## Implications  
For practitioners deploying AI services at the network edge, TP‑MPPO offers a practical framework to balance throughput and reliability without exhaustive search. The method can be adapted to other resource‑constrained inference tasks, enhancing system efficiency and user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25543v1)
