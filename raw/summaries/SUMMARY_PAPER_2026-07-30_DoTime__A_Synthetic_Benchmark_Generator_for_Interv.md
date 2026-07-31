---
title: DoTime: A Synthetic Benchmark Generator for Interventional and Counterfactual Time Series
url: http://arxiv.org/abs/2607.27263v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_07-46-44Z_DoTime_ASyntheticBenchmarkGeneratorforIntervention.md
generated_at: 2026-07-30 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DoTime, an open generator for multivariate temporal structural causal models with interventions and counterfactuals, providing four evaluation suites and showing that interventional training improves direction accuracy over observational models. It claims a measurable advantage across structures and seeds.

## Key Takeaways
- DoTime generates continuous-time intervention windows and counterfactual sampling with positivity guard.
- It supports regime-switching SCMs and non-stationary dynamics as a strict generalization of interrupted time series.
- The released suites include exact ground truth paired interventional trajectories and shared-noise counterfactuals, enabling falsifiable claim that interventional prior-fitted network beats observational model.

## Context
This work addresses the gap in causal inference benchmarks for interventions and counterfactuals which are often small or domain-specific. By providing a scalable synthetic benchmark, DoTime enables rigorous testing of causal foundation models across diverse temporal structures.

## Implications
Practitioners can use DoTime to validate their causal models before deployment, ensuring they handle complex time series with interventions correctly. The generator’s theoretical grounding and exact ground truth make it a reliable prior for AI research in healthcare, policy, and climate science.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27263v1)
