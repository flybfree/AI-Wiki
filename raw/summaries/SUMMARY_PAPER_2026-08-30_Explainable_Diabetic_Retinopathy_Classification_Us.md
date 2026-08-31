---
title: Explainable Diabetic Retinopathy Classification Using Vision Foundation Models
url: http://arxiv.org/abs/2608.28207v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_11-26-43Z_ExplainableDiabeticRetinopathyClassificationUsingV.md
generated_at: 2026-08-30 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an explainable diabetic retinopathy classification system that leverages vision foundation models such as DINOv2, CLIP, and ViT. The study compares full fine‑tuning, linear probing, and Low‑Rank Adaptation (LoRA) across these backbones on the ODIR dataset and external validation on APTOS, achieving high internal and external AUROC scores while also evaluating model interpretability through Grad‑CAM and HiResCAM against expert lesion masks.

## Key Takeaways
- DINOv2‑LoRA reaches the highest internal AUROC of 0.758, showing that parameter‑efficient LoRA can outperform full fine‑tuning for this task.  
- Full fine‑tuning of DINOv2 and ViT yields the best external AUROC of 0.920, indicating strong generalization to new clinical data.  
- Explainability metrics such as Dice, IoU, and Pointing Game demonstrate that attention maps align with clinically relevant retinal lesions when using expert annotations.

## Context
Vision foundation models have become central to medical image analysis because they capture rich visual representations from large datasets. Their efficiency enables rapid adaptation to specialized tasks like diabetic retinopathy screening without the computational cost of training from scratch. This work contributes to the growing body of literature that couples model performance with transparent decision making for clinical adoption.

## Implications
For clinicians, explainable models reduce reliance on black‑box predictions and increase trust in automated screening tools. For developers, LoRA offers a scalable path to fine‑tuning foundation models while preserving interpretability, supporting deployment in resource‑constrained healthcare settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28207v1)
