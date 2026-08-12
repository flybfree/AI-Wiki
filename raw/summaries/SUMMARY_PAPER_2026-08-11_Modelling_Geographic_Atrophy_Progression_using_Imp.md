---
title: Modelling Geographic Atrophy Progression using Implicit Neural Representations
url: http://arxiv.org/abs/2608.10807v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_11-26-01Z_ModellingGeographicAtrophyProgressionusingImplicit.md
generated_at: 2026-08-11 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method for modelling the progression of geographic atrophy in age‑related macular degeneration using implicit neural representations. The approach generates both fundus autofluorescence images and GA segmentations at past and future time points while preserving image quality. Experiments show that the model yields the lowest mean absolute error in lesion area and the highest Dice score among compared approaches.

## Key Takeaways
- The method produces high‑quality FAF reconstructions without degrading the original image, indicating a balance between segmentation accuracy and visual fidelity.  
- GA lesion areas are predicted with minimal mean absolute error, suggesting precise estimation of atrophy extent over time.  
- Dice scores reach their highest values, reflecting strong agreement between predicted and true segmentations across diverse scenarios.

## Context
Implicit neural representations aim to capture complex spatial patterns from limited data by learning latent features rather than explicit pixel‑wise outputs. This work demonstrates that such representations can be applied to longitudinal retinal imaging where data are sparse yet critical for clinical monitoring of disease progression.

## Implications
Clinicians could use the model’s predictions to track individual GA growth, enabling early intervention decisions and personalized care plans. The framework may also inspire similar applications in other low‑data medical imaging tasks that require accurate lesion delineation over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10807v1)
