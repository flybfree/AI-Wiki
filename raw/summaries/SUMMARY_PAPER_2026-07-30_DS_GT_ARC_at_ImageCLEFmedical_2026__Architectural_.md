---
title: DS@GT ARC at ImageCLEFmedical 2026: Architectural Diversity for Concept Detection and Foundation-Model Scaling for Caption Prediction in Medical Image Analysis
url: http://arxiv.org/abs/2607.27763v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_07-01-49Z_DS_GTARCatImageCLEFmedical2026_ArchitecturalDivers.md
generated_at: 2026-07-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents the DS@GT submissions for the ImageCLEFmedical Caption 2026 challenge, which evaluates both concept detection and caption prediction on the ROCOv2 dataset. The authors achieved top rankings in concept detection using a three‑way ensemble of ConvNeXt‑V2, BiomedCLIP ViT‑B/16, and DenseNet‑169 with Honest Threshold Tuning, while their KNN retrieval pipeline matched fine‑tuned results at lower cost. For caption prediction they explored models ranging from the zero‑shot MedGemma‑4B to fully fine‑tuned BLIP pipelines.

## Key Takeaways
- The ensemble of ConvNeXt‑V2, BiomedCLIP ViT‑B/16, and DenseNet‑169 with Honest Threshold Tuning reached a primary F1 of 0.5790 and secondary F1 of 0.9657, ranking first on the official submission for concept detection.
- A training‑free KNN retrieval over frozen BiomedCLIP embeddings achieved nearly identical F1 scores (primary 0.5780, secondary 0.9599), demonstrating that retrieval can match fine‑tuned models with minimal computational expense.
- The caption prediction results span a wide model scale spectrum, from MedGemma‑4B at 0.3186 to fully fine‑tuned BLIP at 0.3564, highlighting the trade‑off between size and performance.

## Context
The ImageCLEFmedical Caption challenge continues the trend of integrating concept detection with natural‑language generation in medical imaging, a critical area for clinical decision support. This work illustrates how architectural diversity can be harnessed to balance accuracy and efficiency, especially when dealing with rare concepts that are difficult to capture by standard fine‑tuning.

## Implications
For researchers, the findings suggest that hybrid approaches combining strong vision encoders with lightweight retrieval mechanisms can outperform pure fine‑tuned models without sacrificing performance. Clinically, these results point toward more scalable and cost‑effective caption generation pipelines that could be deployed in real‑world medical imaging workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27763v1)
