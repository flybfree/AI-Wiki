---
title: Safety-oriented sidewalk and road segmentation for smartphone-based assistive navigation
url: http://arxiv.org/abs/2607.21137v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_10-16-43Z_Safety_orientedsidewalkandroadsegmentationforsmart.md
generated_at: 2026-07-23 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SENSATION-DS, a chest-height pedestrian-view dataset and safety-oriented segmentation framework to distinguish walkable sidewalks from unsafe road regions for smartphone assistive navigation. It evaluates five models using mIoU, error rates, and runtime on Android, finding UPerNet-MobileNetV3 best in accuracy while DeepLabV3Plus-MobileNetV3 excels in low false‑safe errors and high speed.

## Key Takeaways
- Synthetic augmentation generally improves segmentation accuracy across the nine-class taxonomy.
- SAM2 pseudo-labels consistently reduce Road-as-Sidewalk Error Rate, a proxy for false safety.
- UPerNet-MobileNetV3 achieves the highest offline mIoU (0.715) while DeepLabV3Plus-MobileNetV3 yields the lowest error rate and best Android runtime at 7.38 FPS.

## Context
Assistive navigation relies on accurate perception of safe pathways, yet most models prioritize accuracy over real‑world safety or device constraints. This study bridges that gap by jointly measuring performance, false‑safe behavior, and smartphone feasibility.

## Implications
For developers, the findings guide model selection to balance precision with conservative error handling and low latency. Practitioners can adopt these benchmarks to improve user trust and reliability in urban mobility solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21137v1)
