---
title: From Perturbation Correction to Geometry-Aware Sampling: Sharpness-Guided Equilibrium Sampling for Balanced Flat Minima in Long-Tailed Learning
url: http://arxiv.org/abs/2607.21999v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_05-56-00Z_FromPerturbationCorrectiontoGeometry_AwareSampling.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Sharpness-Guided Equilibrium Sampling (SGS), a method that treats the sampling distribution as an active control variable to shape optimization geometry in long-tailed learning. By dynamically adjusting class probabilities and using cumulative counts together with exponential moving average sharpness estimates, SGS reduces reliance on class‑wise perturbations while improving tail accuracy compared to existing SAM variants.

## Key Takeaways
- SGS increases the probability of less frequently sampled classes and suppresses those whose loss changes are large, thereby balancing exposure without extra backward passes.  
- The method is characterized by a continuous‑time stochastic differential equation and a PAC‑Bayes analysis that links frequency‑sharpness feedback to a flatter training landscape.  
- On CIFAR‑100 with an imbalance ratio of 100, SGS‑SAM raises tail accuracy by 10.85 points and overall performance by 3.56 points relative to Focal‑SAM.

## Context
Long‑tailed learning suffers from dominance of head classes and sharp minima in under‑represented ones, limiting generalization. Conventional re‑sampling tackles exposure but ignores geometry, while SAM variants modify losses after biased batches are drawn, adding computational overhead.

## Implications
This work shows that sampling can directly influence the loss landscape, offering a lightweight alternative to heavy geometric modifications. Practitioners may adopt SGS to improve tail performance with minimal training time increase, paving the way for joint data‑exposure and optimization control in long‑tailed scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21999v1)
