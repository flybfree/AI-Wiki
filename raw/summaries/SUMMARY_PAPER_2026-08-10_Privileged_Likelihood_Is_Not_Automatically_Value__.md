---
title: Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.09263v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-18-48Z_PrivilegedLikelihoodIsNotAutomaticallyValue_ThreeC.md
generated_at: 2026-08-10 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether token likelihood changes in on-policy self-distillation automatically translate into outcome credit, finding that they do not; it introduces three checks to separate the issues of action tracking, feedback construction dependence, and training loss reinforcement.

## Key Takeaways
- The additive score derived from token likelihood change is near chance (AUC=0.505) on AIME 2025 with a 20B model, indicating it does not reliably improve trace quality.
- Using hindsight feedback written about the same rollout creates direct self‑dependence between tokens and scoring context, which undermines usefulness; using feedback from another rollout removes this dependence but still yields only modest improvement (64.2% vs 24.2–33.9%).
- The results show that outcome‑only control records 64.2%, while five token‑score variants fall between 24.2% and 33.9%, highlighting the need to validate score meaning, feedback construction, and training behavior separately.

## Context
Self‑distillation aims to improve model reasoning by re‑scoring its own rollouts with training‑only information, but existing methods often treat token likelihood changes as a proxy for better performance without evidence. This work formalizes three distinct questions that must be answered before trusting such scores.

## Implications
Practitioners should not assume that any change in token likelihood signals improved reasoning; instead they must rigorously check whether the score aligns with actual behavior, how feedback is constructed, and what training dynamics are reinforced. Ignoring these factors can lead to near‑chance performance, wasting compute and misleading model evaluation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09263v1)
