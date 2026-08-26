---
title: Scalable Question-Centric Text-to-Image Evaluation: Reliable Ranking, Fine-Grained Diagnosis, and Cost-Aware Routing
url: http://arxiv.org/abs/2608.24112v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_06-20-18Z_ScalableQuestion_CentricText_to_ImageEvaluation_Re.md
generated_at: 2026-08-25 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes QC‑T2I‑Bench, a framework that treats open text‑to‑image prompts as a set of atomic questions linked by a scene graph structure, enabling fine‑grained evaluation. It shows that joint completion drops sharply when many capabilities are required and provides reliable ranking with detailed failure diagnosis.

## Key Takeaways
- The question‑centric design separates basic realization failures from complex compositional failures, allowing precise diagnosis.
- Hierarchy‑constrained aggregation prevents simple and complex prompts from being weighted equally, improving ranking reliability.
- A cost‑aware router matches ERNIE’s performance while using 21.3 % less GPU/MP resources.

## Context
Current T2I evaluation often aggregates scores into a single metric, obscuring which sub‑tasks fail and making model selection subjective. Question‑centric benchmarks have been limited to returning prompts to scores or fixed categories, reducing attribution value.

## Implications
This work offers practitioners a tool to diagnose specific prompt weaknesses without retraining models. The cost‑aware routing can lower inference expenses for large‑scale deployment, encouraging more efficient use of generative AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24112v1)
