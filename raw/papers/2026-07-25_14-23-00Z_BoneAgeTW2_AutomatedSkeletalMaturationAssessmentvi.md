---
title: BoneAgeTW2: Automated Skeletal Maturation Assessment via the Tanner-Whitehouse 2 Method, Deep Learning, and Clinical Report Generation with Distribution Curves
published: 2026-07-25T14:23:00Z
authors: Juan Manuel Castillo Pinto
url: http://arxiv.org/abs/2607.23224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BoneAgeTW2: Automated Skeletal Maturation Assessment via the Tanner-Whitehouse 2 Method, Deep Learning, and Clinical Report Generation with Distribution Curves

## Abstract
We present BoneAgeTW2, the first fully open-source system to automate the complete Tanner-Whitehouse 2 (TW2) clinical protocol for skeletal maturity assessment end-to-end. The system employs YOLOv8 for precise detection and localization of the 20 TW2 hand bones from radiographic images, and an EfficientNet-B3 backbone with 20 independent classification heads to assign maturation stages (A-I) to each bone simultaneously. From these predictions, the system automatically generates clinical PDF reports including interactive Gaussian distribution curves for all 20 bones, enabling direct comparison with population norms. The model is trained on the public RSNA Pediatric Bone Age Challenge dataset (12,611 hand radiographs) using a pseudo-labeling strategy to derive per-bone stage labels from global bone age annotations. The full codebase is publicly available at https://github.com/jmmana/BoneAgeTW2.

## Metadata
- **Published**: 2026-07-25T14:23:00Z
- **Authors**: Juan Manuel Castillo Pinto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23224v1)