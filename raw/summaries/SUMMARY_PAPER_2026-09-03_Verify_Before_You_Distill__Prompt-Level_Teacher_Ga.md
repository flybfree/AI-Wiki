---
title: Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation
url: http://arxiv.org/abs/2609.02998v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_17-54-09Z_VerifyBeforeYouDistill_Prompt_LevelTeacherGatingfo.md
generated_at: 2026-09-03 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Teacher-Gated On-Policy Distillation (TGOPD) to improve on-policy distillation by verifying teacher reliability at the prompt level before applying dense supervision. Experiments show TGOPD outperforms vanilla OPD across multiple domains and scales, while also reducing compute waste for the teacher.

## Key Takeaways
- TGOPD checks each prompt with a verifier-scored probe to decide whether to use dense OPD or verifier-grounded GRPO, directly addressing mode-seeking errors from unreliable teachers.
- Reliability verification reduces teacher-side compute waste, raising GPU utilization from 9.8% to 78.9% in a single-domain run, showing efficient use of otherwise-idle capacity.
- The method yields higher seven-benchmark averages for both 4B and 35B students in mathematics, code, and instruction following, outperforming vanilla OPD in all six single-domain settings.

## Context
On-policy distillation aims to compress large language models by leveraging teacher outputs on student rollouts. Existing methods treat supervision uniformly, ignoring prompt-specific reliability, which can propagate incorrect guidance. This work introduces a prompt-level verification mechanism that aligns with the need for domain-aware model training.

## Implications
For practitioners, TGOPD offers a practical way to enhance distillation quality without extra compute from the teacher, improving resource efficiency in large-scale AI systems. The approach could be adopted across domains where reliable teacher outputs are critical, such as medical or legal instruction following, and may inform future self-supervised learning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02998v1)
