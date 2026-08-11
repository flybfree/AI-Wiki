---
title: MDB-Link: Hierarchical Schema Linking for Multi-Database Text-to-SQL
url: http://arxiv.org/abs/2608.09588v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_13-21-59Z_MDB_Link_HierarchicalSchemaLinkingforMulti_Databas.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MDB‑Link, a hierarchical schema‑linking framework designed for multi‑database text‑to‑SQL tasks. By leveraging a global index and a budget‑aware large language model, the system improves database localization and column selection while keeping the resulting schema compact. Exact match scores rise from 16.88 to 51.41 on MMQA, 2.50 to 9.17 on Spider2‑Snow, and 12.52 to 38.01 on BIRD‑dev.

## Key Takeaways
- MDB‑Link retrieves question‑relevant columns from a global index and aggregates evidence to shortlist databases before reranking with an LLM, enabling precise database selection.
- The budget‑aware LLM reduces schema size to match gold schemas, resulting in exact matches that improve by over 30 percentage points across benchmark datasets.
- The hierarchical approach yields faster performance than existing methods such as LinkAlign and AutoLink.

## Context
The field of text‑to‑SQL assumes a single target database, ignoring the complexity of heterogeneous collections. MDB‑Link addresses this gap by integrating multi‑database awareness into schema generation pipelines.

## Implications
For practitioners, MDB‑Link offers a scalable solution that can be deployed across large data warehouses without manual reconfiguration. The method’s efficiency and accuracy could lower development costs for AI‑driven query assistants in enterprise environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09588v1)
