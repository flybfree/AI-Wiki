---
title: Teach Yourself Where to Look: On-Policy Attention Self-Distillation for Reasoning
published: 2026-09-27T04:38:41Z
authors: Safaeid Hossain Arib, Rabeya Akter, Ismam Nur Swapnil, Md. Faiyaz Abdullah Sayeedi, Md Mofijul Islam, Tasnim Mohiuddin
url: http://arxiv.org/abs/2609.33200v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teach Yourself Where to Look: On-Policy Attention Self-Distillation for Reasoning

## Abstract
On-policy self-distillation trains reasoning models on their own trajectories using dense token distribution guidance from a privileged teacher with access to a verified solution. This supervision transfers what the teacher predicts without directly transferring where it attends within the preceding context. We introduce On-Policy Attention Self-Distillation (OPASD), which complements token-level supervision with solution-conditioned attention distillation. Because the privileged teacher can attend to verified solution tokens unavailable to the student, OPASD projects teacher attention onto student-visible positions and renormalizes the resulting distribution before alignment. Across three model sizes and four competition-level mathematics benchmarks, OPASD consistently outperforms token-only OPSD, improving average accuracy by 4.98 to 8.40 percentage points. OPASD also avoids the response-length inflation and performance degradation observed with token-only distillation, reducing generated rollout tokens by 73.9% and estimated model compute by 72.6% while training 1.53x faster. These results show that solution-conditioned attention provides a complementary supervision signal that makes on-policy self-distillation more accurate, stable, and compute-efficient.

## Metadata
- **Published**: 2026-09-27T04:38:41Z
- **Authors**: Safaeid Hossain Arib, Rabeya Akter, Ismam Nur Swapnil, Md. Faiyaz Abdullah Sayeedi, Md Mofijul Islam, Tasnim Mohiuddin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33200v1)