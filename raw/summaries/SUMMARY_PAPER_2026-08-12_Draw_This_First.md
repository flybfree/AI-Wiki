---
title: Draw This First
url: http://arxiv.org/abs/2608.12064v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_13-48-56Z_DrawThisFirst.md
generated_at: 2026-08-12 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a method that generates ordered vector sketches by predicting a 2D field that encodes the drawing order, rather than creating strokes sequentially. It leverages a pretrained latent flow-matching transformer to provide an image prior and trains a VAE decoder to output both the order field and stroke segmentation. The predicted field is used to sort polylines into an ordered vector sketch.

## Key Takeaways
- The model predicts a 2D field that defines the drawing order, which is then used to sort strokes into an ordered vector sketch.
- It uses a pretrained latent flow-matching transformer as an image prior and trains the VAE decoder to generate both the order field and stroke segmentation simultaneously.
- The final output can be derived from either a text description or an existing image by following the predicted drawing order.

## Context
This work addresses the challenge of generating coherent, ordered sketches that follow human instructions, which is important for applications like visual programming and interactive design. By decoupling stroke creation from sequential execution, the approach offers flexibility in how strokes are produced while maintaining a logical sequence.

## Implications
For developers building sketch tools or generative art systems, this method enables more natural user control over drawing order without complex procedural logic. It also opens possibilities for converting textual commands into visual outputs that respect spatial and temporal constraints of the image.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12064v1)
