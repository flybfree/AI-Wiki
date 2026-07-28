---
title: When Less Is More: A Controlled Benchmark of Lightweight CNNs for Satellite Land-Cover Segmentation on DeepGlobe
url: http://arxiv.org/abs/2607.23024v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_03-51-49Z_WhenLessIsMore_AControlledBenchmarkofLightweightCN.md
generated_at: 2026-07-27 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a controlled benchmark to compare five CNN architectures on satellite land‑cover data, showing that lightweight models can achieve high accuracy while using less memory. It finds MobileNetV2_v1 outperforms deeper networks in overall accuracy and IoU despite lower size, highlighting efficiency gains under strict training conditions.

## Key Takeaways
- MobileNetV2_v1 achieved the highest overall accuracy (0.7906) and mean Intersection over Union (0.4625) among all tested models while being only 24.98 MB, demonstrating that lightweight architectures can match performance of larger ones.
- The study isolated architectural depth as a factor by using identical preprocessing, hyperparameters, and training protocols across VGG16, MobileNetV2, InceptionV3, AlexNet, and CNN, showing that optimization benefits are not confounded by data augmentation or class‑imbalance correction.
- Class‑wise analysis revealed strong performance in urban, agricultural, and water categories but noted persistent confusion for rangeland‑barren classes, indicating architectural improvements alone cannot fully resolve spectrally similar minority classes.

## Context
This work addresses a longstanding challenge in remote sensing AI where model size directly impacts processing power on field devices. By providing a reproducible benchmark that isolates architectural effects, the study contributes to the growing need for efficient models that can run on limited hardware without sacrificing accuracy.

## Implications
For satellite data analysts and environmental agencies, the findings suggest that deploying MobileNetV2‑style networks is feasible for real‑time land‑cover mapping in resource‑constrained settings. Practitioners can prioritize lightweight transfer‑learned models to reduce computational load while maintaining high classification fidelity, supporting scalable and sustainable monitoring.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23024v1)
