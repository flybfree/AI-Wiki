---
title: Toward Reliable RGB-D Semantic Segmentation: Handling Missing Modalities via Condition Dropout
url: http://arxiv.org/abs/2607.20326v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_16-12-27Z_TowardReliableRGB_DSemanticSegmentation_HandlingMi.md
generated_at: 2026-07-23 22:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Condition Dropout (ConD), a method for improving RGB-D semantic segmentation robustness when one of the modalities—RGB or depth—is missing. By simulating complete, RGB-missing, and depth-missing inputs during training, ConD mitigates performance degradation without affecting full‑modality accuracy.

## Key Takeaways
- Condition Dropout adds a second training stage that randomly generates synthetic inputs where either RGB or depth is absent, while freezing the original encoders.  
- The copied encoders receive zero‑initialized feature injection to adapt to missing cues, which reduces degradation caused by incomplete sensor data.  
- Experiments on NYU-Depth V2 and SUN RGB‑D demonstrate that ConD maintains full‑modality performance and even yields slight gains when both modalities are present.

## Context
In autonomous systems, surveillance cameras often suffer from occlusion or failure, leading to partial sensor inputs. Most deep learning models assume both RGB and depth streams are available, which limits their practical deployment in real‑world scenarios where such failures occur frequently.

## Implications
ConD offers a low‑cost way to make existing segmentation pipelines resilient to missing modalities without retraining from scratch. Practitioners can integrate the method into deployed systems, enhancing reliability for applications ranging from robotics to indoor navigation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20326v1)
