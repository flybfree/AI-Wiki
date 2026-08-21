---
title: Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions
published: 2026-08-20T07:09:37Z
authors: Mohammad Arif Ul Alam
url: http://arxiv.org/abs/2608.19710v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions

## Abstract
Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation-model representations can be complemented by sonar under severe degradation. We use frozen DINOv2 as the visual encoder and construct a controlled five-level benchmark ranging from clean to extreme visual conditions. We compare conventional visual detection, frozen foundation-model representations, sonar context, fixed multimodal fusion, clean-trained adaptive gating, and degradation-aware gated fusion. Our method trains the fusion mechanism across the full range of degradation while keeping the visual and sonar encoders frozen, allowing modality contributions to adapt without fine-tuning the pretrained backbone. Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement. The learned sonar contribution increases from 14.2% under clean conditions to 41.3% under extreme degradation, demonstrating adaptive redistribution of cross-modal reliance. Fusion provides the largest gains under severe turbidity and blur, whereas color attenuation alone yields little additional benefit. These results show that foundation-model representations remain valuable but insufficient under severe information loss, and that explicitly adapting fusion to modality reliability can improve robust underwater multimodal perception.

## Metadata
- **Published**: 2026-08-20T07:09:37Z
- **Authors**: Mohammad Arif Ul Alam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19710v1)