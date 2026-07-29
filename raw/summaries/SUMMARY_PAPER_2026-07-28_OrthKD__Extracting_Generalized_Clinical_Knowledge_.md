---
title: OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment
url: http://arxiv.org/abs/2607.25545v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_10-24-40Z_OrthKD_ExtractingGeneralizedClinicalKnowledgefromH.md
generated_at: 2026-07-28 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OrthKD, a selective-trust knowledge distillation method for diabetic retinopathy screening that leverages complementary teachers. It transfers full supervision from a strong CNN and feature-only distillation from a weaker Transformer to create an orthogonally aligned student model. On large datasets the student achieves high accuracy while remaining lightweight.

## Key Takeaways
- OrthKD selects full supervision from the EfficientNet-B3 teacher and uses only feature maps from the Swin-Base teacher, preventing logit misinformation.
- The orthogonal projection constraint forces complementary evidence, improving robustness to domain shift in retinal images.
- The resulting 5.4M‑parameter MobileNetV3 student reaches 0.885 QWK on EyePACS and lifts Messidor‑2 zero‑shot performance from 0.507 to 0.728.

## Context
Knowledge distillation is widely used to shrink deep models for edge deployment, but most prior work assumes uniform teacher reliability which often fails in medical imaging where teachers differ in strength and modality. This paper addresses that gap by designing a trust‑aware framework that respects heterogeneity among teachers.

## Implications
The approach enables high‑performing yet resource‑efficient screening tools suitable for primary care clinics with limited bandwidth. Practitioners can deploy accurate models without sacrificing safety, supporting broader adoption of AI in healthcare.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25545v1)
