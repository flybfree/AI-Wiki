---
title: When Does Knowledge Distillation Hurt? Reliability-Aware Distillation for Low-Resource Language Summarization
url: http://arxiv.org/abs/2607.19956v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_09-32-28Z_WhenDoesKnowledgeDistillationHurt_Reliability_Awar.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when knowledge distillation harms model performance in low-resource language summarization, finding that standard KD often degrades validation loss and only modestly improves ROUGE-L. It introduces two reliability-aware methods CHAD and EWAD+CPDP that outperform baseline by significant margins despite small parameter budgets.

## Key Takeaways
- Standard knowledge distillation on BanSum Bangla yields a negligible ROUGE-L gain of +0.0003 while approximately 51.3% of training samples increase validation loss, indicating harmful per-sample effects.
- The proposed CHAD method uses gradient alignment to detect harmful samples and applies a lightweight gate that generalizes this judgment across the full dataset, achieving +0.0173 ROUGE-L improvement.
- EWAD+CPDP combines entropy-weighted adaptive distillation with a capacity-proportional geometric constraint from a second teacher, delivering +0.0219 ROUGE-L and outperforming a 50x larger Qwen 2.5-3B model.

## Context
Knowledge distillation remains a common technique for compressing large language models but often neglects per-sample impact on downstream validation metrics. This work addresses the gap by quantifying harmful samples and offering methods that balance compression with reliability, especially in low-resource settings where teacher coverage is limited.

## Implications
For practitioners, these findings suggest that blindly applying KD can waste resources and degrade performance, prompting a shift toward reliability-aware training pipelines. The results also highlight the value of multi-teacher distillation in bridging language gaps, offering scalable solutions for multilingual summarization tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19956v1)
