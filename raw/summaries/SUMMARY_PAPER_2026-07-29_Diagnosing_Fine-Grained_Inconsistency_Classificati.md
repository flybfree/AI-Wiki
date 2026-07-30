---
title: Diagnosing Fine-Grained Inconsistency Classification in Financial Disclosure Text
url: http://arxiv.org/abs/2607.26368v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_01-03-53Z_DiagnosingFine_GrainedInconsistencyClassificationi.md
generated_at: 2026-07-29 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses fine-grained inconsistency classification in financial disclosure texts by comparing various models on a benchmark with eleven labels and paired evidence spans. It finds that a fine-tuned encoder achieves 61.9% accuracy, surpassing LoRA‑adapted Qwen3.5 and GPT‑5.4, and highlights the importance of high-quality evidence localization.

## Key Takeaways
- The fine‑tuned encoder’s performance is driven more by accurate evidence spans than model scale, reaching 61.9% accuracy versus 61.5% for a larger LoRA‑adapted model.
- Automatically predicted evidence spans recover only part of the gain from gold spans, showing that localization quality remains a bottleneck in classification.
- Class analyses reveal referential inconsistencies are most affected by poor localization, while factual and logical inconsistencies remain hard even with correct evidence.

## Context
Financial disclosure analysis relies on detecting conflicts between numerical claims, temporal statements, entity references, policy commitments, and risk descriptions. Current approaches often treat inconsistency detection as a binary task, overlooking the need to classify subtle types that require different evidential support.

## Implications
Improving fine‑grained classification will enable more precise downstream checks such as compliance audits and risk assessment. The findings suggest that compact supervised encoders can be effective if paired with robust evidence extraction pipelines, guiding future research toward hybrid models that combine embedding power with high-quality localization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26368v1)
