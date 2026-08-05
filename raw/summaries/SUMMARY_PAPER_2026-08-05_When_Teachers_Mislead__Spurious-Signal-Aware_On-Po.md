---
title: When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation
url: http://arxiv.org/abs/2608.03632v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-17-30Z_WhenTeachersMislead_Spurious_Signal_AwareOn_Policy.md
generated_at: 2026-08-05 01:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper addresses a critical flaw in on‑policy distillation where teacher signals can be misleading and not grounded to the input. The authors introduce SA‑OPD, which filters out such spurious updates and shows it beats vanilla OPD and other selective methods across language and vision‑language tasks.

## Key Takeaways  
- Spurious signals arise from token‑level judgments that depend on language priors or formatting rather than task evidence, leading to large gradients with little improvement.  
- SA‑OPD estimates an input‑groundedness proxy to detect whether a distillation signal truly reflects the input and removes tokens with high divergence but low ground‑ing.  
- Experiments demonstrate consistent gains in model performance, establishing input‑groundedness as essential for selecting useful supervision.

## Context  
Language model training often relies on teacher feedback that may not align with task relevance, causing inefficient or harmful updates. Selective distillation aims to improve this by focusing on high‑impact signals, but existing methods ignore the possibility of input‑agnostic noise. This work fills that gap by introducing a principled filter based on groundedness.

## Implications  
Practitioners can adopt SA‑OPD to reduce wasted gradient computation and improve model robustness across diverse tasks. The framework offers a simple yet effective way to ensure that distillation guidance is truly task‑relevant, benefiting both research and industry applications of large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03632v1)
