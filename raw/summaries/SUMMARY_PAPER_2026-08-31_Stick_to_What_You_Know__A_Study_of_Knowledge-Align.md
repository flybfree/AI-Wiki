---
title: Stick to What You Know: A Study of Knowledge-Aligned Supervised Fine-Tuning
url: http://arxiv.org/abs/2608.30987v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_15-43-51Z_SticktoWhatYouKnow_AStudyofKnowledge_AlignedSuperv.md
generated_at: 2026-08-31 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how supervised fine‑tuning (SFT) can generate hallucinations when the training targets contain knowledge that a base language model does not robustly internalize. It proposes knowledge‑aligned SFT, which restricts SFT targets to the model’s existing parametric knowledge and introduces two new methods: Evidence Rewrite and Recall Rewrite.

## Key Takeaways
- Knowledge‑aligned SFT reduces factual hallucinations by limiting training data to what the base model already knows, as demonstrated on WildHalu and Biography datasets.  
- Evidence Rewrite verifies base‑model generations using external evidence, while Recall Rewrite retains claims only when they can be consistently recalled by the base model.  
- Both methods preserve general language capabilities but improve factuality, with Recall Rewrite yielding the strongest gains.

## Context
The proliferation of large language models has made SFT a standard fine‑tuning technique, yet persistent hallucinations arise from knowledge gaps between training data and model parameters. This work addresses those gaps by aligning training targets with the model’s internal representation.

## Implications
Knowledge‑aligned SFT offers a practical way to mitigate factual errors in deployed models without full retraining. Practitioners can adopt these methods to enhance reliability, especially for applications demanding strict factual consistency such as biographies or fact‑checking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30987v1)
