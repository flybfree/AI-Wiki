---
title: CorePath: A Breast-Specialized Pathology Foundation Model for Core Needle Biopsy Diagnosis and Risk-Controlled Report Generation
url: http://arxiv.org/abs/2608.03079v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_03-43-49Z_CorePath_ABreast_SpecializedPathologyFoundationMod.md
generated_at: 2026-08-05 01:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
CorePath is a breast-specialized foundation model built from PRISM fine‑tuned on 7901 paired CNB whole‑slide images and reports, achieving high performance across detection, invasion assessment, and subtyping without task‑specific retraining. It outperformed existing models in AUCs ranging from 0.9526 to 0.9735 for five‑class histopathology subtyping on private data and set new benchmarks of 0.7780–0.8252 on public benchmarks, while also reducing non‑breast hallucinations in report generation from 30.1% to 2.8%.

## Key Takeaways
- CorePath’s breast‑focused adaptation yields AUCs between 0.9526 and 0.9735 for five‑class CNB subtyping on private cohorts, far exceeding baseline PRISM performance.
- On public benchmarks it reaches the highest weighted AUCs of 0.7780 for BCNB invasive carcinoma subtyping, 0.8178 for BRACS lesion stratification, and 0.8252 for fine‑grained classification.
- The model cuts non‑breast hallucinations in report generation to 2.8%, showing significant improvement after domain specialization.

## Context
Foundation models are increasingly applied to medical imaging, but most are generic and require task‑specific fine‑tuning. CorePath demonstrates that a breast‑specialized model can achieve state‑of‑the‑art results without additional training, highlighting the potential for efficient, high‑performing AI in pathology.

## Implications
This work offers clinicians a reliable diagnostic assistant that reduces false reports and supports risk‑controlled release of subtype information. It also provides a template for domain‑specific foundation models to be deployed across multiple centers with minimal data overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03079v1)
