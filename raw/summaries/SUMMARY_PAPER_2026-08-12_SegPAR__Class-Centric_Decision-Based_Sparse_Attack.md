---
title: SegPAR: Class-Centric Decision-Based Sparse Attack for Semantic Segmentation
url: http://arxiv.org/abs/2608.11285v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_14-44-33Z_SegPAR_Class_CentricDecision_BasedSparseAttackforS.md
generated_at: 2026-08-12 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SegPAR, a decision‑based sparse attack framework for semantic segmentation that addresses query inefficiency in existing methods. By shifting to a class‑centric exploration strategy and using a discrepancy reward, SegPAR achieves higher sparsity efficiency while reducing MIoU loss compared with black‑box baselines.

## Key Takeaways
- The paper shows that image‑centric pixel accumulation causes severe query waste across the large image space.
- SegPAR replaces this with class‑centric exploration to improve sparsity and reduce MIoU reduction.
- The discrepancy reward corrects misleading feedback from standard decision rewards during pixel accumulation.

## Context
Semantic segmentation relies on dense pixel outputs, making it vulnerable to sparse attacks that can degrade model performance. Prior work has focused on classification, leaving segmentation under‑explored.

## Implications
For practitioners, SegPAR offers a template for applying black‑box attack techniques to image tasks, enabling more efficient and realistic threat modeling. The framework can be integrated into security pipelines to protect segmentation models without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11285v1)
