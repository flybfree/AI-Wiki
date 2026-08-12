---
title: MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models
url: http://arxiv.org/abs/2608.10635v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-22-13Z_MedUP_AwakeningUnifiedUnderstandingandPerceptionin.md
generated_at: 2026-08-11 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MedUP, a unified medical vision‑language model that integrates visual perception and textual understanding into a single shared token space. By using the UniMedTok tokenizer to embed region masks as discrete tokens alongside text, MedUP eliminates representation gaps between segmentation and language generation. Experiments show MedUP outperforms native, agentic, and dual‑decoder approaches across all tasks while staying competitive with specialist segmentors.

## Key Takeaways
- The UniMedTok tokenizer creates a unified vocabulary where mask tokens are interleaved with textual tokens, allowing the model to process perception and understanding simultaneously.
- The curated UniMed‑Train corpus of 1.84 million instances spans text‑guided segmentation, region‑grounded understanding, medical VQA, and CoT‑based segmentation, providing diverse training signals for a single model.
- Unified evaluation on UniMed‑Bench demonstrates that MedUP achieves the best performance across all tasks, highlighting the advantage of native perception‑understanding modeling.

## Context
Current Med-VLMs either separate visual analysis from language output or rely on external modules, which introduces alignment problems. This work addresses those gaps by embedding both modalities in one model, reflecting a broader trend toward multimodal foundation models that aim for seamless cross‑modal reasoning.

## Implications
For medical AI practitioners, MedUP offers a ready‑to‑use framework that reduces the need to stitch together separate segmentation and language components. The unified approach can lead to more accurate diagnostic assistants, streamlined deployment pipelines, and improved interpretability in clinical settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10635v1)
