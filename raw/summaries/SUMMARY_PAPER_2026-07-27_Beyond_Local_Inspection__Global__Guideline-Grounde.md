---
title: Beyond Local Inspection: Global, Guideline-Grounded Evaluation of Post-hoc XAI Methods for ECG Classification
url: http://arxiv.org/abs/2607.24035v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_06-16-28Z_BeyondLocalInspection_Global_Guideline_GroundedEva.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a global, guideline‑grounded framework that aggregates post‑hoc explanations across heartbeats and compares them to clinically defined regions of interest for ECG classification. It demonstrates that most gradient‑based XAI methods systematically prioritize signal amplitude over disease‑specific patterns, with nine out of thirteen classifiers performing below chance for at least one condition.

## Key Takeaways
- The aggregated explanations often correlate strongly with signal amplitude rather than disease‑specific patterns, achieving Spearman correlations up to 0.69.
- For ischemia detection, LRP‑ε assigns only 4.6 % relevance to the ST segment while LRP‑SIGN correctly captures 63.8 %, showing a severe mismatch between model output and clinical importance.
- Nine of the thirteen gradient‑based methods fall below chance for at least one condition, indicating inconsistent reliability across pattern types.

## Context
Explainable AI aims to make models interpretable, yet many methods are trained on generic image data and transfer poorly to medical signals. This study highlights that without domain‑specific evaluation, XAI can propagate harmful biases in high‑stakes applications like ECG classification.

## Implications
Practitioners must adopt global, guideline‑grounded frameworks rather than relying on local heatmaps; otherwise, explanations may mislead clinicians and degrade diagnostic trust. The paper calls for systematic cross‑pattern validation to ensure AI tools are clinically sound.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24035v1)
