---
title: Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See
url: http://arxiv.org/abs/2608.17744v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_13-09-03Z_ThinkinginaLow_ResourceLanguage_WhatSFTBuilds_What.md
generated_at: 2026-08-18 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates how fine‑tuning (SFT) and reinforcement learning (RL) affect mixture‑of‑experts models when reasoning in a low‑resource language such as Greek. It finds that SFT dramatically improves surface‑level performance while RL further refines the model’s internal behavior, yet accuracy benchmarks remain largely unchanged.

## Key Takeaways
- Fine‑tuned checkpoints answer correctly on ~98% of items even though their reasoning traces are unreadable to humans, indicating progress where human assessment cannot see.  
- RL with pre‑registered verifiable rewards reduces format skips and leakage dramatically (24% → 2.5% and 3.5% → 0.0%) compared to a flat random reward baseline.  
- Despite these gains, an explicit “think in English” instruction is obeyed only half the time, showing that RL cannot fully eliminate the model’s native language bias.

## Context
The study highlights a gap between surface metrics and deeper model behavior in low‑resource settings where data are scarce and benchmark noise dominates. It underscores the need for evaluation tools that capture internal reasoning dynamics beyond simple accuracy scores.

## Implications
For practitioners, this work suggests that RL can be a powerful complement to SFT when fine‑tuning models for multilingual tasks, but it cannot eliminate inherent language preferences without careful reward design. The findings push the field toward more holistic assessments of model behavior in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17744v1)
