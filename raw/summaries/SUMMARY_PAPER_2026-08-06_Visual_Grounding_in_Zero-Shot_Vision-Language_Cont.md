---
title: Visual Grounding in Zero-Shot Vision-Language Control
url: http://arxiv.org/abs/2608.06154v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_15-21-42Z_VisualGroundinginZero_ShotVision_LanguageControl.md
generated_at: 2026-08-06 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether zero-shot vision-language controllers truly rely on visual input or if simulator dynamics and prior biases can generate good scores. It finds that most models ignore visual cues, remain constant, or fail under reflection, while a simple image-only control works well, indicating visual information is sufficient but perception must be grounded.

## Key Takeaways
- The direct-control results are largely negative: a constant-SLOW policy outperforms a scripted geometric controller, several models are image-invariant or nearly constant, and models that recognize longitudinal hazards still fail to transform LEFT and RIGHT under reflection.
- No local VLM meets the joint longitudinal and lateral grounding criteria, yet an image-only deterministic positive control estimates the lead gap with 0.090 m MAE and exact mirror equivariance.
- A post‑hoc symmetry‑consensus guardian selects two models from calibration frames and freezes a 2‑of‑4 hazard vote across original and reflected views, achieving balanced accuracy of 0.954 on held‑out frames.

## Context
Vision-language models are being deployed as zero-shot controllers in autonomous driving simulators, but the paper reveals that their performance may be driven more by simulation artifacts than genuine perception. This work provides empirical evidence that visual grounding is not automatic and highlights the need for explicit perceptual checks.

## Implications
For practitioners, the findings suggest that relying solely on high‑level VLMs can lead to unsafe or misleading behavior in safety‑critical applications. Designing modular, locally grounded controllers with symmetry‑aware guardians may improve reliability without sacrificing zero‑shot flexibility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06154v1)
