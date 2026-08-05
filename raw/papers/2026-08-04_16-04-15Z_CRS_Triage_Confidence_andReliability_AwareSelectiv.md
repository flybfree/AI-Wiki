---
title: CRS-Triage: Confidence- and Reliability-Aware Selective Triage under Incomplete Clinical Evidence
published: 2026-08-04T16:04:15Z
authors: Guan Qiang, Yushen Chen, Tianlong Liu, David Rotenberg, Ethan H. Kim, Fang Fang
url: http://arxiv.org/abs/2608.03862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRS-Triage: Confidence- and Reliability-Aware Selective Triage under Incomplete Clinical Evidence

## Abstract
Emergency triage requires reliable decisions within a short time period. However, the available electronic health record (EHR) data, including structured data and clinical text, are often incomplete, unreliable, and inconsistent. This makes machine learning (ML)-based triage prediction more challenging, as existing ML models typically rely on complete and reliable EHR data to accurately predict patients' acuity levels. To address this, we propose confidence- and reliability-aware selective triage (CRS-Triage) to predict patients' acuity levels with a confidence score. By comparing the confidence score with a predefined threshold, CRS-Triage can selectively determine whether the model should make the decision or defer the case. Specifically, CRS-Triage separately evaluates the reliability of structured data and clinical text and then jointly considers the consistency between the two modalities to estimate the confidence of each prediction. Moreover, to reduce the risk of missing high-acuity patients, namely under-triage, CRS-Triage prefers to assign patients slightly higher acuity levels, namely over-triage, by penalizing under-triage errors. Experiments on the MIMIC-IV-ED dataset show that CRS-Triage achieves strong predictive performance. It also provides a better risk-coverage trade-off and remains reliable when the available EHR data are incomplete, degraded, or inconsistent across modalities.

## Metadata
- **Published**: 2026-08-04T16:04:15Z
- **Authors**: Guan Qiang, Yushen Chen, Tianlong Liu, David Rotenberg, Ethan H. Kim, Fang Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03862v1)