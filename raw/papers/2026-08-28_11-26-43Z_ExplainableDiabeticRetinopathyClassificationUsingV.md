---
title: Explainable Diabetic Retinopathy Classification Using Vision Foundation Models
published: 2026-08-28T11:26:43Z
authors: Abhishek Verma, Anila Krishna, Abhishek Gajanan Bankar, Juan Miguel Lopez Alcaraz
url: http://arxiv.org/abs/2608.28207v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explainable Diabetic Retinopathy Classification Using Vision Foundation Models

## Abstract
Diabetic retinopathy (DR) is a major cause of preventable blindness, creating a need for accurate and trustworthy automated screening. This study investigates an explainable DR classification framework using vision foundation models and multiple transfer learning strategies. Three backbones, DINOv2, CLIP, and Vision Transformer (ViT), were evaluated using full fine-tuning, linear probing, and Low-Rank Adaptation (LoRA). Models were trained and internally evaluated on the ODIR dataset and externally evaluated on APTOS to assess generalization. DINOv2-LoRA achieved the highest internal AUROC of 0.758, while DINOv2 full fine-tuning and ViT full fine-tuning achieved the highest external AUROC of 0.920. Calibration was further assessed using reliability analysis after isotonic regression. For explainability, Grad-CAM and HiResCAM were evaluated against expert-annotated lesion masks from the IDRiD dataset using Dice, Intersection over Union (IoU), and Pointing Game metrics. The results demonstrate that foundation models, particularly DINOv2, can provide strong predictive performance, while LoRA offers a parameter-efficient alternative to full fine-tuning. Quantitative evaluation of explanation maps further supports the assessment of whether model attention corresponds to clinically relevant retinal lesions.

## Metadata
- **Published**: 2026-08-28T11:26:43Z
- **Authors**: Abhishek Verma, Anila Krishna, Abhishek Gajanan Bankar, Juan Miguel Lopez Alcaraz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28207v1)