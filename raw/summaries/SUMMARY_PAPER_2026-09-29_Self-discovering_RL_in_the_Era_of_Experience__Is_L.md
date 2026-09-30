---
title: Self-discovering RL in the Era of Experience: Is Learning History an Asset or a Burden?
url: http://arxiv.org/abs/2609.35897v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-27_20-56-26Z_Self_discoveringRLintheEraofExperience_IsLearningH.md
generated_at: 2026-09-29 20:44
model: qwen3.6-35b-a3b
---

## Summary
This paper presents the first causal mechanistic audit of a self-discovered reinforcement learning rule, Disco103, to determine whether learning history functions as an asset or a burden within the framework of the "Era of Experience." Through surgical interventions on recurrent states while holding meta-parameters fixed, the study demonstrates that history significantly expands reward scale utilization but can induce performance penalties due to state clamping, and that external data turnover may confound internal plasticity advantages over baselines like DQN.

## Key Takeaways
- Recurrent learning history actively expands usable reward scales, sustaining a six-decade window of effective operation compared to only three under zero-pinning conditions, indicating that maintaining historical context is crucial for handling extended horizons and grounded reward magnitudes in self-improving agents.
- Decoupling historical content from its maintenance reveals that the penalty associated with mismatched history stems from perpetual clamping rather than the content itself; allowing imported states to evolve naturally attenuates this burden, suggesting that rigid state preservation hinders adaptation while dynamic evolution supports it.
- Controlling replay retention under environmental change reverses the apparent adaptation advantage of self-discovered rules over DQN, demonstrating that external data turnover can confound internal plasticity assessments and highlighting the need for rigorous causal controls when evaluating learning dynamics in continuing streams.

## Context
The pursuit

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35897v1)
