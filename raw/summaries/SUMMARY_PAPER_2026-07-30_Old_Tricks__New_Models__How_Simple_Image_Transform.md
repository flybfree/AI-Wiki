---
title: Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation
url: http://arxiv.org/abs/2607.28187v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_13-25-09Z_OldTricks_NewModels_HowSimpleImageTransformationsB.md
generated_at: 2026-07-30 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the shift from conventional classifiers to large foundation‑model based APIs improves the robustness of image moderation. The authors perform a black‑box test across three commercial services and discover that simple, model‑agnostic transformations can reliably bypass these systems, indicating that the new models are not inherently more secure.

## Key Takeaways
- All three commercial services can be circumvented using inexpensive image transformations such as color inversion or grayscale conversion that do not require gradients or surrogate models.  
- Even fixed transformations like color inversion cause unsafe‑to‑safe decision changes while leaving the content recognizable to humans.  
- The systems’ vulnerabilities differ across datasets and harm categories, with multimodal and self‑harm images showing the greatest weaknesses.

## Context
Modern AI moderation relies on foundation models that claim broader contextual understanding than traditional classifiers. However, these models are often evaluated under idealized conditions, ignoring real‑world image manipulations that can undermine their safety guarantees.

## Implications
Practitioners should treat foundation‑model APIs as one layer in a layered moderation pipeline rather than a standalone filter. The findings highlight the need for rigorous testing against diverse transformations to ensure genuine security across all content types.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28187v1)
