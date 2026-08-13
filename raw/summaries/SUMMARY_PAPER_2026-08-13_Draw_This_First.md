---
title: Draw This First
url: http://arxiv.org/abs/2608.12064v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_13-48-56Z_DrawThisFirst.md
generated_at: 2026-08-13 08:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a method for generating ordered vector sketches by predicting a 2D field that defines stroke order rather than drawing strokes sequentially. Using a pretrained latent flow-matching transformer as an image prior, the model outputs an intermediate representation while training the VAE decoder to predict the order field, stroke mask, and segmentation. The predicted segmentation is vectorized into polylines sorted by the field value, yielding an ordered vector sketch that can be produced from text or derendered from images.

## Key Takeaways
- The model predicts a continuous 2D field that encodes the drawing order, allowing strokes to be reordered after generation.
- It leverages a pretrained latent flow-matching transformer as an image prior and trains the VAE decoder jointly on the order field, stroke mask, and segmentation.
- The final output is an ordered vector sketch derived by sorting polylines according to the predicted field values.

## Context
This work addresses the challenge of generating coherent sketches from textual instructions in a manner that respects drawing order, which is essential for applications like interactive design and image restoration. By reversing the conventional stroke‑by‑stroke approach, the authors enable more flexible and context‑aware generation pipelines that can handle complex compositions without manual ordering.

## Implications
For practitioners, this framework reduces the need for separate ordering logic in sketch generation systems, streamlining pipeline integration with text‑to‑image or image‑to‑sketch models. The ability to derender images into ordered vectors opens new possibilities for visual editing and animation where stroke sequence is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12064v1)
