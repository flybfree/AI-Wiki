---
title: Distilling Vision-Language Models for Robust Traffic Sign Perception in Autonomous Vehicles
published: 2026-08-09T17:05:00Z
authors: Pedram MohajerAnsari, Amir Salarpour, Mert D. Pesé
url: http://arxiv.org/abs/2608.08815v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling Vision-Language Models for Robust Traffic Sign Perception in Autonomous Vehicles

## Abstract
Traffic sign recognition (TSR) models based on deep neural networks achieve strong clean-data performance but remain vulnerable to physically realizable adversarial attacks, including shadow perturbations, natural-light interference, and printed patches. Existing defenses often improve robustness against one attack type while degrading performance on others, and can reduce clean accuracy. We propose LAMDA (Language-Anchored Model for Direction Alignment), a training framework that transfers language-grounded structure into TSR models without using adversarial examples or adding inference-time overhead. LAMDA builds two fixed prototype banks from VLM-generated sign descriptions and class names using a frozen OpenCLIP text encoder, and uses them to supervise visual features through two complementary auxiliary losses during training. At inference, the adapter and prototype banks are discarded, leaving a standard backbone and classifier. Evaluated on GTSRB and LISA across four backbones and three physical attack types, LAMDA is the only method among ten evaluated that consistently improves robustness across all attack-backbone-dataset combinations, with gains of up to +12.5 pp under shadow attacks and +13.2 pp under natural-light attacks, while preserving or improving clean accuracy in nearly all cases.

## Metadata
- **Published**: 2026-08-09T17:05:00Z
- **Authors**: Pedram MohajerAnsari, Amir Salarpour, Mert D. Pesé
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08815v1)