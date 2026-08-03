---
title: Who Wins Where? Conformal Model Comparison for Local Superiority
published: 2026-07-31T06:10:54Z
authors: Yi Zhou, Baishi Li, Xuan Yao, Ke-Wei Huang
url: http://arxiv.org/abs/2607.29053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Wins Where? Conformal Model Comparison for Local Superiority

## Abstract
Standard model comparison is global, aggregating losses across the covariate space to declare a single winner. This can obscure heterogeneous performance, where different models are preferable in different regions. We introduce conformalized local model comparison, a split-sample framework for constructing calibrated local best-model maps. Given a model comparison score, such as the difference between two squared losses, the method uses three disjoint splits to fit competing models, estimate local centers and scales from out-of-sample scores, and conformally calibrate residual uncertainty. At a target point, the procedure declares a local winner only when a one-sided conformal bound excludes a tie, with the score's sign determining the favored model. We prove finite-sample marginal control for one-sided erroneous declarations on the realized future comparison score, establish pointwise consistency of the localized mean-score estimator away from tie boundaries, show that aggregate comparison can disagree sharply with the prevalence of local superiority, and derive a squared-loss bias--variance decomposition that clarifies how model structure affects local wins. Synthetic and real-data experiments show that the method recovers heterogeneous winner regions, abstains under uncertainty, and yields higher conditional gain than global selection.

## Metadata
- **Published**: 2026-07-31T06:10:54Z
- **Authors**: Yi Zhou, Baishi Li, Xuan Yao, Ke-Wei Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29053v1)