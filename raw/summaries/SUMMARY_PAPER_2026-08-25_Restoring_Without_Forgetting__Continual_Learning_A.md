---
title: Restoring Without Forgetting: Continual Learning Across Image Degradations
url: http://arxiv.org/abs/2608.23799v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_20-04-18Z_RestoringWithoutForgetting_ContinualLearningAcross.md
generated_at: 2026-08-25 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Restoring without Forgetting (RwF), a continual learning framework for multi-degradation image restoration that adapts to new degradation types without retraining the whole model. The method learns lightweight adapters for each degradation, achieving higher PSNR than sequential fine‑tuning while maintaining routing accuracy across diverse real‑world conditions.

## Key Takeaways
- RwF solves continual domain‑incremental learning by creating a small adapter per degradation, preventing catastrophic forgetting when new degradations appear.  
- The framework operates on a shared image content benchmark with five degradation domains, allowing unsupervised routing to select the correct restoration path at test time.  
- Compared to naive fine‑tuning, RwF improves final average PSNR by 15.25 dB on Restormer and 11.83 dB on NAFNet across the five‑domain sequence.

## Context
Continual learning in vision tasks faces challenges when new environments or degradations emerge, especially where historical data is unavailable due to privacy or storage limits. Existing approaches either require full retraining or suffer from forgetting, limiting real‑world applicability of restoration models that must adapt dynamically.

## Implications
RwF demonstrates that lightweight adapters can preserve performance while enabling rapid adaptation, offering a practical solution for edge devices with limited resources. This systematic baseline encourages researchers to design continual learning pipelines that respect data constraints and degrade gracefully over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23799v1)
