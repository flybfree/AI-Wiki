---
title: DASH: Decoupled Adaptive Surrogate - Acquisition Harness for Automated Bayesian Optimization
url: http://arxiv.org/abs/2608.00641v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_12-53-34Z_DASH_DecoupledAdaptiveSurrogate_AcquisitionHarness.md
generated_at: 2026-08-03 20:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DASH, a Decoupled Adaptive Surrogate‑Acquisition Harness designed to improve automated Bayesian optimization for large‑language‑model tasks. By separating surrogate selection from acquisition adaptation and leveraging an LLM for final choice, DASH achieves higher trajectory acceleration and endpoint enhancement across chemical optimization benchmarks.

## Key Takeaways
- DASH selects surrogates using predictive reliability, uncertainty calibration, and ranking consistency to ensure a reliable model.
- The two‑stage acquisition controller periodically reallocates quotas among functions and delegates the final selection to an LLM, avoiding mismatched components.
- An integrated harness with knowledge‑guided warm start and structured memory leverages domain expertise and accumulated feedback.

## Context
Automated Bayesian optimization seeks online adaptation of surrogate models and acquisition functions without creating bottlenecks. Existing methods either adapt one component while leaving the other static or jointly optimize both, often ignoring their distinct roles in predictive reliability versus campaign context.

## Implications
DASH can be integrated into LLM‑enhanced BO pipelines to boost performance on large‑scale tasks, offering practitioners a robust framework that balances model trustworthiness with adaptive exploration. This approach may become standard for high‑stakes optimization where both accuracy and efficiency are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00641v1)
