---
title: CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding
url: http://arxiv.org/abs/2607.24582v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_15-49-42Z_CADER_Confidence_AwareDynamicEvidenceReasoningforL.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
CADER introduces a training‑free framework that adapts long‑video reasoning based on answer confidence. It uses a logit‑margin signal to allow high‑confidence examples to exit early, while uncertain cases trigger a second‑stage tool‑augmented loop. Experiments demonstrate improved performance and efficient inference.

## Key Takeaways
- CADER estimates answer confidence using a logit‑margin signal to enable early exit for high‑confidence examples, reducing unnecessary processing.
- For uncertain examples it activates a second‑stage tool‑augmented loop that combines temporal cropping, semantic verification and relevance‑guided resampling to locate evidence.
- Experiments show CADER improves long‑video reasoning while avoiding extra tool use on easy cases.

## Context
Long‑video understanding increasingly depends on vision‑language models that perform uniform inference across all queries. This uniformity leads to wasteful tool usage for simple questions and limited control over complex temporal evidence. Adaptive methods like CADER address these inefficiencies by tailoring reasoning effort per example.

## Implications
By treating tool use as a sample‑level decision, CADER offers a practical inference‑time route that can be integrated into existing models without retraining. This reduces computational cost, enables scalable deployment, and makes long‑video reasoning more reliable for industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24582v1)
