---
title: Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal Prediction
published: 2026-08-06T15:59:57Z
authors: Anton Conrad, Rustam Isaev, Denis Belomestny, Eric Moulines, Sergey Samsonov
url: http://arxiv.org/abs/2608.06206v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Marginal Validity: Finite-Sample Guarantees for Localized Conformal Prediction

## Abstract
Conformal prediction endows arbitrary black-box predictors with finite-sample, distribution-free marginal coverage, yet marginal validity can hide severe covariate-specific miscalibration, while exact distribution-free conditional coverage is finite-sample unattainable. Randomly localized conformal prediction (RLCP) mitigates this gap by calibrating near the test point while preserving marginal coverage. Existing theory, however, lacks finite-sample guarantees for the realized localized set that jointly control conditional validity and oracle efficiency. We provide such guarantees. For any fixed score, under Hölder regularity of the conditional score CDF and standard density and kernel assumptions, we prove high-probability bounds, uniform over a realized localization neighbourhood, for the conditional-coverage gap and the length error relative to the oracle. The bounds decompose into an $O(h^β)$ localization bias and a calibration term decreasing with calibration size, clarifying the bandwidth bias-variance tradeoff and when RLCP tracks the oracle. We also analyze data-split learned scores: when the score targets a pivotal score, as in conformalized quantile regression, uniform local guarantees decompose into fixed-score calibration and uniform score-estimation errors, showing that improved learning sharpens localized guarantees.

## Metadata
- **Published**: 2026-08-06T15:59:57Z
- **Authors**: Anton Conrad, Rustam Isaev, Denis Belomestny, Eric Moulines, Sergey Samsonov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06206v1)