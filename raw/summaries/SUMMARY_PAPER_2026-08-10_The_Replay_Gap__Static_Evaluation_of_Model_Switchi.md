---
title: The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World
url: http://arxiv.org/abs/2608.08239v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_17-07-11Z_TheReplayGap_StaticEvaluationofModelSwitchinginLLM.md
generated_at: 2026-08-10 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the shortcomings of static replay-based evaluation for model switching in LLM agents, demonstrating that swapping models along a logged trajectory often rewrites large portions of subsequent actions and misleads evaluators. Across 900 rollouts, model swaps cause 61‑94% of post‑fork actions to change, with many early swaps diverging at the first step, while replay evaluations predict outcomes with near‑zero similarity.

## Key Takeaways
- Swapping models during agent execution rewrites a substantial fraction (61‑94%) of actions after the fork point.  
- Early model switches frequently cause divergence from the original trajectory, affecting 74‑77% of first post‑fork steps versus only 6‑35% in control runs.  
- Replay evaluators mispredict success‑relevant calls and produce patches with 0.00‑0.11 similarity to reality.

## Context
LLM routers aim to route requests to the most cost‑effective model, but current evaluation treats each router as a single turn by replaying logs without accounting for dynamic model behavior. This static approach ignores how model differences can fundamentally alter downstream reasoning and task completion.

## Implications
If agents rely on cheap model swaps, their performance may be severely underestimated or overestimated by existing benchmarks. Practitioners must adopt more realistic evaluation methods that capture actual model interactions to avoid deploying routing strategies that fail in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08239v1)
