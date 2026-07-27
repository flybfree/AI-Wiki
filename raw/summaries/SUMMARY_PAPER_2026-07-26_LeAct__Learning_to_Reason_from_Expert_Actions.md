---
title: LeAct: Learning to Reason from Expert Actions
url: http://arxiv.org/abs/2607.21856v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_22-50-23Z_LeAct_LearningtoReasonfromExpertActions.md
generated_at: 2026-07-26 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LeAct, a method for extracting natural‑language reasoning traces from expert system actions in games and robotics benchmarks. By treating the hidden CoT as a latent variable, LeAct samples candidate reasoning chains and selects those that boost the student’s action prediction accuracy, achieving performance on par with the solver on small enumerable games and significantly outperforming baselines on larger problems.

## Key Takeaways
- LeAct recovers the implicit chain‑of‑thought from expert actions by optimizing a latent variable rather than relying on explicit annotations.  
- The approach improves action prediction by five times compared to the strongest expert‑iteration baseline, reaching the solver’s numerical floor in small games and gaining +60 mbb/g at Flop Hold’em.  
- In robotics simulations, LeAct is the only training recipe that yields gains over direct imitation learning.

## Context
Modern foundation models rely on human‑annotated reasoning data or distillation from stronger LLMs, yet expert systems generate high‑quality actions without providing explicit reasoning traces. This paper demonstrates how to leverage these silent experts as a new source of supervision for AI agents.

## Implications
LeAct opens the door to training foundation models with richer, domain‑specific knowledge that can generalize beyond narrow datasets. Practitioners may integrate expert‑derived CoTs into their pipelines to boost performance in games, planning, and robotics without costly annotation efforts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21856v1)
