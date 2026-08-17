---
title: Intelligent Detection of Mechanical, Electrical, and Plumbing (MEP) Metrics Based on 2D Floor Plans
url: http://arxiv.org/abs/2608.14317v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_13-59-55Z_IntelligentDetectionofMechanical_Electrical_andPlu.md
generated_at: 2026-08-16 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a neural network model that automatically extracts lighting symbols, identifies light types, and reads associated texts from two‑dimensional floor plans using Mask RCNN as its backbone. The model achieved high detection and segmentation performance with bbox_mAP of 0.7596 and segm_mAP of 0.7111, maintaining strong results across various IoU thresholds. These findings demonstrate that the system can support efficient floor design and power‑requirement estimation.

## Key Takeaways
- The model reaches a bounding‑box mAP of 0.7596 and segmentation mAP of 0.7111, indicating reliable detection and precise localization of MEP symbols on floor plans.
- Performance remains robust at high IoU thresholds, with bbox_mAP dropping to 0.9850 at 50% IoU and segm_mAP to 0.9219 at 75% IoU, showing strong recall under challenging conditions.
- The system is trained on annotated floor‑plan images converted to COCO format, enabling transferable learning for diverse architectural datasets.

## Context
Automated interpretation of building schematics remains a bottleneck in design workflows, where manual parsing consumes significant time and increases error risk. This work contributes to the growing trend of applying computer vision and deep learning to generate actionable data from 2D drawings, aligning with broader goals of smart‑building optimization.

## Implications
Architects and engineers can leverage this tool to accelerate design cycles, reduce material waste, and estimate energy consumption more accurately. By automating MEP extraction, the approach paves the way for integrated building information modeling that supports sustainable construction practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14317v1)
