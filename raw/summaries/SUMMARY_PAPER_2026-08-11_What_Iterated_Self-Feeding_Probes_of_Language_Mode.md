---
title: What Iterated Self-Feeding Probes of Language Models Measure, and a test that separates the construction from the model
url: http://arxiv.org/abs/2608.10986v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_14-40-35Z_WhatIteratedSelf_FeedingProbesofLanguageModelsMeas.md
generated_at: 2026-08-11 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a test that distinguishes between two distinct phenomena measured by iterated self‑feeding probes of language models. It shows that the probe can capture both a fixed construction property and a model‑specific quantity, making them appear indistinguishable without careful separation. The authors validate their instrument with exact reproducibility and demonstrate how varying either the construction or the model changes the observed readings.

## Key Takeaways
- The damage light cone is kinematic, scaling with token radius in a way that does not depend on the specific language model.
- The Lyapunov exponent lambda_ca(r) remains invariant across 19 models and two scale ladders spanning a factor of 70.
- A phase transition observed by the probe is actually an artifact of the construction, not a genuine change in model behavior.

## Context
Iterated self‑feeding probes are emerging tools for probing the dynamics of large language models. By feeding a model its own output through structured token loops, researchers can observe how internal states evolve over time. This work adds a rigorous test that separates measurement artifacts from true model properties, contributing to more reliable diagnostics in AI research.

## Implications
For practitioners, this test offers a clear method to avoid misinterpreting construction‑induced signals as model failures. It encourages systematic validation and could reduce the number of retracted studies caused by ambiguous results. The framework may become standard practice for evaluating any self‑referential probe used in language model analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10986v1)
