---
title: Automatic Statistical Test for Rationally Expressible Algorithms by Selective Inference, with Applications to Feature Selection
url: http://arxiv.org/abs/2608.04667v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-25-56Z_AutomaticStatisticalTestforRationallyExpressibleAl.md
generated_at: 2026-08-05 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AutoSI a framework that automatically generates the selection event for rational functions of data enabling exact selective inference. It proves p-values are valid in finite samples and applies to three feature‑selection methods including lasso with cross‑validated R^2.

## Key Takeaways
- AutoSI constructs the selection event automatically from algorithm operations eliminating manual derivation.
- The framework handles any rational function of data not limited to linear or quadratic inequalities.
- Experiments confirm that p-values control type I error while maintaining high power.

## Context
Selective inference is essential for valid hypothesis testing when the same data are used for model selection and testing. Existing methods require expert‑derived selection events limiting their applicability. AutoSI addresses this limitation by automating the process.

## Implications
Practitioners can now apply exact statistical tests to a wide range of feature‑selection algorithms without specialized expertise. This improves reliability of AI pipelines that rely on automated model selection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04667v1)
