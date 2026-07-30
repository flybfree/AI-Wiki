---
title: Simultaneous Coverage and Efficiency Guarantee in Online Conformal Prediction
published: 2026-07-29T07:56:59Z
authors: Rahul Vaze
url: http://arxiv.org/abs/2607.26577v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simultaneous Coverage and Efficiency Guarantee in Online Conformal Prediction

## Abstract
Adaptive conformal inference (ACI) of Gibbs and Cand{è}s and its variants are the standard approach to online conformal prediction under distribution shift, but they suffer from three fundamental limitations. First, their guarantees control only the \emph{signed} long-run coverage error: persistent miscoverage in one direction can be masked by compensating errors later, so a method can satisfy the theoretical guarantee while being badly wrong for extended periods. Second, existing guarantees say nothing about prediction-set size, so validity can be achieved trivially at the cost of unduly wide prediction sets. Third, the efficiency guarantees that do exist compare against a \emph{fixed} predictor chosen in hindsight, a benchmark that becomes increasingly less meaningful once the data-generating distribution shifts, since the very notion of an optimal threshold then changes over time.   We consider a unified online learning framework that simultaneously controls absolute, non-cancelling coverage violation and prediction-set efficiency against a dynamically evolving benchmark for three important models. In the fully adversarial setting, exploiting the fact that the standard ACI update is exactly projected online gradient descent on the pinball loss, we derive simultaneous coverage and efficiency guarantees for arbitrary monotone Lipschitz efficiency objectives, with no distributional or {\it convexity} assumptions. In the stochastic setting with full-score feedback, we propose a sliding-window quantile tracker and establish a matching minimax lower bound showing our algorithm is rate-optimal. In the covariate-dependent stochastic setting, we develop a partitioned ACI algorithm that tracks a function-valued oracle threshold, and derive simultaneous coverage and efficiency guarantees.

## Metadata
- **Published**: 2026-07-29T07:56:59Z
- **Authors**: Rahul Vaze
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26577v1)