---
title: ARC: Augmented-Rank Conformalization for Changepoint Localization --- Finite-Sample Validity and Distribution-Robust Efficiency
published: 2026-08-09T02:44:08Z
authors: Chenchen Peng, Mixia Wu, Qijing Yan, Zhiqi Shen, Jie Zhang
url: http://arxiv.org/abs/2608.08424v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARC: Augmented-Rank Conformalization for Changepoint Localization --- Finite-Sample Validity and Distribution-Robust Efficiency

## Abstract
Conformal changepoint localization turns any score into a confidence set for the changepoint with finite-sample coverage. Coverage is universal; efficiency is not. The oracle score is a likelihood ratio, so practical scores estimate density ratios, and set length deteriorates under heavy tails, skewness, and distribution shift, where no length guarantee applies. We propose ARC (Augmented-Rank Conformalization), a family of scores depending on the data only through within-segment ranks: rank-CUSUM location and scale channels, their fixed combinations, and a lightweight neural score frozen after synthetic training. Every ARC score inherits finite-sample coverage for every frozen weight configuration, including random initialization and mistraining. The main result is an efficiency transfer theorem: the entire ARC confidence set is almost surely invariant under strictly increasing marginal transforms, so the set length distribution depends on the data pair only through its rank structure, and lengths certified once hold verbatim across its monotone orbit, whereas a plug-in score's length changes with every re-expression. Across different rank structures lengths do change, and are reported as such. Classical rank-test theory positions ARC as targeting the optimal invariant score at bounded cost. Simulations confirm nominal coverage for all scores, including sabotaged networks, identical sets under monotone transforms where plug-in scores inflate, and smooth degradation where plug-in sets become vacuous; on the well-log benchmark ARC localizes annotated shifts to three to five candidates and flags misfit by an empty set. Two boundaries are stated rather than hidden: serial dependence destroys exactness, and trend-type alternatives lie outside the piecewise-exchangeable model.

## Metadata
- **Published**: 2026-08-09T02:44:08Z
- **Authors**: Chenchen Peng, Mixia Wu, Qijing Yan, Zhiqi Shen, Jie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08424v1)