---
title: Beyond Tables: Doc2DB-Bench for Relationally Faithful Document-to-Database Construction
url: http://arxiv.org/abs/2608.08459v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_03-58-39Z_BeyondTables_Doc2DB_BenchforRelationallyFaithfulDo.md
generated_at: 2026-08-10 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Doc2DB‑Bench, a benchmark for constructing relational databases from long heterogeneous documents. The benchmark contains 203 document instances across multiple schemas and domains, featuring both entity tables and relationship tables to test faithful database construction. The generated documents are verified as authentic and indistinguishable from real references.

## Key Takeaways
- Doc2DB‑Bench provides a comprehensive set of 7,341 rows and 41,935 cells across 117 entity tables and 132 relationship tables, ensuring that extracted facts maintain proper normalization and integrity constraints.  
- The benchmark includes seven domain groups such as finance, healthcare, education, transportation, and enterprise operations, each with its own schema taxonomy to evaluate cross‑domain relational reasoning.  
- Authenticity verification confirms that the synthetic documents are indistinguishable from real-world references, validating the reliability of LLM‑based database generation.

## Context
The need for AI systems to produce queryable relational databases rather than flat tables is driven by downstream analytics, compliance, and decision‑making processes in regulated industries. Existing benchmarks focus on single‑table extraction, which fails to capture multi‑table relationships that are essential for real data pipelines.

## Implications
This benchmark will guide researchers toward more robust LLM models capable of preserving entity identities and cross‑table links during document conversion. Practitioners can leverage Doc2DB‑Bench to assess system performance in compliance audits and enterprise data integration workflows, ultimately improving the reliability of AI‑driven database generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08459v1)
