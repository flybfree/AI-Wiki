---
title: Same Predictions, Different Reasons: The Effect of Quantization on Model Explanations
url: http://arxiv.org/abs/2607.22872v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_19-26-47Z_SamePredictions_DifferentReasons_TheEffectofQuanti.md
generated_at: 2026-07-27 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how post‑training quantization (PTQ) influences the interpretability of five popular CNN architectures when moving from full‑precision to INT8 and INT4 representations. By comparing Grad‑CAM spatial attention with LIME input‑level attributions across two binary classification tasks, the authors reveal that accuracy alone does not guarantee stable explanations.

## Key Takeaways
- Classification accuracy can remain high while interpretability deteriorates, indicating that precision reduction may alter model reasoning without affecting performance metrics.  
- DenseNet161 shows consistent feature consistency across both INT8 and INT4, suggesting architectural robustness to quantization.  
- EfficientNet‑B0 experiences a notable drop in input‑level attribution despite good spatial attention, highlighting vulnerability of certain models to precision loss.

## Context
Quantization is essential for deploying deep networks on edge devices where compute and memory are limited. However, the literature often overlooks how such compression impacts model explanations, which are crucial for trustworthy AI applications.

## Implications
For practitioners, this work underscores that selecting an architecture matters as much as choosing a quantization level when interpretability is required. Deployers must balance accuracy with explanation fidelity to ensure reliable and explainable models in production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22872v1)
