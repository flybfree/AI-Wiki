---
title: PDD-RRG: Posterior Diagnostic Decision for Study-level Radiology Report Generation
published: 2026-08-04T03:12:34Z
authors: Yang Yu, Yiming Ji, Bin Dai, Dong Zhang, Zhiyong Zhou, Shoushan Li, Yakang Dai
url: http://arxiv.org/abs/2608.03055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PDD-RRG: Posterior Diagnostic Decision for Study-level Radiology Report Generation

## Abstract
Automatic radiology report generation (RRG) aims to simulate the workflow of radiologists, assisting them in clinical diagnosis. However, existing methods often fall short in utilizing all information relevant to the examination, as is typically done in clinical practice. Although some works attempt to incorporate multi-view images and historical data, these additional inputs may sometimes lead to avoidable diagnostic errors on the contrary. To address these challenges, we introduce a decision-making stage after report generation for the first time and propose a Posterior Diagnostic Decision framework (PDD-RRG) to integrate potentially conflicting diagnoses. Specifically, we create various subsets of input data and utilize an existing RRG model to generate reports from different perspectives. Then the Bayesian posterior probability and the learned thresholds for each clinical observation are calculated to obtain an aggregated diagnostic conclusion, which is subsequently used to refine the generated report. Experiments on MIMIC-CXR demonstrate that our proposed PDD-RRG can effectively enhance the clinical efficacy of existing RRG models without any retraining.

## Metadata
- **Published**: 2026-08-04T03:12:34Z
- **Authors**: Yang Yu, Yiming Ji, Bin Dai, Dong Zhang, Zhiyong Zhou, Shoushan Li, Yakang Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03055v1)