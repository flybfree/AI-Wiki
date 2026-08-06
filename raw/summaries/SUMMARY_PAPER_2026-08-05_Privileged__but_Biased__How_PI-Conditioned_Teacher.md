---
title: Privileged, but Biased: How PI-Conditioned Teachers Break Self-Distillation
url: http://arxiv.org/abs/2608.04794v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_12-59-10Z_Privileged_butBiased_HowPI_ConditionedTeachersBrea.md
generated_at: 2026-08-05 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether self‑distillation (SD) can improve reasoning performance beyond narrow, low‑difficulty gains reported in prior work. The authors reproduce SDPO’s easy‑task results but find that validation accuracy does not increase and often degrades on difficult tasks across multiple domains.

## Key Takeaways
- PI bias pulls the teacher's per‑token target toward a specific reference solution rather than toward general correctness, creating a systematic misalignment between loss signals and task success.  
- The student learns to match this biased target everywhere, causing the loss to focus on low‑information tokens such as stopwords, punctuation, and uncertainty markers instead of those that determine answers.  
- Exploration tokens incur the highest divergence, so the model penalizes the hesitation required for reasoning, resulting in a flatter, less decisive student.

## Context
Self‑distillation is promoted as a compute‑efficient alternative to reinforcement learning with verifiable rewards, allowing models to learn from dense supervision without external reward terms. This paper challenges that optimism by showing its limitations when applied broadly across task difficulty and modalities.

## Implications
If SD optimizes only a signal decoupled from task success, practitioners should treat it as an auxiliary objective rather than the primary driver of model performance. Better PI design or combined loss functions may be needed to harness its efficiency without sacrificing reasoning quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04794v1)
