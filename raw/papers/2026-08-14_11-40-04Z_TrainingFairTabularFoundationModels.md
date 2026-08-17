---
title: Training Fair Tabular Foundation Models
published: 2026-08-14T11:40:04Z
authors: Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini, Samira Ebrahimi Kahou, Ulrich Aïvodji
url: http://arxiv.org/abs/2608.14211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Fair Tabular Foundation Models

## Abstract
Tabular Foundation Models (TFMs) have emerged as leading methods for tabular predictive tasks, leveraging in-context learning to predict on new data without task-specific training. Despite the increased use of TFMs in high-stakes decision-making, their fairness properties remain largely unexplored. In this work, we incorporate fairness constraints directly into TFM training, enabling fair predictions in a single forward pass. Our approach addresses two key challenges: limited access to sensitive attributes in training data, and the incompatibility of existing fairness techniques with the in-context learning paradigm. We propose FairTFM, a scalable training strategy based on synthetic fairness tasks and a fairness-aware architecture using a gradient reversal layer, which encourages the model to learn representations invariant to sensitive attributes. Experiments on 132 fairness tasks show consistent improvements in fairness while maintaining competitive accuracy.

## Metadata
- **Published**: 2026-08-14T11:40:04Z
- **Authors**: Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini, Samira Ebrahimi Kahou, Ulrich Aïvodji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14211v1)