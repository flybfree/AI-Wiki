---
title: Synthetic Data Augmentation for Satellite-Based Analysis of Battle-Damaged Agricultural Fields in Ukraine
url: http://arxiv.org/abs/2608.16380v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_10-32-38Z_SyntheticDataAugmentationforSatellite_BasedAnalysi.md
generated_at: 2026-08-17 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes using synthetic data augmentation to improve satellite image classification of bombed versus normal agricultural fields in Ukraine. By training GAN and DDPM models on real images, it generates additional labeled samples for the underrepresented not‑bombed class. The best configuration raises accuracy from 84% to 88%, balanced accuracy from 67% to 81%, macro F1 from 65% to 78%, and recall for the not‑bombed class from 41% to 69%.

## Key Takeaways
- The synthetic GAN/DDPM models can create realistic bombed and non‑bombed field images that augment training data without affecting real test evaluation.  
- Balanced DDPM augmentation yields the largest gains, especially improving recall for the previously underrepresented not‑bombed class from 41% to 69%.  
- The classifier is a Vision Transformer evaluated on exclusively real test sets, ensuring synthetic images only aid training.

## Context
In geospatial AI, limited labeled data hampers performance of computer‑vision systems for disaster monitoring. This work addresses that bottleneck by demonstrating how generative models can supply balanced synthetic samples to boost model reliability in data‑scarce environments.

## Implications
These results show that synthetic augmentation can be a practical solution for war‑affected regions where real imagery is scarce, enabling robust classification pipelines. Practitioners may adopt DDPM‑based methods to improve model performance in similar data‑scarce scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16380v1)
