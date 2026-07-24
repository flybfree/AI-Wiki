---
title: From Agent Failures to Text Policies: What Works and What Breaks
url: http://arxiv.org/abs/2607.20668v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_19-08-19Z_FromAgentFailurestoTextPolicies_WhatWorksandWhatBr.md
generated_at: 2026-07-23 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how textual feedback can be used to improve language‑model agents without altering their weights, focusing on the difficulty of linking feedback to specific decisions in sequential tasks. The authors find a clear gap between an agent’s ability to follow a useful policy and its capacity to learn that policy from experience, showing that human‑written policies boost frozen 7B models by five success points while trajectory‑generated policies do not.

## Key Takeaways
- Human‑crafted policy text can significantly improve frozen agents on TextWorldExpress, indicating that well‑designed textual guidance is effective.  
- Policy generation from agent trajectories remains unreliable even when enriched with counterfactual evidence or iterative GEPA search, highlighting a limitation in extracting useful policies automatically.  
- The primary challenge for agent‑level TextGrad lies not in applying policy updates but in reliably generating and selecting them from limited experience.

## Context
The study addresses a growing need to integrate feedback into autonomous agents, where traditional gradient methods fail because actions are delayed and uninterpreted. By separating policy execution from policy learning, the work contributes to broader efforts on interpretable reinforcement learning and human‑in‑the‑loop optimization of AI behavior.

## Implications
For practitioners, this research suggests that providing clear, human‑written instructions can be a low‑cost way to boost agent performance without retraining large models. It also warns against assuming that automatically generated policies will match the quality of expert‑crafted ones, urging careful design of feedback mechanisms in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20668v1)
