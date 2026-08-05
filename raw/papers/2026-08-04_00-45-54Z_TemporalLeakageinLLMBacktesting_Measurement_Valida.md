---
title: Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores
published: 2026-08-04T00:45:54Z
authors: Zeyu Zhang, Bradly C. Stadie
url: http://arxiv.org/abs/2608.02985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Temporal Leakage in LLM Backtesting: Measurement, Validation, and Adjusted Scores

## Abstract
The standard check for contamination in LLM backtests is simple: compare scores before and after the training cutoff. We show this check is uninformative. Four flagship models fail it on questions they cannot have memorized: every scored question resolved after their cutoffs. The reason is structural. Models legitimately know more about times near their cutoff, so recency mimics leakage, and we prove no passive backtest can separate the two from genuine skill. Measurement, not just detection, requires information from outside the backtest. We supply it in two forms. A known cutoff identifies leakage at the boundary; a matched clean control identifies it globally and yields a leakage-adjusted score. We also derive where leakage hides: it concentrates on outcomes that surprised the crowd and were well covered in training, and partial memorization is disproportionately rewarded. We validate the estimators against ground truth by planting leakage in twin models, where they recover the injected dose and return null on clean questions. Deployed on frontier models, they detect one cutoff-localized signature and, at the audit's power floor, clear five models whose apparent advantages were recency alone. Backtests need not be discarded; they need one defensible reference.

## Metadata
- **Published**: 2026-08-04T00:45:54Z
- **Authors**: Zeyu Zhang, Bradly C. Stadie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02985v1)