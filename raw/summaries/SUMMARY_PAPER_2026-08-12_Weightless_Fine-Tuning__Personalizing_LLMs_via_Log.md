---
title: Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport
url: http://arxiv.org/abs/2608.11342v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_18-49-03Z_WeightlessFine_Tuning_PersonalizingLLMsviaLogit_Sp.md
generated_at: 2026-08-12 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Weightless Fine-Tuning, a method that adapts large language models to personal preferences without updating model weights or performing retraining. The authors demonstrate that WFT can match or exceed supervised fine‑tuning performance on three LaMP benchmarks while using less than 7% of the effective computation. Logit‑level analysis shows an 0.875 cosine similarity between logit shifts, indicating strong distributional alignment.

## Key Takeaways
- Weightless Fine-Tuning replaces gradient updates with logit‑space corrections computed from dropout‑induced cross‑covariance, enabling training‑free personalization.
- The method achieves the best average performance across three LaMP datasets and matches or exceeds SFT on individual tasks, outperforming lightweight baselines.
- Logit‑level analysis reveals a cosine similarity of 0.875 between WFT and SFT logit shifts over 95% of next‑token probability mass.

## Context
Personalization of large language models is essential for user‑specific experiences but traditionally requires costly weight updates and retraining. This work offers a lightweight alternative that can be applied at inference time, reducing computational overhead while preserving adaptation quality.

## Implications
For industry practitioners, WFT lowers the barrier to deploying personalized AI services without heavy infrastructure changes. Practitioners can implement personalization quickly, saving resources and enabling rapid iteration across user groups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11342v1)
