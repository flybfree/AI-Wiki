---
title: Why Does the Future Branch? Identifiable Closure Tests for Stochastic Physical World Models
published: 2026-08-01T11:07:24Z
authors: Yibin Dong
url: http://arxiv.org/abs/2608.00591v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Does the Future Branch? Identifiable Closure Tests for Stochastic Physical World Models

## Abstract
Stochastic world models are usually evaluated by the accuracy and calibration of their predicted futures. These criteria leave a decision-relevant ambiguity: the same conditional future distribution can arise because an observation aliases different physical states, or because the dynamics remain random after the declared full state is fixed. We prove that this attribution is not identifiable from ordinary transition data, even with an optimal probabilistic predictor. We introduce ClosurePairs, an interventional evaluation protocol that crosses compatible microstates with repeated exogenous disturbances. A two-way variance decomposition identifies state aliasing, process noise, and their nonlinear interaction; an independent-repeat variant applies when disturbances cannot be reused. On likelihood-equivalent Gaussian systems, paired supervision reduces alias-fraction error 15.96-fold at identical test NLL. Across 18 nonlinear Langevin conditions, it reduces attribution MAE from 0.372 to 0.051 and sensing regret from 0.0138 to 0.0003 without changing NLL. On a pixel-conditioned recurrent model, a frozen shared-state probe reduces alias-fraction MAE against a deep ensemble from 0.584 to 0.130 in distribution and from 0.630 to 0.170 out of distribution over ten seeds. Finally, in a matched-total-variance REFINE/BRANCH test, a total-variance router reaches 66.48 percent plus or minus 1.06 percent accuracy, whereas ClosurePairs reaches 99.99 percent plus or minus 0.02 percent and improves selected NLL from -2.087 to -2.717 over five seeds. ClosurePairs therefore measures why futures branch, information that proper forecast scores cannot identify.

## Metadata
- **Published**: 2026-08-01T11:07:24Z
- **Authors**: Yibin Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00591v1)