---
title: Sequential Modality Dropout for Robust Multi-Modal Sequential Recommendation
url: http://arxiv.org/abs/2608.10240v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_21-18-25Z_SequentialModalityDropoutforRobustMulti_ModalSeque.md
generated_at: 2026-08-11 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Sequential Modality Dropout (SMD), a technique that makes multi‑modal sequential recommenders robust to missing image or text streams during serving. Experiments show SMD improves text retention by up to 3.2× while preserving full‑modality accuracy, and even under extreme missingness retains 61% of HR@10 versus 22% without the method.

## Key Takeaways
- During training each modality stream is independently erased with probability p for an entire user interaction history, forcing the model to learn predictions without relying on any single modality.  
- The robustness metric retention measures how much of a model’s full‑modality accuracy (HR@10) survives when a modality is removed at test time, and SMD raises this by 1.0 to 3.2× with little cost to the baseline performance.  
- With an extreme 95% per‑item missing rate, SMD retains 61% of HR@10 versus only 22% without it, a 2.8× improvement.

## Context
Multi‑modal sequential recommenders assume every item carries both image and text information, but real product catalogs often lack one or the other at serving time, causing sharp drops in recommendation quality. This paper addresses that gap by providing an architecture‑agnostic way to train models that can handle missing modalities without retraining.

## Implications
SMD offers a simple four‑line change that can be applied to existing multi‑modal sequential recommender systems, reducing the risk of performance collapse when data is incomplete in production. Practitioners can expect higher user satisfaction and lower churn by maintaining relevance even when image or text cues are unavailable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10240v1)
