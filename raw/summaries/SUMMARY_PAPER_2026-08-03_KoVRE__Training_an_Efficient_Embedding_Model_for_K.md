---
title: KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval
url: http://arxiv.org/abs/2608.01389v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_17-11-09Z_KoVRE_TraininganEfficientEmbeddingModelforKoreanVi.md
generated_at: 2026-08-03 23:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KoVRE, a single-vector embedding model for Korean visual document retrieval that improves over existing English-centric systems. It achieves strong performance on Korean benchmarks without using large backbones or multi‑vector representations. The 2B model outperforms its larger counterpart and a multi‑vector baseline.

## Key Takeaways
- KoVRE uses positive‑aware hard‑negative mining to train a single‑vector retriever on 708,729 Korean and English query‑page pairs, focusing training data composition and hard‑negative treatment. - The model’s architecture is lightweight (2B parameters) yet surpasses an 8B single‑vector version and a strong multi‑vector baseline, showing that efficient design can match larger models. - Controlled analyses reveal that bilingual supervision and careful negative sampling are essential for high performance across diverse document domains.

## Context
Visual Document Retrieval aims to preserve visual information when matching queries to images, yet most resources focus on English text. This work addresses the gap by creating a Korean‑focused dataset and training pipeline, demonstrating that domain‑specific models can be effective without massive compute or storage.

## Implications
For practitioners, KoVRE shows that targeted bilingual supervision and efficient training strategies can yield high‑quality retrieval systems for under‑served languages. It encourages industry to prioritize multilingual data curation over scaling backbones, reducing cost while maintaining performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01389v1)
