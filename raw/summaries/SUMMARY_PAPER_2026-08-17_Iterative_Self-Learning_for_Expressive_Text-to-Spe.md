---
title: Iterative Self-Learning for Expressive Text-to-Speech Synthesis
url: http://arxiv.org/abs/2608.15910v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_19-54-20Z_IterativeSelf_LearningforExpressiveText_to_SpeechS.md
generated_at: 2026-08-17 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an Iterative Self-Learning (ISL) framework for expressive text-to-speech that recovers discrete expressive labels from unlabeled speech using a classifier‑free inversion method. By iteratively generating pseudo‑labels, training on the combined labeled and pseudo‑labeled data, and repeating, the model improves both label accuracy and synthesis quality. Experiments show that ISL outperforms single‑pass baselines and approaches fully supervised performance even with very few expressive labels.

## Key Takeaways
- The framework recovers discrete expressive labels from unlabeled speech using a classifier‑free inversion of a frozen generative model, eliminating the need for manual labeling.
- Iterative refinement of pseudo‑labels leads to higher label accuracy compared with single‑pass pseudo‑labeling baselines.
- Improvements in pseudo‑label quality translate into better adherence to expressive constraints and higher synthesis quality as measured by objective metrics and human listening tests.

## Context
Expressive TTS aims to produce speech that reflects linguistic or emotional attributes, but obtaining high‑quality labels at scale is a bottleneck. Most semi‑supervised methods target data scarcity of paired speech‑text pairs rather than the lack of expressive annotations, limiting their applicability to tasks requiring fine control over voice qualities.

## Implications
This work provides a practical path to scalable expressive TTS without costly label collection, enabling developers to deploy models that can be tuned on limited labeled corpora. Practitioners can leverage ISL to improve model robustness and user satisfaction in applications where expressive control is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15910v1)
