---
title: From Recoverability to Functional Use: Certifying Temporal Reports in Time-Series Forecasting
published: 2026-08-11T03:30:36Z
authors: Qipeng Qian, Yuntao Qian
url: http://arxiv.org/abs/2608.10433v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Recoverability to Functional Use: Certifying Temporal Reports in Time-Series Forecasting

## Abstract
Temporal reports are increasingly emitted alongside numerical forecasts and are often interpreted as statements about the computation producing those forecasts. We formalize the resulting certification problem as three distinct stages: \emph{recoverability}, \emph{report correctness}, and \emph{functional use}. For point delays, an exact finite-sample recovery--substitutability identity ties structural discrimination and proxy prediction to the same realized shift geometry while placing them on different scales: structural evidence grows with $nη_n$, whereas the normalized predictive penalty is governed by $η_n$. A delay can therefore be statistically decisive while an alternative lag remains near-oracle. Guided by this regime, we evaluate TCN- and N-HiTS-based systems on the strict intersection of recoverable trajectories, correct reports, and near-oracle one-step predictions. Their dominant forecast dependence remains far from the reported delay under masking, finite perturbations, local Jacobians, and in-distribution conditional replacement, and the separation persists across a 100-fold forecast-loss sweep. A no-bypass factorization then provides an explicit access certificate for the final stage, while architecture-matched multi-seed, post-hoc, and gate-destruction controls identify report-coordinate access as the mechanism governing alignment. The resulting framework separates statistical evidence for \emph{what can be identified} from computational evidence for \emph{what the forecast uses}.

## Metadata
- **Published**: 2026-08-11T03:30:36Z
- **Authors**: Qipeng Qian, Yuntao Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10433v2)