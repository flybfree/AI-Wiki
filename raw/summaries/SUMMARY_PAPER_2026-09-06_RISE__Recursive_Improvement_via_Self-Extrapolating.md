---
title: RISE: Recursive Improvement via Self-Extrapolating Policy Distillation
url: http://arxiv.org/abs/2609.05295v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_15-47-51Z_RISE_RecursiveImprovementviaSelf_ExtrapolatingPoli.md
generated_at: 2026-09-06 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper RISE (Recursive Improvement via Self‑Extrapolating Policy Distillation) introduces a method that creates an internal teacher from the model’s own training trajectory, enabling dense token‑level supervision without external models or privileged conditioning. By extrapolating displacement between checkpoints in parameter space or logit space, RISE turns sparse outcome rewards into fine‑grained guidance. Experiments show RISE beats both RLVR‑only and on‑policy self‑distillation across reasoning, STEM, code, and agentic tasks.

## Key Takeaways
- RISE builds a synthetic teacher directly from the model’s own RLVR trajectory, eliminating reliance on external teachers or privileged conditioning. 
- The method extrapolates displacement between current checkpoint and trailing anchor to convert sparse updates into dense token targets. 
- Distillation is recursive because the teacher is refreshed each iteration as the student improves.

## Context
Current language model training often relies on external teacher models that suffer from distribution mismatch, limiting the utility of on‑policy distillation. Self‑distillation methods are hampered by limited in‑context learning capacity. RISE addresses these bottlenecks by generating a high‑quality internal teacher and integrating it with reinforcement learning via outcome rewards.

## Implications
For practitioners, RISE offers a scalable way to improve model performance without costly external resources or complex conditioning. In industry, this could accelerate fine‑tuning pipelines and reduce compute overhead for downstream reasoning tasks. The recursive improvement loop suggests future work on continual self‑optimization of large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05295v1)
