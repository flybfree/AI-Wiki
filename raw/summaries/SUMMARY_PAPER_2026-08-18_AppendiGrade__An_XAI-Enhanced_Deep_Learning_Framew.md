---
title: AppendiGrade: An XAI-Enhanced Deep Learning Framework for Grading Appendicitis in Ultrasound with Gaussian Blur and Grad-CAM
url: http://arxiv.org/abs/2608.17923v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_15-46-42Z_AppendiGrade_AnXAI_EnhancedDeepLearningFrameworkfo.md
generated_at: 2026-08-18 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AppendiGrade, an XAI‑enhanced deep learning framework for automatically detecting complicated appendicitis in ultrasound images using Gaussian blur and Grad‑CAM. It trains four pretrained models on a dataset of 4679 images across five classes and achieves high accuracy after preprocessing. Gradient‑weighted class activation mapping provides interpretable heatmaps that highlight infected regions.

## Key Takeaways
- The InceptionV3 model reaches 95.58% accuracy after image sharpening, hyperparameter tuning, and fine‑tuning, surpassing other models.
- The dataset includes five distinct appendicitis categories, enabling robust classification beyond simple binary detection.
- Grad‑CAM generates visual explanations that aid clinician verification of the model’s predictions.

## Context
This work contributes to medical imaging AI by integrating explainability techniques with deep learning for clinical decision support. By providing interpretable heatmaps, the framework bridges the gap between automated diagnosis and human expertise. It also demonstrates how preprocessing can significantly boost model performance in real‑world ultrasound data.

## Implications
Clinicians can rely on visual cues to validate AI outputs, reducing diagnostic errors. The approach may be adopted in hospitals to streamline appendicitis triage and improve patient outcomes without radiation exposure. Future research could explore deployment in other abdominal conditions using similar XAI methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17923v1)
