---
title: Hide&Seek: Learning to Explain in an End-to-End Differentiable Network
url: http://arxiv.org/abs/2608.16689v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_15-10-05Z_Hide_Seek_LearningtoExplaininanEnd_to_EndDifferent.md
generated_at: 2026-08-17 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Hide&Seek, an end‑to‑end differentiable model for instance‑wise feature selection that jointly learns a selector and a predictor without information leakage. The authors replace discrete feature removal with a continuous scaling operation, enabling smooth gradient updates during training. Experiments show Hide&Seek outperforms state‑of‑the‑art methods across diverse datasets while being fast to train.

## Key Takeaways
- Feature removal is reformulated as a differentiable scaling of each feature rather than binary exclusion, preserving the ability to backpropagate gradients.
- A parsimony‑weight annealing schedule stabilizes training by gradually reducing the weight on the selector component, preventing overfitting.
- The joint objective eliminates information leakage between selection and prediction, allowing reliable gradient flow throughout the network.

## Context
Feature selection remains a critical challenge in interpretable machine learning, where global methods often miss instance‑specific patterns. Differentiable selectors are rare because traditional binary masks break gradient computation, limiting integration into modern training pipelines that rely on automatic differentiation.

## Implications
For practitioners, Hide&Seek offers a practical path to transparent models without sacrificing performance or computational cost. The framework can be adopted in industry settings where explainability and fast iteration are essential, paving the way for more trustworthy AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16689v1)
