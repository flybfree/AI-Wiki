---
title: RepBench: Compiling Benchmarks into Capability Representations for Large Language Models
url: http://arxiv.org/abs/2607.28008v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_10-56-44Z_RepBench_CompilingBenchmarksintoCapabilityRepresen.md
generated_at: 2026-07-30 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
RepBench introduces a benchmark‑grounded data layer for capability‑aligned representation probing, aggregating 13,427 papers and 353 public datasets into a unified corpus of probe texts. The pipeline shows that raw per‑text vectors lack natural cluster structure, while benchmark‑pooled capability vectors achieve optimal clustering with few clusters across models, though they show low agreement to human taxonomy. Cross‑benchmark transfer evaluation reveals method‑dependent results: difference‑in‑means outperforms logistic regression on ten models, highlighting the importance of readout and aggregation criteria.

## Key Takeaways
- Raw per‑text vectors lack natural cluster granularity.
- Benchmark‑pooled capability vectors achieve interior clustering optimum with a small number of clusters across all evaluated models, yet exhibit low agreement to the human taxonomy.
- Cross‑benchmark transfer evaluation shows disagreement between methods: difference‑in‑means attains the highest model‑level mean on ten models, while logistic regression wins the most capability‑model cells.

## Context
Representation engineering is central to understanding and improving large language models, but current evaluations rely on paper‑specific synthetic data that hinder comparison. RepBench addresses this by creating a reproducible, multi‑benchmark framework for probing capabilities in a unified manner.

## Implications
For researchers, RepBench provides a reusable workflow that standardizes capability measurement across diverse benchmarks. Practitioners can leverage its pipeline to obtain more reliable model assessments and guide development decisions based on consistent, benchmark‑aligned representations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28008v1)
