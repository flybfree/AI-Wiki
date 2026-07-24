---
title: PRISM-DR: Per-lesion Retinal Inference with Specialist Models for Diabetic Retinopathy
published: 2026-07-22T07:52:45Z
authors: Zübeyr Özeren, Tansel Uyar
url: http://arxiv.org/abs/2607.19864v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRISM-DR: Per-lesion Retinal Inference with Specialist Models for Diabetic Retinopathy

## Abstract
Diabetic retinopathy is a leading cause of preventable blindness; its early lesions are small, low contrast, and easily missed in manual screening. Most automated detectors handle the four non-proliferative DR lesions: microaneurysms, hemorrhages, hard exudates, and soft exudates, with a single multi-class model, even though these lesions differ sharply in size, color, morphology, and prevalence, so a shared model favors common, easy classes over rare, difficult ones. We present PRISM-DR, a lesion-specific pipeline that trains one single-class detector per lesion, each with its own configuration. From a raw fundus image, the pipeline applies region of interest cropping, fundus-specific preprocessing, four parallel YOLO detectors, tiling, per-lesion ensembling of five cross-validation folds, and an inter-lesion suppression step that resolves overlaps by physical lesion size and clinical priority rather than confidence. Per lesion, the best of five YOLO generations is selected, and augmentation is tuned by Bayesian optimization. Trained on IDRiD with stratified five-fold cross-validation, the system reaches a test mAP50 of 0.527 and F1 of 0.529, highest AP50 on hard exudates with 0.561. Without fine-tuning, the models transfer well where the imaging scale is close to IDRiD and degrade as field of view and resolution depart. These modest absolute results reflect a small single-source training set and a difficult task; however, treating each lesion as a separate detection problem is a practical alternative to a single multi-class model.

## Metadata
- **Published**: 2026-07-22T07:52:45Z
- **Authors**: Zübeyr Özeren, Tansel Uyar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19864v1)