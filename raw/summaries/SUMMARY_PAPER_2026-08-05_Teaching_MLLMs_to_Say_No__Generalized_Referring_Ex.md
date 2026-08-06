---
title: Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO
url: http://arxiv.org/abs/2608.04698v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_11-07-22Z_TeachingMLLMstoSayNo_GeneralizedReferringExpressio.md
generated_at: 2026-08-05 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Refusal-Calibrated Group Relative Policy Optimization (RC‑GRPO) to improve Generalized Referring Expression Comprehension in MLLMs by balancing positive localization and negative refusal. Experiments show that RC‑GRPO maintains high accuracy on existing objects while reliably refusing nonexistent ones, outperforming prior methods.

## Key Takeaways
- The model enforces "None" outputs during rollouts to ensure accurate advantage estimation for negative samples, preventing hallucinated bounding boxes.
- A penalty is applied to avoid over‑refusing positive samples, preserving localization performance.
- A second‑stage reasoning reinforcement step further enhances causal understanding and interpretability.

## Context
Generalized Referring Expression Comprehension remains a critical benchmark for multimodal models because it tests both object detection and safe refusal. Current approaches often sacrifice one aspect for the other, limiting real‑world applicability where correct negation is essential.

## Implications
This work provides a framework that can be adapted to other safety‑critical tasks requiring dual positive/negative responses. Practitioners can leverage RC‑GRPO to deploy MLLMs with reliable grounding and safe behavior without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04698v1)
