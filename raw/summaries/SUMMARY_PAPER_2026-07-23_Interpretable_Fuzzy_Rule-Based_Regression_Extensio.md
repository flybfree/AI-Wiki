---
title: Interpretable Fuzzy Rule-Based Regression Extension for Ex-Fuzzy Library
url: http://arxiv.org/abs/2607.20277v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_15-25-38Z_InterpretableFuzzyRule_BasedRegressionExtensionfor.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an interpretable regression extension for the Ex-Fuzzy library that enables Mamdani fuzzy inference with scalar consequents learned directly from data. The method uses a target-aware partition initialisation based on Fuzzy C‑Means clustering to derive linguistic variables from an augmented input-output space, producing compact rule bases. Experiments on ten KEEL regression datasets show Gaussian partitions outperform uniform trapezoidal ones, achieving a mean coefficient of determination around 0.86.

## Key Takeaways
- The target-aware partition strategy derived from Fuzzy C‑Means clustering creates linguistic variables that emphasize output-relevant regions in the feature space.
- Gaussian partitions consistently yield higher predictive performance than uniform trapezoidal partitions, reaching a mean coefficient of determination near 0.86.
- The extension produces compact rule bases containing roughly ten to fifteen human-readable rules.

## Context
Modern machine learning models often sacrifice interpretability for accuracy, limiting their use in safety-critical and regulated environments where transparent decision making is required. Fuzzy rule-based systems provide linguistic transparency but lack a direct regression counterpart that integrates learned scalar consequents. This work bridges that gap by extending the Ex-Fuzzy library with a data-driven fuzzy regression approach.

## Implications
The results demonstrate that interpretable fuzzy regression can match or exceed black-box models on standard benchmarks, offering a practical alternative for practitioners needing both performance and explainability. As regulatory frameworks demand model transparency, this method could become a valuable tool in AI deployment pipelines across finance, healthcare, and autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20277v1)
