---
title: Rethinking On-Policy Self-Distillation for Thinking Models
url: http://arxiv.org/abs/2607.05184v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-06_15-01-35Z_RethinkingOn_PolicySelf_DistillationforThinkingMod.md
generated_at: 2026-07-23 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the impact of privileged self‑distillation on thinking language models, showing that providing model‑specific solutions during training can harm performance on long reasoning tasks. Across Qwen3 and OLMo variants evaluated on AIME24–AIME25 and HMMT25, adding privileged context reduces average accuracy by up to 17% when rollout budgets are extended. The degradation is linked to altered learning at high‑entropy forking positions where multiple continuations remain plausible.

## Key Takeaways
- Privileged self‑distillation causes a relative drop of up to 17% in avg@16 accuracy across five thinking models, especially noticeable on long rollout budgets.  
- The effect stems from privileged teacher context reshaping learning at high‑entropy forking positions, lowering fork rates but not affecting instruction‑model rollouts.  
- Training with a privileged teacher reduces verification, backtracking, and hedging markers in the student’s output even after length normalization.

## Context
Self‑distillation is widely used to improve language models by letting them teach themselves using internal knowledge. Thinking models aim to leverage test‑time reasoning as a form of privileged information, but this study reveals that such assistance can be counterproductive when it interferes with the model’s ability to explore diverse reasoning paths.

## Implications
Practitioners must consider token‑level signals during self‑distillation, particularly around correction and backtracking steps. Ignoring these nuances may degrade performance on complex reasoning benchmarks, prompting a need for more refined distillation strategies that preserve flexibility in thinking models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.05184v1)
