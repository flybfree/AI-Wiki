---
title: Conformal Calibration for Multi-Modal Regression with Missing Modalities
published: 2026-08-07T22:38:35Z
authors: Ilia Azizi
url: http://arxiv.org/abs/2608.07795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformal Calibration for Multi-Modal Regression with Missing Modalities

## Abstract
Prediction intervals for multi-modal regression with tabular variables, text, images, or other input sources are difficult to calibrate when those sources disagree or one is missing. A single global quantile averages these regimes together instead of calibrating to the modality pattern observed at test time. We address this through a modality-aware conformal calibration layer. The layer trains or reuses one predictor per modality, computes a disagreement score from their predictions, and uses that score in split conformal calibration under a strict split protocol. We use the score in two complementary ways. First, a continuous disagreement-scaled method reallocates interval width across examples while preserving the usual marginal split-conformal guarantee. Second, a Mondrian (stratified) method calibrates within groups defined by disagreement or modality availability fixed before calibration, giving group guarantees under joint exchangeability of the calibration and test examples. Across four multi-modal datasets, the disagreement-scaled layer matches or improves the marginal conformal baseline in 59 of 60 paired runs for interval continuous ranked probability score (CRPS) and in 52 of 60 for interval width, while keeping empirical coverage near the 95% target. In stress tests with missing modalities, mask-matched recalibration recovers up to 19.5 percentage points of coverage in the hardest fixed-mask regime. The result is a simple, model-agnostic reliability layer for multi-modal regression systems. A project page is available at https://unco3892.github.io/modality-aware-conformal.

## Metadata
- **Published**: 2026-08-07T22:38:35Z
- **Authors**: Ilia Azizi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07795v1)