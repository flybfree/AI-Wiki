---
title: Beyond Aggregate Calibration: Decomposing Income-Conditional Recall Disparities in Automated Credit Default Prediction
published: 2026-08-08T15:57:15Z
authors: Sai Srikar Boddupalli
url: http://arxiv.org/abs/2608.08202v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Aggregate Calibration: Decomposing Income-Conditional Recall Disparities in Automated Credit Default Prediction

## Abstract
Data-centric curation pipelines frequently rely on model confidence scores to flag and filter noisy or mislabeled training instances. Evaluating this filtering convention on a large-scale consumer lending sample (LendingClub, N = 1,344,936) uncovers an underlying demographic asymmetry: high-income defaulters are disproportionately classified as label noise relative to low-income defaulters (Cramer's V approximately 0.03-0.07). Re-examining this behavior through the lens of equal opportunity [Hardt et al., 2016] reveals a far more severe discrepancy: a 16.86 percentage point gap in true positive rate (recall) between high- and low-income borrowers who ultimately defaulted. Implementing a sequential feature-blinding methodology allows us to isolate the drivers of this disparity across three distinct mechanisms: (1) direct reliance on self-reported applicant income; (2) algorithmic absorption of upstream institutional bias encoded within origination interest rates; and (3) a residual disparity (3.55 percentage points in cross-validation; 2.56 percentage points on a held-out test partition, Z = -4.04, p < 0.0001) that remains even after purging both income and interest rates from the model. Out-of-sample signed SHAP valuations demonstrate that this residual gap is maintained by structural proxies, most notably loan amount and home ownership status. These empirical findings show that simply blinding an algorithm to sensitive attributes fails to ensure fairness when institutional pricing decisions and behavioral proxy variables collectively reconstruct the omitted signals. We outline the practical implications of these findings for auditing data-centric AI workflows within regulated financial institutions.

## Metadata
- **Published**: 2026-08-08T15:57:15Z
- **Authors**: Sai Srikar Boddupalli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08202v1)