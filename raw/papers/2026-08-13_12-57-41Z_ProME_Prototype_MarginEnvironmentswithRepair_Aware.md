---
title: ProME: Prototype-Margin Environments with Repair-Aware Selection for Group-Robust Learning
published: 2026-08-13T12:57:41Z
authors: Qianqian Wang, Yunshan Li, Dawei Huang, Wenwu Gong, Lili Yang
url: http://arxiv.org/abs/2608.13190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProME: Prototype-Margin Environments with Repair-Aware Selection for Group-Robust Learning

## Abstract
Group-robust learning is crucial for maintaining accuracy on rare subpopulations when training-group labels are unavailable. However, existing methods often infer environments from a separate reference model and select representations before fitting the classifier used at deployment, leaving both decisions misaligned with the deployed predictor. In this work, we formulate group robustness without training-group labels as the endogenous environments with repair-aware selection (ERAS) problem, and propose ProME (Prototype-Margin Environments) to align both decisions with the deployed predictor. ProME splits prototype margins at their median to construct approximately balanced environments along the training trajectory, and fits a group-balanced linear head on group-annotated validation data to rank the resulting predictors by validation worst-group accuracy. We theoretically bound the worst risk across the inferred environments for a fixed predictor and partition, showing that this bound transfers to the oracle groups under an explicit alignment condition. Extensive experiments show that prototype margins enrich shortcut-conflicting examples, classifier repair reshapes candidate evaluation, and ProME achieves the highest average worst-group accuracy among the compared methods with the same group-label access.

## Metadata
- **Published**: 2026-08-13T12:57:41Z
- **Authors**: Qianqian Wang, Yunshan Li, Dawei Huang, Wenwu Gong, Lili Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13190v1)