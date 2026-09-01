---
title: MMDS-Bench: Benchmarking Multimodal Large Language Models on Dynamic Stance in Social Media Interactions
url: http://arxiv.org/abs/2608.30903v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_14-53-08Z_MMDS_Bench_BenchmarkingMultimodalLargeLanguageMode.md
generated_at: 2026-08-31 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MMDS-Bench as a benchmark for multimodal dynamic stance classification in social media parent‑reply interactions and evaluates twelve large language models on it. It finds that current models still struggle with relational inference beyond separate comprehension of the parent and reply.

## Key Takeaways
- The dataset includes 3,482 instances annotated with seven labels and an 800‑instance diagnostic subset requiring structured reasoning.
- Five challenge factors are annotated: multimodal fusion, parent framing, non‑literal expression, interaction reasoning, and label‑boundary ambiguity.
- Evaluation shows LLMs perform poorly on relational inference tasks.

## Context
Social media interactions increasingly involve images, memes, and reaction graphics that affect how replies relate to their parents. Prior benchmarks focus on text‑only settings, leaving a gap for multimodal stance understanding.

## Implications
This work highlights the need for models that can integrate visual cues with textual context to capture dynamic relational stances. Practitioners should prioritize multimodal reasoning in social media analytics and content moderation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30903v1)
