---
title: A Cost-Aware Agentic Architecture for NL-to-SQL over Nested Enterprise Schemas, with a New Benchmark
url: http://arxiv.org/abs/2609.04641v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_02-20-53Z_ACost_AwareAgenticArchitectureforNL_to_SQLoverNest.md
generated_at: 2026-09-06 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a cost‑aware agentic architecture designed to answer natural language queries over deeply nested enterprise schemas and presents the DevRev NL2SQL benchmark, which includes 900 execution‑verified queries with graph‑like structures. The system achieves 91.7% answer correctness on this benchmark, outperforming previous baselines by a large margin.

## Key Takeaways
- The DevRev benchmark adds nested‑type and link‑graph complexity to NL2SQL evaluation, providing a more realistic measure of analytical reasoning depth through the Semantic Depth Score.
- A cost‑aware single‑generation agentic architecture integrates schema selection, metadata retrieval, and error repair to handle these complex schemas efficiently.
- On Spider 2.0 Snowflake data, the system matches leading performance at a single‑generation operating point.

## Context
Current NL2SQL research focuses on clean relational datasets, ignoring the messy, graph‑like nature of real enterprise databases. This work bridges that gap by creating a benchmark and architecture tailored to such environments.

## Implications
For practitioners, this approach offers a practical framework for deploying accurate SQL generation in production systems where schema depth is high. It also sets a new standard for evaluating NL2SQL models beyond simple accuracy metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04641v1)
