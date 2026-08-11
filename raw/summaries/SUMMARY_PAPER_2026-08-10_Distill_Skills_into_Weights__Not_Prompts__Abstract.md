---
title: Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation
url: http://arxiv.org/abs/2608.09826v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_16-43-18Z_DistillSkillsintoWeights_NotPrompts_AbstractSkills.md
generated_at: 2026-08-10 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SKALD, an on-policy self-distillation method that leverages abstract skill cards to improve reinforcement learning performance when group-relative rewards are uninformative. By training a student model on its own prefixes while using teacher-preferred tokens as privileged signals, SKALD recovers substantial gains over GRPO across mathematics benchmarks.

## Key Takeaways
- The paper demonstrates that group-relative rewards are often uniformly correct or wrong (63–68% of groups), rendering them useless for distillation.
- SKALD uses two context views—question-only student and teacher conditioned on an explicit skill card—to transfer skill advantage without privileged input at test time, stabilizing distribution mismatch with an annealed tilt objective.
- Empirically, SKALD improves avg@8 by 2.46–12.01 over FLOP-matched GRPO, recovers most of the gain even in zero-variance-only distillation, and outperforms contextual skill exposure.

## Context
This work addresses a key limitation in RL with verifiable rewards: when rollout groups are homogeneous, they provide no relative signal for learning. The proposed framework shows that abstract, explicit skill annotations can serve as dense supervision, enabling more effective model self-distillation without relying on noisy reward gradients.

## Implications
For practitioners, SKALD offers a practical way to enhance RL models using lightweight, human‑curated skill cards, reducing reliance on high‑cost reward calibration. It also suggests that abstract supervision could be generalized across domains where reward signals are ambiguous or unreliable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09826v1)
