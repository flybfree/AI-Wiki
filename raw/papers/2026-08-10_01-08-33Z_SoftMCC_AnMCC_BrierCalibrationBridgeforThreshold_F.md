---
title: SoftMCC: An MCC-Brier Calibration Bridge for Threshold-Free Model Selection under Class Imbalance
published: 2026-08-10T01:08:33Z
authors: Özkan Canay
url: http://arxiv.org/abs/2608.08984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoftMCC: An MCC-Brier Calibration Bridge for Threshold-Free Model Selection under Class Imbalance

## Abstract
Model selection for imbalanced binary classification often uses the Matthews correlation coefficient (MCC), but thresholding makes validation rankings threshold-dependent. SoftMCC is a post-training MCC validation framework on established probability-valued confusion counts, coupling an MCC-specific calibrated identity with a tie-aware, shared-pool selection protocol. Its core score is a covariance-normalized probability-label association, reduces exactly to MCC for hard predictions, and is Pearson-bounded. Under perfect population calibration it equals the Brier skill score with identical candidate ordering; outside that regime the gap does not identify calibration error. Across 18 settings with 12 duplicate-safe grouped repeats, SoftMCC attains the best stability mean rank (2.31) and highest mean tie-corrected Kendall's W (0.659), with a significant Friedman test (p=0.007); Nemenyi analysis separates it from AUPRC and MCC@0.5, while 14-source-family sensitivity retains only the latter. Selected-model utility shows no advantage. Three of six prespecified comparisons have negative mean test-MCC differences, only F1@best survives Holm correction (p=0.014), and the dataset-level test is not significant (p=0.117). Label permutation lowers mean W to 0.092; temperature scaling shifts SoftMCC rankings (mean Spearman 0.851) whereas rank-based and threshold-optimized metrics remain invariant. SoftMCC is a calibration-sensitive MCC-family selector with bounded stability and utility evidence.

## Metadata
- **Published**: 2026-08-10T01:08:33Z
- **Authors**: Özkan Canay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08984v1)