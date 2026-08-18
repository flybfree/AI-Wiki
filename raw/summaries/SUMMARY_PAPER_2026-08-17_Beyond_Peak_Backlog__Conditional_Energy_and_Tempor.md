---
title: Beyond Peak Backlog: Conditional Energy and Temporal Geometry in Capacity-Constrained Delayed Bandit Optimization
url: http://arxiv.org/abs/2608.16216v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_07-49-51Z_BeyondPeakBacklog_ConditionalEnergyandTemporalGeom.md
generated_at: 2026-08-17 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the optimal delay complexity behaves when a learner can only track a limited number of pending feedback items, with discarded feedback permanently lost. It introduces a scheduler‑side conditional‑energy interface that yields an untuned learner whose regret scales as O(√E_C d_tot) and shows that even with identical aggregate delays, timing can cause polynomially different minimax regrets under strong convexity.

## Key Takeaways
- The conditional‑energy interface decouples rate adaptation from the one‑point perturbation filtration, allowing a delay term of order √(E_C d_tot) where E_C is an explicit restart factor.  
- A public constant‑factor peak bound removes the restart factor while keeping total delay d_tot unknown, and under strong convexity the temporal cost becomes H_A(d)=∑_t σ_t/(A+t).  
- Two delay vectors sharing the same d_tot, σ_max, and capacity can have polynomially different minimax regrets, demonstrating that timing matters even when aggregate delay summaries agree.

## Context
This work extends classic one‑point bandit convex optimization to settings where feedback is partially retained, a common scenario in online learning with memory constraints. By analyzing the interplay between tracking capacity C and total delay d_tot, the authors reveal new trade‑offs that were previously hidden by coarse aggregate bounds.

## Implications
For practitioners designing adaptive algorithms under limited feedback windows, this research suggests that managing the timing of feedback processing can be as crucial as the total number of queries. The derived upper bounds provide practical guidance for setting C relative to T, while the lower endpoint highlights potential capacity starvation when feedback is scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16216v1)
