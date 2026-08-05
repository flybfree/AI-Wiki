---
title: Distilled Roads: Generalisable Road Network Extraction Across Sensors, Resolutions, and Region
published: 2026-08-04T10:01:30Z
authors:  Sanayya, Rakshith Sathish, Ashwathi Nambiar
url: http://arxiv.org/abs/2608.03407v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilled Roads: Generalisable Road Network Extraction Across Sensors, Resolutions, and Region

## Abstract
Road network segmentation from satellite imagery remains challenging due to large geographic variation in road appearance, occlusions, and domain shifts introduced by differing resolutions and sensors. Existing models, typically trained under narrow resolution--region combinations, generalise poorly to unseen environments such as rural settings, regions with distinct road materials, or imagery from new satellite platforms, often producing broken or disconnected predictions. Adapting these models to new domains usually requires retraining or fine-tuning, which is costly and risks catastrophic forgetting.   In this work, we reframe global road extraction as a continual adaptation problem rather than an architectural one. Our framework combines cross-resolution knowledge distillation across a resolution-decreasing curriculum, multi-sensor training, and topology-aware supervision, yielding a single model that generalises across $0.3-1.0$ m imagery from multiple satellite platforms across continents. On publicly available benchmarks, including City-Scale and Global-Scale, our model outperforms state-of-the-art results by up to $22$ F1 points and $15$ APLS points, while remaining the most efficient, with $3\times$ faster inference. Our results suggest that improved robustness across diverse sub-meter satellite imagery can be achieved through targeted training strategies, such as data curricula, distillation, and topology-aware losses, rather than increasingly complex architectures.

## Metadata
- **Published**: 2026-08-04T10:01:30Z
- **Authors**:  Sanayya, Rakshith Sathish, Ashwathi Nambiar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03407v1)