---
title: Real-Time Semantic Segmentation with Optimized RetinaNet Architectures for Embedded Automotive Systems
published: 2026-07-21T08:30:00Z
authors: Sai Sidharth D
url: http://arxiv.org/abs/2607.22714v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Real-Time Semantic Segmentation with Optimized RetinaNet Architectures for Embedded Automotive Systems

## Abstract
Real-time perception is a foundational requirement for advanced driver assistance systems (ADAS) and autonomous vehicles, yet embedded automotive platforms impose severe constraints on compute, memory, and power. This paper presents an optimized semantic segmentation architecture derived from the RetinaNet detection framework, adapted for dense pixel-wise prediction and tailored for deployment on resource-constrained embedded hardware. The proposed architecture, termed Opt-RetinaSeg, replaces the standard ResNet-50 backbone with a hybrid lightweight feature extractor, restructures the Feature Pyramid Network (FPN) to reduce redundant multi-scale computation, and introduces a compact segmentation head guided by focal-loss-inspired class balancing to address the severe foreground-background imbalance common in road scenes. We further apply a three-stage optimization pipeline consisting of structured channel pruning, post-training INT8 quantization, and knowledge distillation from a high-capacity teacher network. Evaluated on the Cityscapes and BDD100K datasets and deployed on an NVIDIA Jetson Xavier NX and a Qualcomm QCS610 automotive SoC, the proposed model achieves 73.9% mIoU at 70.4 FPS, representing a 7.4x inference speedup and a 4x reduction in model size relative to the ResNet-50 baseline, with less than 3% accuracy degradation. These results indicate that RetinaNet-derived architectures, when systematically optimized, are viable candidates for real-time semantic segmentation in embedded automotive perception pipelines

## Metadata
- **Published**: 2026-07-21T08:30:00Z
- **Authors**: Sai Sidharth D
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22714v1)