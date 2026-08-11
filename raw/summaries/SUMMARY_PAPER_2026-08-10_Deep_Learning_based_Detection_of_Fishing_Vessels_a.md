---
title: Deep Learning based Detection of Fishing Vessels and Fishing Monitoring using Nightlight Images
url: http://arxiv.org/abs/2608.09360v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_09-39-18Z_DeepLearningbasedDetectionofFishingVesselsandFishi.md
generated_at: 2026-08-10 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a deep learning system that detects small fishing vessels using nighttime light imagery from the SDGSAT‑1 satellite, specifically targeting “dark” vessels lacking AIS signals along India’s western coast. The dual‑branch YOLO11 architecture achieved high precision and recall, detecting 31 525 vessel instances across a two‑year period.

## Key Takeaways
- The model combines 10‑meter panchromatic and 40‑meter RGB data into a single network, yielding an F1‑score of 0.96 and mAP@50 of 0.96, outperforming standard YOLO variants.  
- Cross‑matching with AIS shows only 22.7 % of detections have corresponding transmissions, indicating that 77.3 % are likely dark vessels.  
- Spatio‑temporal analysis reveals peak fishing activity from January to April within a 50‑100 km corridor parallel to the coastline.

## Context
The integration of satellite nighttime light data with convolutional neural networks exemplifies how AI can augment maritime surveillance beyond traditional radar or AIS, offering continuous monitoring where conventional sensors fail. This approach aligns with broader trends in remote sensing and computer vision for environmental protection and security applications.

## Implications
For Indian authorities, the system provides a cost‑effective tool to identify illegal fishing operations that evade detection by AIS, supporting enforcement of sustainable fisheries policies. Practitioners can leverage similar multimodal deep learning pipelines to monitor other maritime activities in low‑visibility conditions worldwide.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09360v1)
