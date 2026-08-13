---
title: Uncertainty-Aware Compositional Localization and Placement Assessment of Catheters and Tubes in Chest X-Rays
published: 2026-08-11T16:04:58Z
authors: Harshil Lodhiya
url: http://arxiv.org/abs/2608.11288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Aware Compositional Localization and Placement Assessment of Catheters and Tubes in Chest X-Rays

## Abstract
Assessing catheter and tube placement on chest X-rays is safety-critical yet tedious and error-prone. Current deep learning methods either classify placement globally -- losing track of which device is where -- or segment all devices into a single mask, making per-device assessment impossible when catheters overlap. We introduce UCompCXR, a compositional framework that detects local catheter fragments, associates them into device instances via graph-based clustering, fuses per-fragment tip predictions through precision-weighted Gaussian estimation, and classifies placement per device. On the RANZCR CLiP dataset (30,083 images, 5-fold patient-level CV with bootstrap CIs), UCompCXR detects 26% more devices than a strong multi-task baseline sharing the same MobileNetV3 backbone, with 75% fewer false positives and well-calibrated tip uncertainty (95% coverage = 0.948). The aggregate tip error rises -- but only because the model finds devices the baseline misses entirely, especially nasogastric tubes. On matched devices, catastrophic localization failures drop substantially. At 2.27M parameters in a single forward pass, the model is deployable on resource-constrained clinical hardware.

## Metadata
- **Published**: 2026-08-11T16:04:58Z
- **Authors**: Harshil Lodhiya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11288v1)