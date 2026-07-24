---
title: The C-index illusion: discrimination without calibration in published survival models
url: http://arxiv.org/abs/2607.19526v2
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_19-13-54Z_TheC_indexillusion_discriminationwithoutcalibratio.md
generated_at: 2026-07-23 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the concordance index (C-index) used to compare survival models provides a fair assessment when calibration and time‑dependent accuracy are ignored, using three published non‑clinical survival models. It finds that while discrimination can be similar across models, several exhibit systematic calibration errors that lead to biased risk estimates, especially in high‑risk segments.

## Key Takeaways
- The C-index alone cannot reliably compare models because it ignores calibration; a model with C≈0.9595 still fails formal calibration tests at p<0.001.
- Calibration failures are not due to a single feature but arise from the overall risk prediction, causing upward bias of up to two percentage points in default risk and nearly four in the riskiest segment.
- Model preference may be misplaced rather than incorrect; the chosen model is often trusted despite calibration issues, highlighting a confidence problem.

## Context
In AI‑driven survival analysis, practitioners rely heavily on discrimination metrics like C-index for model selection and deployment. However, real‑world data often involve censoring mechanisms that affect both discrimination and calibration, yet existing benchmarks focus on synthetic or clinical settings, leaving the validity of published models untested.

## Implications
For industry stakeholders, this work warns against trusting only C-index scores when evaluating survival predictions, as they may hide systematic bias. Practitioners should supplement model comparison with calibration checks to ensure risk estimates remain trustworthy and actionable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19526v2)
