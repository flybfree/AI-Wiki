---
title: Single-Query Black-Box Calibration Auditing via Logit Bias
published: 2026-09-04T13:24:52Z
authors: Roman Plaud, Antoine Saillenfest, Matthieu Labeau, Thomas Bonald, Willem Waegeman
url: http://arxiv.org/abs/2609.05125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Single-Query Black-Box Calibration Auditing via Logit Bias

## Abstract
Evaluating the calibration of Large Language Models (LLMs) is critical for their safe deployment as zero-shot classifiers. Yet, commercial API providers increasingly hide the continuous output probabilities required by standard calibration metrics. To bypass this opacity, we demonstrate that any LLM API exposing a logit\_bias parameter can be mathematically manipulated to evaluate exact probability thresholds using strictly one query per sample. Leveraging this mechanism, we introduce a novel and provably consistent estimator of the True Calibration Error for binary tasks. Our approach therefore provides an efficient framework for auditing black-box foundation models.

## Metadata
- **Published**: 2026-09-04T13:24:52Z
- **Authors**: Roman Plaud, Antoine Saillenfest, Matthieu Labeau, Thomas Bonald, Willem Waegeman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05125v1)