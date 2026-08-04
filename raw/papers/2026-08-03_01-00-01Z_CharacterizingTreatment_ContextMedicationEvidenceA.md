---
title: Characterizing Treatment-Context Medication Evidence Across Clinic Notes and Structured EHR Medication History
published: 2026-08-03T01:00:01Z
authors: Mingyang Jiang, Congning Ni, Weixin Liu, Zhijun Yin
url: http://arxiv.org/abs/2608.01570v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Characterizing Treatment-Context Medication Evidence Across Clinic Notes and Structured EHR Medication History

## Abstract
Clinic notes and structured electronic health record (EHR) medication history often contain different medication information. Same-visit disagreement between these sources may result from note-side normalization errors, differences in terminology or timing, or actual differences in documentation. We developed a note-grounded approach that uses large language model (LLM) assisted reference construction, targeted and random human review, deterministic medication normalization, and semantic and temporal comparisons with structured medication history. We evaluated all normalization results on a patient-level held-out test set to limit adaptation to the study cohort. On 5,403 held-out mention rows, exact canonical agreement improved from 0.7226 with surface-exact matching to 0.8429 after lexical cleanup and curated alias mapping. In a random audit of previously unaudited rows, canonical-label agreement was 0.9210 among evaluable valid medication mentions, whereas treatment-action attribution was lower at 0.5326. In the full-cohort characterization analysis, only 16.44% of note-derived rows had same-visit exact overlap with structured medication history, but 55.17% had same-visit semantic overlap, 90.34% had same-visit or +/-30-day overlap, and only 3.97% remained in the strict no-structured-overlap bucket under broad project-level mapping. An ontology-backed sensitivity analysis further showed that held-out strict Observational Medical Outcomes Partnership (OMOP)-backed no-overlap fell from 43.99% to 36.68% after a development-derived alias supplement. These results show that note-to-structured-medication mismatch can arise from normalization errors, differences in terminology, and differences in documentation timing.

## Metadata
- **Published**: 2026-08-03T01:00:01Z
- **Authors**: Mingyang Jiang, Congning Ni, Weixin Liu, Zhijun Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01570v1)