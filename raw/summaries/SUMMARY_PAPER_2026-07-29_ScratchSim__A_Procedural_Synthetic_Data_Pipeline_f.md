---
title: ScratchSim: A Procedural Synthetic Data Pipeline for Surface Scratch Detection
url: http://arxiv.org/abs/2607.27065v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_15-54-01Z_ScratchSim_AProceduralSyntheticDataPipelineforSurf.md
generated_at: 2026-07-29 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ScratchSim, a procedural pipeline that generates large‑scale annotated synthetic data for surface scratch detection using BlenderProc and COCO format labels. Experiments across two objects with different materials show that fine‑tuning from synthetic weights outperforms real‑only training and mixed training recovers performance when real data are scarce.

## Key Takeaways
- Fine‑tuning from synthetic weights consistently improves detector performance compared to training on real data alone, indicating strong transferability of synthetic information.  
- Mixed training strategies effectively restore accuracy under limited real‑data availability, offering a practical compromise for industrial settings with few labeled examples.  
- The pipeline supports both convolutional and transformer‑based detectors (YOLOX, YOLO26, LW‑DETR) demonstrating broad applicability across model families.

## Context
Automated defect detection remains challenging due to the high cost of manual annotation and limited availability of real labeled datasets. Generative synthetic data pipelines aim to bridge this gap by providing diverse, scalable training examples that mimic real manufacturing conditions without requiring extensive labeling effort.

## Implications
This work enables on‑device industrial inspection systems to operate with high accuracy despite scarce real defect images, reducing reliance on costly annotation pipelines. Practitioners can leverage the provided scripts and models to quickly prototype detection solutions tailored to specific material properties, accelerating time‑to‑market for quality control applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27065v1)
