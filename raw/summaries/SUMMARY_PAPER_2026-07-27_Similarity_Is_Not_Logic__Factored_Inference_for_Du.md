---
title: Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models
url: http://arxiv.org/abs/2607.23052v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_05-39-51Z_SimilarityIsNotLogic_FactoredInferenceforDual_Enco.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses a fundamental flaw in dual-encoder vision-language models where their similarity interface ignores logical operators, causing queries such as “umbrella and no person” to retrieve images that contain both objects. By analyzing the Bag-of-Concepts effect, it shows that similarity scores are computed as mean‑pooled concept evidence rather than respecting relational constraints. The authors introduce factored inference and a training‑free method LCSE (Logic‑Constrained Score Editing) that applies constraints externally to frozen encoder outputs, achieving substantial gains over fine‑tuned baselines.

## Key Takeaways
- The similarity interface treats all concepts independently, leading to compositional violations when logical operators are present.  
- Fine‑tuning the encoders does not fix the problem because the bottleneck lies in how evidence is aggregated rather than what is represented.  
- LCSE separates evidence extraction from constraint execution and can boost retrieval accuracy by up to 90.7% on SigLIP 2 while improving NegBench COCO MCQ performance.

## Context
Dual‑encoder vision-language models are widely used for zero‑shot image retrieval, yet their similarity mechanisms often ignore the logical structure of natural language queries. This limitation hampers applications that require precise reasoning about object co‑occurrence or absence. The paper contributes a principled way to enforce these constraints without retraining the encoders.

## Implications
For practitioners building VLMs, this work shows that improving retrieval quality can be achieved by decoupling constraint application from encoder updates, reducing reliance on costly fine‑tuning pipelines. It also demonstrates measurable gains in benchmark tasks, suggesting that factored inference could become a standard component of multimodal systems aiming for reliable zero‑shot performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23052v1)
