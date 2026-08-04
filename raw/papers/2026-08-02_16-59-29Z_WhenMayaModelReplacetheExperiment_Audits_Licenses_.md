---
title: When May a Model Replace the Experiment? Audits, Licenses, and the Price of Trust in Surrogate-Driven Design
published: 2026-08-02T16:59:29Z
authors:  Shuangxiu,  Ma,  Wenhe,  Zhao
url: http://arxiv.org/abs/2608.01378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When May a Model Replace the Experiment? Audits, Licenses, and the Price of Trust in Surrogate-Driven Design

## Abstract
Design campaigns in chemistry, materials science, and machine learning share a bottleneck: determining how good a candidate truly is requires an expensive evaluation - an experiment, a first-principles simulation, or a full training run. Machine-learning surrogates that predict these outcomes are increasingly used not only to propose candidates but to grade them, and even to feed their own predictions back into the search as though they were measurements. Through mathematical analysis validated on three exhaustively ground-truthed design tasks, we establish when this practice is safe, what any certificate of safety must cost, and when the substitution provably pays. Predictive accuracy cannot anchor trust: near-perfect R^2 is compatible with worst-possible selections, and screening N candidates inflates the over-prediction at the selected candidate by a quantifiable "selection tax" with matching upper and lower bounds. Safety follows instead from an architectural rule - predictions may propose and train without restriction, but every certified conclusion must rest on true evaluations - which is sufficient with no assumptions on the surrogate, and necessary, since admitting predictions into certification with the standing of measurements opens a deterministic self-confirmation failure mode. We derive the minimal criterion under which a model may act as an oracle (rank preservation, not accuracy), show that trust must be purchased through selection-aware audits that are optimal in query complexity, and prove a dichotomy fixing when audited surrogates cut certified evaluation cost. Across 432 surrogate fits over six task-regime conditions, the audit statistic tracks deployed search performance at Spearman rank correlation 0.80-0.99, while the rank correlation of R^2 with deployed regret falls as low as 0.33; audited screening reduces certified oracle cost by a measured factor of 25.

## Metadata
- **Published**: 2026-08-02T16:59:29Z
- **Authors**:  Shuangxiu,  Ma,  Wenhe,  Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01378v1)