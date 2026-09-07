---
title: What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection
url: http://arxiv.org/abs/2609.05198v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_14-32-08Z_WhatMattersinOn_PolicyDistillation_APerspectiveonD.md
generated_at: 2026-09-06 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper examines how data efficiency and choice affect on‑policy distillation (OPD) for large language models in reasoning tasks. It shows that training OPD on a single example can still yield strong improvements, especially when the examples are hard or generate long chain‑of‑thought paths.

## Key Takeaways
- 1‑shot OPD is consistently effective across all sampled training examples and harder examples often provide superior performance gains.
- The student’s improvement is driven by longer CoT reasoning rather than high token entropy, allowing it to capture critical thinking patterns like reflection that short CoTs miss.
- Training on only eight selected hard examples can match the performance of a 17 K‑example baseline across models from 1.5B to 7B.

## Context
On‑policy distillation is increasingly used to fine‑tune large language models without full retraining, but its reliance on data quality and quantity remains unclear. This study bridges that gap by empirically linking data selection to reasoning performance in a minimal dataset setting.

## Implications
Practitioners can achieve high accuracy with far fewer training examples by focusing on hard, long CoT questions rather than volume. This approach reduces computational cost and enables efficient fine‑tuning of models across various sizes and domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05198v1)
