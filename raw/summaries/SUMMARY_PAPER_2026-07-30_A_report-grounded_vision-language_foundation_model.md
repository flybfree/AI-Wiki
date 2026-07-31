---
title: A report-grounded vision-language foundation model for colonoscopy from 280000 routine reports
url: http://arxiv.org/abs/2607.28466v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-24-36Z_Areport_groundedvision_languagefoundationmodelforc.md
generated_at: 2026-07-30 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces EndoCLIP, a vision‑language foundation model for colonoscopy that extracts lesion information from routine reports and links it to individual frames. Trained on 125,756 image‑text pairs recovered from 280,476 colonoscopy records, the model outperforms existing encoders in retrieval, report generation, and classification tasks. The linear probe achieves performance comparable to expert readers in a blinded blind study.

## Key Takeaways
- lesion-level image‑text retrieval is enabled through structured report generation that couples each frame with its corresponding findings  
- the linear probe on benign versus malignant classification approaches the accuracy of 12 endoscopists, indicating strong clinical relevance  
- the dataset comprises 125,756 pairs derived from 280,476 routine reports, providing a massive source for scalable supervision  

## Context
Vision‑language models typically rely on generic datasets that do not capture domain‑specific medical imaging. This work demonstrates how routine clinical documentation can be transformed into a rich training resource, reducing the need for large annotated image sets in vision tasks.

## Implications
Clinicians can now specify diagnostic targets using natural language rather than manually annotating each frame, streamlining model development and deployment. The approach opens pathways to automated colonoscopy analysis that are scalable across institutions and supported by existing routine reports.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28466v1)
