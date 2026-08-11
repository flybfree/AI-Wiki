---
title: A Domain-Structured Ensemble Framework for Perioperative Outcome Prediction Using Electronic Health Record Data
published: 2026-08-09T21:15:12Z
authors: Shikhar Shukla, Cristina Barboi
url: http://arxiv.org/abs/2608.08920v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Domain-Structured Ensemble Framework for Perioperative Outcome Prediction Using Electronic Health Record Data

## Abstract
Perioperative risk prediction models are often limited by narrow surgical populations, incomplete intraoperative data, poor calibration, and limited interpretability. We present a domain-structured ensemble framework for perioperative outcome prediction using routinely collected electronic health record (EHR) data. Predictors are organized into patient-related, surgery-related, and anesthetics-related domains. Domain-specific gradient boosting models generate independent risk estimates that are integrated through a logistic regression meta-learner. We demonstrate the framework using postoperative delirium (POD) in a case-control sample of 5,386 surgical encounters (2,693 cases, 2,693 controls) from a statewide health information exchange. POD required both delirium-related ICD codes and a positive Confusion Assessment Method screening within seven postoperative days; patients with preexisting dementia were excluded. The stacked meta-learner achieved AUROC 0.899 (95% CI: 0.891-0.906), precision-recall AUC 0.881, and Brier score 0.126, compared with AUROC 0.849 for the best single-stage model. Domain ablation showed improved discrimination and calibration over a surgery-only model (AUROC 0.879, Brier 0.140). Temporal validation on held-out post-2017 data yielded AUROC 0.915. Calibration was excellent, with intercept -0.006 (95% CI: -0.083 to 0.070) and slope 1.035 (95% CI: 0.982 to 1.088). Decision curve analysis, corrected for case-control sampling, showed positive net benefit across clinically plausible thresholds. The modular framework supports alternative outcomes, extension of predictor domains, and dynamic risk updating, providing a scalable foundation for interpretable, calibration-aware perioperative clinical decision support.

## Metadata
- **Published**: 2026-08-09T21:15:12Z
- **Authors**: Shikhar Shukla, Cristina Barboi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08920v1)