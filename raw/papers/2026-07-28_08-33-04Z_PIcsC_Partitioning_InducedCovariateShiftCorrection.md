---
title: PIcsC: Partitioning-Induced Covariate Shift Correction
published: 2026-07-28T08:33:04Z
authors: Behraj Khan, Behroz Mirza, Syed Ahmad Chan Bukhari, Tahir Qasim Syed
url: http://arxiv.org/abs/2607.25441v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PIcsC: Partitioning-Induced Covariate Shift Correction

## Abstract
Covariate shift across training-data partitions biases model selection and parameter estimation in cross-validation, lifelong learning, and federated learning. We propose \textit{Partition-Induced Covariate-shift Correction} (\texttt{PIcsC}), a Fisher information-based regularization framework that mitigates distribution mismatch between data partitions and a reference distribution. \texttt{PIcsC} approximates partition divergence using the Fisher Information Matrix (FIM) and incorporates the resulting statistic as a regularizer during optimization. The same formulation applies to both centrally partitioned datasets (batches or cross-validation folds) and inherently distributed data (federated clients or decentralized nodes), requiring only partition-local gradient statistics rather than raw data. We further introduce a conditional adaptation mechanism that combines FIM shift with KL divergence to detect significant distribution shifts and activates regularization only when necessary. Experiments on more than 40 datasets demonstrate consistent improvements under both natural and synthetic covariate shift. On fragmented batch and fold settings, \texttt{PIcsC} reduces fragmentation-induced performance degradation by more than 20\% and 25\%, respectively. On seven federated learning benchmarks, it consistently outperforms FedAvg, FedProx, and SCAFFOLD by 3 -5 percentage points without requiring client-specific personalization. These results demonstrate that Fisher information provides an effective and unified mechanism for mitigating partition-induced covariate shift across both centralized and distributed learning.

## Metadata
- **Published**: 2026-07-28T08:33:04Z
- **Authors**: Behraj Khan, Behroz Mirza, Syed Ahmad Chan Bukhari, Tahir Qasim Syed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25441v1)