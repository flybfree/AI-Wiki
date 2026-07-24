---
title: RRPO: Reference-Relative Policy Optimization with Stratified Conditional Rollouts
url: http://arxiv.org/abs/2607.18470v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_19-40-25Z_RRPO_Reference_RelativePolicyOptimizationwithStrat.md
generated_at: 2026-07-23 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Reference-Relative Policy Optimization, RRPO, a method that extends group relative policy optimization without relying on verifier correctness signals. It replaces direct advantage computation with contrastive comparisons using stratified conditional rollouts and a metric projection head. Experiments show RRPO remains competitive across various settings.

## Key Takeaways
- RRPO constructs positive and negative anchor sets via stratified conditional rollouts to enable reference-relative contrastive comparisons.
- The projection head is frozen during policy optimization while alignment scores define contrastive advantages within each group.
- RRPO achieves gains over weakly supervised baselines and improves after supervised fine‑tuning without needing task ground‑truth verifiers.

## Context
Group relative methods like GRPO rely on verifier signals that are limited to verifiable tasks. This paper addresses the gap by using reference contrastive learning, which is more flexible for open‑ended generation and post‑SFT scenarios where single correctness measures fail.

## Implications
RRPO offers a scalable framework for RL optimization in domains lacking reliable feedback, enabling practitioners to apply group relative techniques broadly. The approach reduces reliance on expensive verifiers and can be integrated into existing pipelines with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18470v1)
