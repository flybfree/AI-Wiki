---
title: BIRD-History: A Benchmark for History-Driven Text-to-SQL with Fine-Grained Knowledge Annotations
url: http://arxiv.org/abs/2608.29345v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_15-59-56Z_BIRD_History_ABenchmarkforHistory_DrivenText_to_SQ.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BIRD-History, a benchmark of 1,393 tasks across 11 databases to evaluate text-to-SQL systems' ability to use historical SQL logs for grounding underspecified queries. Experiments show that plug‑in retrievers improve four state‑of‑the‑art models, confirming the value of history‑driven knowledge.

## Key Takeaways
- The benchmark provides ground‑truth annotations linking natural language questions to specific historical SQL clauses, enabling precise evaluation of knowledge retrieval and utilization.
- A plug‑in retriever extracts five types of external knowledge from historical scripts without altering existing few‑shot pipelines.
- Consistent improvements across four text‑to‑SQL systems demonstrate that leveraging historical query logs can handle implicit domain knowledge.

## Context
Current text‑to-SQL research focuses on explicit schema and question phrasing, overlooking the rich implicit knowledge embedded in real‑world operational queries. Historical SQL logs are a natural source of such knowledge but lack standardized evaluation tools.

## Implications
Practitioners can adopt BIRD-History to fine‑tune models for business‑logic aware query generation, reducing errors caused by underspecified inputs. The open‑source toolkit encourages broader adoption of history‑driven text‑to-SQL systems in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29345v1)
