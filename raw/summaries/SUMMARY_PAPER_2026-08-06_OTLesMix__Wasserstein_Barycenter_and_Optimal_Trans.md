---
title: OTLesMix: Wasserstein Barycenter and Optimal Transport Map for Synthetic Lesion Generation with Diverse Shapes and Locations
url: http://arxiv.org/abs/2608.06264v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_16-54-15Z_OTLesMix_WassersteinBarycenterandOptimalTransportM.md
generated_at: 2026-08-06 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces OTLesMix, a method that uses Wasserstein barycenter and optimal transport to synthesize brain lesion images with varied shapes and locations. It improves Dice scores by 2.9 to 6.6 points compared to models without synthetic data and outperforms existing mix-based approaches.

## Key Takeaways  
- The method employs Wasserstein barycenter and optimal transport to create realistic synthetic lesions that vary in shape and position.  
- Synthetic data generated via OTLesMix raises Dice scores by up to six point five percent over baseline models lacking augmentation.  
- The approach surpasses state-of-the-art mix-based techniques, demonstrating superior performance on three lesion segmentation tasks.

## Context  
Deep learning segmentation relies heavily on diverse training samples; however most augmentation pipelines produce limited variation in lesion morphology and location. This work addresses that limitation by applying advanced transport theory to generate anatomically plausible synthetic images.

## Implications  
The results suggest that sophisticated synthesis methods can significantly enhance model robustness and diagnostic accuracy. Practitioners may adopt OTLesMix to reduce overfitting and improve generalization across heterogeneous clinical datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06264v1)
