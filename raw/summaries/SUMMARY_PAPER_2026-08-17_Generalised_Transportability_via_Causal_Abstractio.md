---
title: Generalised Transportability via Causal Abstractions
url: http://arxiv.org/abs/2608.15645v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_09-19-16Z_GeneralisedTransportabilityviaCausalAbstractions.md
generated_at: 2026-08-17 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a model‑level framework that treats transportability as a special case of causal abstraction, allowing multiple target queries to be evaluated simultaneously with a single alignment map. By formulating the problem as distributionally robust optimisation over mechanism and environment perturbations, it provides certified intervals for both non‑transportable queries and settings lacking target data. The approach yields quantitative measures of approximate transportability and demonstrates that the resulting intervals correctly bracket true interventional estimates on benchmark datasets.

## Key Takeaways
- Transportability is recast as a single map aligning source and target variables across their interventions, enabling simultaneous query evaluation.
- Approximate maps generate certified query intervals when no exact alignment exists, turning abstraction error into a measurable transportability metric.
- The framework yields bounds for non‑transportable queries and guarantees under target‑agnostic settings, covering both Markovian and semi‑Markovian scenarios.

## Context
In causal inference, transportability remains a single‑query problem with limited practical utility when data are unavailable. This work bridges that gap by leveraging abstraction theory to produce comprehensive, certified estimates across all queries, offering a unified view of model‑level alignment in AI research.

## Implications
For practitioners, the certified intervals provide reliable bounds for decision making without needing exhaustive target data, accelerating causal analysis pipelines. The methodology also enriches theoretical understanding of transportability as an abstraction problem, guiding future work on robust causal inference models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15645v1)
