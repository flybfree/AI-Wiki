---
title: Pretrained, Curriculum-Tuned, and Ensembled: A Tracer-Aware Interactive Segmentation Pipeline for AutoPET V
url: http://arxiv.org/abs/2608.30844v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_14-13-09Z_Pretrained_Curriculum_Tuned_andEnsembled_ATracer_A.md
generated_at: 2026-08-31 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces TRIAGE, a tracer‑aware interactive segmentation pipeline designed to segment lesions in whole‑body PET/CT scans from the AutoPET V challenge. The method combines a 3D STU‑Net backbone pre‑trained with masked autoencoding, an auxiliary organ segmentation model, and a dedicated tracer classifier that routes FDG or PSMA studies into separate branches while sharing a common processing pipeline. Curriculum‑style training and model ensembling are used to boost robustness across interaction steps.

## Key Takeaways
- The core backbone is a 3D STU‑Net initialized through masked autoencoding with an asynchronous masking strategy, aiming to learn transferable anatomical and cross‑modal representations before task‑specific fine‑tuning.  
- An auxiliary organ segmentation model provides explicit anatomical context that helps distinguish physiological uptake from malignant lesions during inference.  
- A tracer classifier routes each study to FDG or PSMA branches; the two branches share the same pipeline but are trained independently to account for tracer‑specific appearance and error modes.

## Context
Interactive lesion segmentation in PET/CT is challenging because corrective scribbles are sparse, and tracer distributions differ markedly between FDG and PSMA studies. Existing models often fail to adapt to these heterogeneous conditions, leading to suboptimal initial predictions that hinder refinement. This work addresses those limitations by integrating anatomy‑aware guidance and a curriculum‑driven training regimen.

## Implications
The pipeline’s ability to handle both FDG and PSMA modalities with independent yet unified training could improve diagnostic accuracy for clinicians relying on whole‑body scans. By emphasizing robustness across diverse cohorts, the approach may become a standard component of automated PET/CT analysis systems in clinical practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30844v1)
