---
title: Conformal Fusion Under Missing Modalities
published: 2026-08-07T12:57:16Z
authors: Alireza Moayedikia
url: http://arxiv.org/abs/2608.07183v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformal Fusion Under Missing Modalities

## Abstract
Multimodal fusion architectures typically assume all modalities are available at inference, yet sensor failures, acquisition variability, and cost constraints routinely produce incomplete observations. Existing work treats modality absence as a prediction-accuracy problem, leaving a more basic question unanswered: whether a model's confidence estimates remain calibrated when an entire input stream is removed. We argue that missing-modality robustness and calibrated uncertainty are a single coupled property, and introduce Modality-Conditioned Conformal Fusion (MCCF), an architecture that addresses both at once. MCCF combines a multimodal bottleneck fusion backbone trained with modality dropout, per-modality evidential heads producing modality-decomposed Dirichlet distributions, and a Dempster-Shafer combination rule that fuses the per-modality evidence into a joint predictive distribution; an absent modality contributes vacuous evidence that is structurally ignored, so the fused uncertainty automatically reflects the reduced information without test-time imputation. A Mondrian conformal calibration module keyed on the modality-presence mask then provides finite-sample group-conditional coverage for every non-empty modality subset. MCCF is, to our knowledge, the first method with formal coverage guarantees under arbitrary modality availability through architectural integration rather than post-hoc recalibration, and the evidential decomposition yields per-modality vacuity scores that localise uncertainty to the absent modality responsible. Across a synthetic problem and three real multimodal benchmarks, MCCF holds its target coverage on every modality-presence subset, substantially narrows the coverage gap between full and partial modalities relative to a marginal split-conformal baseline, and imposes no measurable accuracy cost relative to temperature-scaled and evidential baselines.

## Metadata
- **Published**: 2026-08-07T12:57:16Z
- **Authors**: Alireza Moayedikia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07183v1)