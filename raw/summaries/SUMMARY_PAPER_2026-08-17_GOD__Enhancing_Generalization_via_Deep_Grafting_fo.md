---
title: GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation
url: http://arxiv.org/abs/2608.16073v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_04-11-49Z_GOD_EnhancingGeneralizationviaDeepGraftingforSeque.md
generated_at: 2026-08-17 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GOD, a component-level knowledge distillation method that replaces selected frozen teacher components with trainable student counterparts to improve generalization for sequential recommendation. By using hybrid models for bidirectional feedback, GOD reduces the entanglement of supervision and achieves up to 13.92% improvement over state-of-the-art baselines across three real-world datasets.

## Key Takeaways
- Knowledge distillation usually runs teacher and student independently then matches outputs, which entangles student-component effects and blurs whether weak generalization stems from unreliable embeddings or overfitted encoding.
- Grafting denotes replacing selected frozen-teacher components with trainable student counterparts to build hybrid source models that provide component-level feedback.
- At inference, GOD uses only the trained student model, incurring no additional cost while leveraging teacher and student representations for evaluation.

## Context
In sequential recommendation systems, user histories are often sparse and noisy, making it difficult to generalize to new interactions. Traditional distillation approaches treat teacher and student as independent models, which can obscure whether poor performance stems from unreliable embeddings or overfitted encoders. This paper addresses these limitations by providing component-level insights.

## Implications
For practitioners, GOD offers a way to enhance model robustness without increasing inference latency, as only the trained student is used at runtime. The method could lead to more reliable recommendations in domains where data scarcity is common, such as early-stage e‑commerce or healthcare platforms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16073v1)
