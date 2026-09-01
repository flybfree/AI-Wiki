---
title: Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines
url: http://arxiv.org/abs/2608.29589v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_06-19-46Z_NotSafeforAll_AuditingtheDialectPenaltyinText_to_I.md
generated_at: 2026-08-31 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how text-to-image safety filters misclassify prompts from non‑standard English dialects, calling this bias the dialect penalty. It finds that NSFW‑T over‑flags benign dialect prompts while LatentGuard under‑flags toxic ones, creating large bias gaps up to 28.3 pp. The root cause is linguistic surface features rather than semantic content.

## Key Takeaways
- Text‑level filters trigger on dialectal phonological cues, leading to opposite misclassifications for benign versus toxic prompts.
- The OpenAI Moderation API under‑detects these dialect prompts, widening the bias gap and indicating a systemic equity failure in current pipelines.
- Balanced exposure through group‑balanced retraining improves performance, showing that the deficit is tied to data imbalance rather than the worst‑group objective of GroupDRO.

## Context
Safety guardrails for generative AI are designed to protect users from harmful content, yet they often perform poorly across linguistic variations. This paper highlights a specific fairness gap where dialects—historically underrepresented in training data—are penalized or mislabeled, revealing a broader issue of algorithmic bias that can marginalize speakers of non‑standard English.

## Implications
For developers and researchers, the findings stress the need for equitable evaluation across all linguistic variants before deploying safety systems. Ignoring dialectal performance can lead to real‑world exclusion of users who speak differently but are not inherently harmful, undermining trust in AI services that claim neutrality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29589v1)
