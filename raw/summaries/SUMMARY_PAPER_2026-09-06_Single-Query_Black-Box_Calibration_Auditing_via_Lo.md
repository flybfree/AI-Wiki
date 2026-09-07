---
title: Single-Query Black-Box Calibration Auditing via Logit Bias
url: http://arxiv.org/abs/2609.05125v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_13-24-52Z_Single_QueryBlack_BoxCalibrationAuditingviaLogitBi.md
generated_at: 2026-09-06 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper demonstrates that any LLM API exposing a logit_bias parameter can be used to compute exact probability thresholds for binary classification tasks with just one query per sample. It introduces a provably consistent estimator of the True Calibration Error, enabling auditing of black‑box foundation models without access to raw probabilities.

## Key Takeaways
- The method converts the logit_bias parameter into an exact probability estimate per query, allowing precise calibration metric calculation.
- Only one API call is required per sample, dramatically reducing computational overhead compared with generating multiple queries.
- The estimator is mathematically consistent and provably unbiased for binary tasks, offering a reliable audit tool.

## Context
Calibration of LLMs as zero‑shot classifiers remains a concern because providers often mask continuous outputs. This work reveals that the hidden logit_bias interface can be exploited to reveal these probabilities, addressing the opacity issue in AI evaluation.

## Implications
For practitioners, this provides a low‑cost way to verify model reliability before deployment. For industry, it supports responsible AI practices and regulatory compliance by exposing calibration gaps.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.05125v1)
