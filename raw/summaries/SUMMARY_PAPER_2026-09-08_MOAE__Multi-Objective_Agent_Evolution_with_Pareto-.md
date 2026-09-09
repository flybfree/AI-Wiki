---
title: MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search
url: http://arxiv.org/abs/2609.05992v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-05_09-31-34Z_MOAE_Multi_ObjectiveAgentEvolutionwithPareto_Prese.md
generated_at: 2026-09-08 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MOAE a method for optimizing multiple agent objectives through Pareto-preserving evolutionary search. It demonstrates that MOAE improves task performance and trajectory quality while keeping safety high within limited rollout budgets on TravelPlanner and AgentDojo benchmarks.

## Key Takeaways
- MOAE maintains an empirical archive of non-dominated candidates throughout the evolutionary process, preserving trade‑off solutions rather than collapsing them into a single scalar score.
- The search uses objective‑specific diagnostics to generate offspring, separating candidate preservation from final preference selection at deployment.
- Experiments show that Pareto preservation expands the attainable objective region and increases joint improvement frequency compared with scalarized approaches.

## Context
Current LLM agent evaluation often reduces diverse goals to one numeric metric, limiting exploration of useful trade‑offs. Multi‑objective methods are needed to capture nuanced performance across accuracy, interaction quality, safety, and efficiency without sacrificing any dimension.

## Implications
Practitioners can adopt MOAE’s in‑context evolutionary framework to design agents that balance multiple critical metrics without premature scalarization, leading to more robust deployments. This approach supports scalable research on agent optimization where trade‑offs are essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05992v1)
