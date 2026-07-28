---
title: Bayesian Complete-Pooling in Cross-Subject Classification for Motor Imagery Electroencephalogram
published: 2026-07-25T01:35:16Z
authors: Ethan Davis
url: http://arxiv.org/abs/2607.22980v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bayesian Complete-Pooling in Cross-Subject Classification for Motor Imagery Electroencephalogram

## Abstract
Brain-computer interfaces (BCIs) have long sought calibration-free operation, but classifiers are typically benchmarked by discrimination alone, blind to whether predicted probabilities are well calibrated - a meaningful gap given nonstationary electroencephalogram (EEG) signals and the risk of overconfident point-estimate classifiers under distribution shift. We conducted a large-scale study contrasting Bayesian complete-pooling models against frequentist baselines for cross-subject, left-hand versus right-hand motor imagery EEG classification across 20 datasets. Six frequentist pipelines were each paired with an analogous Bayesian pipeline sharing identical feature engineering, fit via Markov chain Monte Carlo posterior sampling. Our primary metric was the Brier score, decomposed into reliability and resolution, alongside AUROC for discrimination and Shannon entropy for sharpness. Each metric was analyzed via random-effects meta-analysis (REML, Knapp-Hartung adjustment), verified by leave-one-out influence analysis. Bayesian complete-pooling produced statistically but not practically significant improvements in reliability and increases in predictive uncertainty (lower sharpness); Brier score, resolution, and discrimination showed no significant differences. Between-study heterogeneity was low across all metrics, though the reliability result was sensitive to leave-one-out removal. We additionally profiled computational cost, finding that Bayesian pipelines consumed roughly thirteen times more energy than their frequentist counterparts, a cost that remains modest relative to common household appliances. These results suggest that Bayesian complete-pooling alone offers limited practical benefit for cross-subject motor imagery classification, and that partial-pooling across subjects and sessions is a more promising direction for future work.

## Metadata
- **Published**: 2026-07-25T01:35:16Z
- **Authors**: Ethan Davis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22980v1)