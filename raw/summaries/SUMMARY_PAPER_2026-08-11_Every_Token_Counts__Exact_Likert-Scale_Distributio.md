---
title: Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases
url: http://arxiv.org/abs/2608.10503v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_05-20-06Z_EveryTokenCounts_ExactLikert_ScaleDistributionsfor.md
generated_at: 2026-08-11 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an exact analytical framework for measuring LLM attitudes and biases using token‑level probability mass functions in fully crossed factorial experiments. It replaces unstructured benchmarks with controlled designs that isolate causal effects, revealing hidden country‑of‑origin biases across five LLMs.

## Key Takeaways
- The framework uses exact token‑level PMFs instead of Monte Carlo sampling to eliminate noise, allowing precise measurement of bias distributions.
- Crossed factorial experiments systematically isolate main effects and interaction effects between model and context variables.
- A multivariate ordinal consensus metric and distributional ANOVA are derived to process these PMFs analytically, providing a consensus view of LLM attitudes.

## Context
Current evaluation methods rely on large, unstructured benchmarks that conflate various sources of bias. This limitation hampers the ability to attribute observed disparities to specific model traits or contextual factors in autonomous AI systems.

## Implications
This approach enables practitioners and researchers to diagnose and mitigate systematic biases in autonomous agents with confidence. As LLMs become more embedded in decision‑making, such precise measurement is essential for ethical deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10503v1)
