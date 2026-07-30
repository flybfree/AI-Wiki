---
title: Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents
url: http://arxiv.org/abs/2607.27083v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_16-07-37Z_ScoresAreNotDecisions_Cost_AwareStoppingforToolAcq.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the challenge of selecting tools for LLM agents when each tool has different acquisition costs, showing that simply ranking tools by relevance is insufficient. It introduces cost-aware marginal decision-focused stopping (CAM-DF) and a lightweight variant CAM-DF-lite to decide how many ranked tools to use based on expected payoff gaps. Experiments across 1343 tasks demonstrate CAM-DF outperforms baseline methods, achieving higher task success while reducing tool exposure by 37%.

## Key Takeaways
- The objective uses the sign and magnitude of the offline gap between stopping now and best continuation to label decisions, weighting errors by payoff at stake.  
- CAM-DF is Bayes-aligned with the stopping target and outperforms score-only rules under heterogeneous costs.  
- Live evaluation shows CAM-DF reduces tool usage by 37% while maintaining comparable task success.

## Context
LLM agents increasingly rely on external services, creating a trade‑off between information gain and operational cost. Existing solutions ignore these varying acquisition expenses, leading to suboptimal tool selection that can degrade performance or increase privacy risk.

## Implications
This work provides a principled framework for cost‑aware tool acquisition that can be integrated as a pre‑execution plugin without retraining agents. Practitioners can deploy it across diverse domains to balance efficiency and effectiveness in real‑world agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27083v1)
