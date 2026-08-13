---
title: CLEAR: Class-wise Expert Aggregation with Structured Sampling for Long-Tailed Classification
url: http://arxiv.org/abs/2608.11287v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_15-45-09Z_CLEAR_Class_wiseExpertAggregationwithStructuredSam.md
generated_at: 2026-08-12 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
CLEAR proposes a modular ensemble framework for long‑tailed classification that generates diverse experts through threshold‑based structured sampling while preserving the full label space. The method estimates class‑wise trust scores using a smoothed precision formulation and combines predictions with a class‑wise generalized product‑of‑experts aggregation. Experiments on CIFAR‑100‑LT, ImageNet‑LT, and Places‑LT across multiple backbones show competitive overall accuracy and particularly strong few‑shot performance.

## Key Takeaways
- CLEAR generates diverse experts through threshold‑based structured sampling while preserving the full label space.
- It estimates class‑wise trust scores using a smoothed class‑wise precision formulation.
- During inference, expert predictions are combined via class‑wise generalized product‑of‑experts aggregation, allowing different experts to be emphasized for different classes.

## Context
Long‑tailed classification is common in real‑world datasets where rare classes are underrepresented, causing models to be unreliable on those classes. Existing approaches often apply global rebalancing or treat all classes equally, which does not address per‑class reliability concerns. This paper introduces a principled way to select and trust experts individually for each class.

## Implications
Class‑wise trust scores provide a design principle that can guide ensemble construction, enabling more robust predictions on long‑tailed data with limited labeled samples. Practitioners can integrate CLEAR into modular architectures, improving deployment efficiency when dealing with imbalanced datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11287v1)
