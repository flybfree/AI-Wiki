---
title: Layers Matter: Why Continual Learning Regularization Should Be Layer-Adaptive
url: http://arxiv.org/abs/2608.15901v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_19-37-38Z_LayersMatter_WhyContinualLearningRegularizationSho.md
generated_at: 2026-08-17 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that continual learning regularizers such as EWC should adapt their penalties to individual layers rather than using a uniform per‑parameter approach. By assuming a block‑diagonal Hessian, the authors show that forgetting can be decomposed into layer‑specific terms driven by each layer’s top eigenvalue of curvature, which diagonal Fisher values cannot capture.

## Key Takeaways
- Forgetting decomposes as a sum of per‑layer contributions weighted by each layer's top Hessian eigenvalue.  
- Diagonal‑Fisher weights cannot recover the true eigenvalue because they only average across parameters.  
- Uniform regularization loses new‑task performance proportionally to the layer condition number, which can be large.

## Context
Continual learning aims to maintain task performance while adding new tasks, but existing regularizers often ignore how curvature varies across layers. This limitation hampers stable training and leads to significant forgetting, especially in deep networks where early layers are highly sensitive.

## Implications
Practitioners should implement layer‑adaptive regularization that strongly penalizes changes in early layers and allows deeper layers more flexibility. This can boost overall continual learning performance and make models robust to task transitions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15901v1)
