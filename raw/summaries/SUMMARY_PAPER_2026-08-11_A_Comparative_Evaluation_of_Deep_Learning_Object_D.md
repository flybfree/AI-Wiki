---
title: A Comparative Evaluation of Deep Learning Object Detection Models on a Real-World Multi-Plant Dataset from Africa
url: http://arxiv.org/abs/2608.11053v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-22-58Z_AComparativeEvaluationofDeepLearningObjectDetectio.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study evaluates six object detection models—YOLOv5, YOLOv8, YOLO11, YOLO26, Faster R-CNN, and RT-DETR—on a real‑world agricultural dataset collected from Nigerian farms. The results indicate that RT-DETR outperforms the others in both precision and mAP@0.5:0.95, while YOLOv8 and YOLO11 also show strong performance and faster training.

## Key Takeaways
- RT‑DETR achieved the highest overall detection quality with a precision of 0.768 and an mAP@0.5:0.95 of 0.624, outperforming all other models on the AgriAISeg dataset.  
- YOLOv8 and YOLO11 delivered consistent high performance, highlighting their suitability for real‑world field conditions despite being one‑stage detectors.  
- Faster R-CNN recorded significantly lower accuracy (mAP@0.5 = 0.466), suggesting reduced effectiveness under complex lighting, occlusion, and perspective variations typical of agricultural scenes.

## Context
The paper addresses a gap in AI research where most object detection benchmarks are built on controlled or synthetic data that do not reflect the variability of real agricultural environments. By using AgriAISeg, it demonstrates how modern detectors can be validated under diverse lighting, occlusion, and viewpoint conditions typical of field crops.

## Implications
For precision farming practitioners, these findings suggest that transformer‑based detectors like RT-DETR may provide more reliable crop monitoring solutions with higher accuracy. Industry adoption could benefit from faster training times associated with YOLO variants, enabling real‑time deployment in resource‑constrained agricultural settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11053v1)
