---
title: Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR
published: 2026-07-28T20:43:23Z
authors: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
url: http://arxiv.org/abs/2607.26253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR

## Abstract
Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by rollout generation, yet many sampled prompts produce saturated groups (all responses correct or all incorrect) whose zero reward variance yields no policy-gradient signal. Existing remedies either oversample a larger candidate pool and discard saturated prompts (dynamic sampling), paying heavy extra rollouts, or predict prompt difficulty before sampling, which is fragile under a shifting policy. We observe that a group's effectiveness is usually decided early, within the first few of its rollouts, so spending a full group on an already-decided prompt is wasteful. We cast per-step rollout collection as a budget-constrained sequential allocation (optimal stopping) problem and introduce SARA (Sequential Adaptive Rollout Allocation). SARA maintains a Beta posterior over each prompt's success rate, evaluates a closed-form predictor of group effectiveness, and applies a two-threshold, SPRT-style rule that commits effective groups, abandons saturated ones after a short probe, and reallocates the freed budget to fresh prompts, without any extra prediction rollouts. We prove abandonment reliability, expected rollout savings, fixed-budget yield dominance, and a link between effective-group yield and the GRPO gradient norm. On mathematical reasoning and planning with 1.5B/3B models on a single GPU, SARA matches DPS (both below the DS oracle) while using 22% fewer rollouts than DS; composing SARA with DPS yields the best accuracy, slightly above DS, at 67% fewer rollouts (near-uniform cost).

## Metadata
- **Published**: 2026-07-28T20:43:23Z
- **Authors**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26253v1)