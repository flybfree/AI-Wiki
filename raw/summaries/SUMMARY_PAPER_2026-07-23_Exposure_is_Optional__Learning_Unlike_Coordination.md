---
title: Exposure is Optional: Learning Unlike Coordination in Language Models
url: http://arxiv.org/abs/2607.20251v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_15-11-11Z_ExposureisOptional_LearningUnlikeCoordinationinLan.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether language models need direct exposure to unlike coordination in training data and finds they can generalize using only alike coordination. It uses filtered corpora without unlike examples and shows models still handle unlike coordination with comparable perplexity and grammaticality scores. The experiments also reveal that the models' ability to handle unlike coordination is robust across different filterings of the training corpus.

## Key Takeaways
- Direct exposure to unlike coordination is unnecessary; models trained on filtered data (no unlike examples) still generalize to unlike coordination, achieving similar perplexity and grammaticality scores.
- Internal representations treat conjoined elements as belonging to similar structural categories or via a deletion-like mechanism that can be learned from alike coordination alone.
- This demonstrates language models' ability to learn compositional patterns without explicit exposure, challenging the view that unlike coordination requires specific training.

## Context
Language model research often assumes that complex linguistic structures require direct examples in data. This study challenges that by showing emergent abilities can arise from general compositional learning, adding to debates on how models capture syntax and semantics.

## Implications
For practitioners, the results imply that improving model performance may focus on enhancing exposure to diverse syntactic patterns rather than forcing explicit training of rare structures. It also suggests internal mechanisms like category alignment are learnable, guiding future interpretability efforts. This insight could inform curriculum design for larger language models, encouraging richer exposure to varied syntactic structures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20251v1)
