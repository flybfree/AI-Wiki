---
title: CRS-Triage: Confidence- and Reliability-Aware Selective Triage under Incomplete Clinical Evidence
url: http://arxiv.org/abs/2608.03862v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_16-04-15Z_CRS_Triage_Confidence_andReliability_AwareSelectiv.md
generated_at: 2026-08-05 01:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CRS-Triage, a method that predicts patient acuity levels while providing a confidence score and selectively deciding when to use the model’s prediction. By evaluating both structured EHR data and clinical text separately and integrating their consistency, CRS-Triage generates reliable predictions even with incomplete or degraded information. Experiments on MIMIC-IV-ED demonstrate strong performance and improved risk‑coverage trade‑offs.

## Key Takeaways
- CRS-Triage assigns a confidence score to each prediction by comparing the reliability of structured data and clinical text, allowing it to defer decisions when confidence falls below a threshold.  
- The system prefers over‑triage to avoid under‑triaging high‑acuity patients, penalizing errors that could lead to missed critical cases.  
- Joint evaluation of modality consistency enhances overall confidence, making predictions more trustworthy despite missing or inconsistent EHR entries.

## Context
Machine learning triage systems often assume complete and reliable electronic health record data, which is rarely the case in real‑world emergency settings. This gap can degrade model accuracy and lead to unsafe clinical decisions. CRS-Triage addresses this limitation by incorporating uncertainty quantification and selective decision making.

## Implications
Practitioners can rely on CRS-Triage to complement human triage, reducing reliance on potentially flawed EHR inputs. The approach supports safer, more equitable emergency care by minimizing the risk of under‑triage while maintaining efficient workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03862v1)
