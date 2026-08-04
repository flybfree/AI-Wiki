---
title: When Replanning Becomes the Bottleneck: Budgeted Replanning for Embodied Agents
url: http://arxiv.org/abs/2608.01428v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_18-17-35Z_WhenReplanningBecomestheBottleneck_BudgetedReplann.md
generated_at: 2026-08-03 23:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BRACE and E-RECAP to address the problem of frequent replanning in embodied agents where accumulated textual context causes heavy-tailed latency and SLO violations. By treating replanning as a budgeted control loop with explicit token budgets and service‑level objectives, they achieve significant reductions in token usage and SLO breach rates across simulated platforms.

## Key Takeaways
- BRACE reduces replanning‑call token counts by 62–92% while lowering SLO violation rates from near 100% to under 50%, showing that per‑call budgeting can mitigate tail latency. - The cost‑aware progressive pruning method E‑RECAP predicts token utility and removes non‑essential tokens across transformer layers without losing critical head or tail tokens, preserving plan quality. - In a challenging RoboFactory scenario where open‑loop plans fail, BRACE + E‑RECAP reaches 80% task success with only 4.6% SLO violations, proving effective tail‑aware budgeting even when other methods collapse.

## Context
Embodied AI agents rely on LLM‑driven replanning to correct drift and coordination issues, but the growing textual context inflates latency in unpredictable ways that average metrics hide. This work addresses a known bottleneck where latency spikes cause service failures despite high success rates, highlighting the need for explicit budgeting beyond simple efficiency.

## Implications
Practitioners can adopt budgeted replanning loops to keep LLM calls within real‑time constraints, improving reliability of autonomous robots and reducing cloud costs. The approach offers a reusable component that scales across diverse simulation environments, encouraging broader adoption in robotics research and industry deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01428v1)
