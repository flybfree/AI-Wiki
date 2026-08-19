---
title: Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease
url: http://arxiv.org/abs/2608.17370v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_04-59-46Z_PathologyTransport_Optimal_TransportExplanationsfo.md
generated_at: 2026-08-18 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an optimal‑transport based framework that models the distributions of healthy and diseased patients to generate label‑free explanations for clinical AI. Experiments on breast cancer biomarkers show high AUROC scores and agreement with supervised methods, while chest X‑ray experiments reveal a gap between synthetic heatmaps and true disease localisation.

## Key Takeaways
- The optimal‑transport rectified flow produces per‑patient counterfactuals and an unsupervised malignancy score with AUROC 0.91 across five seeds, demonstrating strong predictive performance.
- Heatmap explanations derived from the transport model are population‑level signals rather than localisers of disease, especially when applied to real radiologist annotations where they perform at chance.
- A reconstruction‑based variant achieves moderate localisation on synthetic lesions but collapses to random predictions on actual RSNA boxes, highlighting a synthetic‑to‑real gap.

## Context
Generative AI explanations aim to replace black‑box classifiers with geometry between patient distributions. This work tests whether such geometric insights can be trusted as disease localisers in clinical settings, addressing a longstanding concern about the validity of label‑free attribution methods.

## Implications
For practitioners, this research warns against assuming that visually appealing heatmaps guarantee accurate localisation, urging rigorous validation against ground truth. For industry, it provides a reusable transport recipe and benchmark to evaluate explainability claims, guiding responsible deployment of AI diagnostics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17370v1)
