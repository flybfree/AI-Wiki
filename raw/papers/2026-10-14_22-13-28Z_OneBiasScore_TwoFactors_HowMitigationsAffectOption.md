---
title: One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice Evaluation
published: 2026-10-14T22:13:28Z
authors: Hyunjong Ok, Minjae Park, Jaeho Lee
url: http://arxiv.org/abs/2610.20993v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice Evaluation

## Abstract
Reordering multiple-choice options can change a model's answer, an effect studied as selection bias (a preference for certain option letters) and as order sensitivity (changes in answers across option orderings). We connect these perspectives through the pooled selection-rate standard deviation (pooled SD), which measures how unevenly option letters are selected across questions and orderings. When every option of each question appears equally often at each position, the pooled SD is exactly the product of two label-free factors: the flip rate and the positional skew. The flip rate is the fraction of questions whose chosen option changes across orderings; the positional skew is the standard deviation of option-letter selection rates among those questions. Across 41 checkpoints and 12 benchmarks, the flip rate tracks accuracy and output uncertainty, while the positional skew tracks the estimated option-symbol prior. Prior correction for selection bias mainly reduces the positional skew. Aggregating each ordering with its reversal, a mitigation for order sensitivity, mainly reduces the flip rate. Both reduce the range of accuracy across correct-answer letters by similar amounts, but aggregation leaves fewer model-rank reversals. Applying prior correction before aggregation reduces both factors and further narrows this accuracy range. However, aggregation lowers the flip rate partly by settling questions on the same wrong option. We therefore recommend reporting both factors to distinguish mitigation effects, alongside accuracy to distinguish stability from correctness.

## Metadata
- **Published**: 2026-10-14T22:13:28Z
- **Authors**: Hyunjong Ok, Minjae Park, Jaeho Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20993v1)