---
title: TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH
published: 2026-08-17T11:06:16Z
authors: Yu-Han Huang, Yujia Wu, Vincent S. Tseng
url: http://arxiv.org/abs/2608.16410v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH

## Abstract
Combined algorithm selection and hyperparameter optimization (CASH) searches a conditional space in which the selected model determines which hyperparameters are active. In time-series forecasting, temporal choices, chronological validation, and costly evaluations further complicate this search. Controlled comparisons of heterogeneous search methods under a shared time-series CASH (TS-CASH) evaluation protocol remain limited. Within this setting, we study TRACECASH, a task-local hybrid sequential optimizer combining grouped actor-critic candidate generation with fixed rules for model coverage, validation-guided exploitation, and exploration after stalled progress. A model actor proposes an initial forecasting model; three model-conditioned actors generate temporal, architectural, and training actions; and a modelspecific decoder constructs the configuration ultimately evaluated. We compare TRACE-CASH with six alternatives spanning random, Bayesian, evolutionary, multi-objective, and language-model-assisted search across 41 dataset-frequency task variants. TRACE-CASH has the lowest mean rank on both MASE and WQL. Descriptively, it also has the lowest window-averaged test-MASE rank in the predefined full and late windows. These results support the complete TRACECASH procedure as competitive among the evaluated methods.

## Metadata
- **Published**: 2026-08-17T11:06:16Z
- **Authors**: Yu-Han Huang, Yujia Wu, Vincent S. Tseng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16410v1)