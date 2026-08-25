---
title: Beyond the Harness: End-to-End Optimization of Context Artifacts for Enterprise Text-to-SQL
url: http://arxiv.org/abs/2608.22830v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_05-47-55Z_BeyondtheHarness_End_to_EndOptimizationofContextAr.md
generated_at: 2026-08-24 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes constructing knowledge‑base context from historical query usage to improve enterprise Text-to-SQL performance, showing that optimized context artifacts yield larger gains than optimizing the retrieval harness. On a proprietary dataset of 5176 queries, adding retrieved knowledge‑base context improves AST similarity by up to 25%, while only modest improvements are seen with harness changes alone.

## Key Takeaways
- Retrieved knowledge‑base context provides the largest marginal improvement when combined with the full oracle query graph.
- Optimizing a distillation procedure that turns historical query profiles into reusable SQL reference cards yields larger gains than optimizing the retrieval harness.
- On the BEAVER benchmark, table cards alone perform similarly to raw historical SQL, indicating limited benefit without production‑usage signals.

## Context
Enterprise Text-to-SQL systems face scalability issues because business logic involves thousands of tables that cannot be loaded into a model at once. Prior work focused on model tuning or retrieval mechanisms, but this study highlights the importance of preprocessing context artifacts derived from real usage patterns.

## Implications
Practitioners can reduce false positives and improve query relevance by building SQL reference cards from historical data rather than relying solely on raw logs. The approach offers a scalable way to augment LLM inputs without increasing model size or complexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22830v1)
