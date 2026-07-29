---
title: Automatic Knowledge Graph Construction and Query for Earthquake Catalogs
url: http://arxiv.org/abs/2607.24984v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_18-39-05Z_AutomaticKnowledgeGraphConstructionandQueryforEart.md
generated_at: 2026-07-28 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GraphRAG, a graph‑based retrieval augmented generation system that automatically builds knowledge graphs from raw earthquake catalog tables and enables accurate query answering. The authors apply it to three diverse catalogs, verify results against ground truth, and achieve reliable answers with minimal prompting.

## Key Takeaways
- The pipeline constructs complete, queryable knowledge graphs without manual structuring across multiple catalogs.
- Rigorous evaluation against catalog‑derived ground truth reveals failure modes that are corrected by four seismology‑informed prompt fixes.
- A vector RAG baseline shows the advantage of graph layers for summarization and temporal comparison.

## Context
Automated knowledge graph construction reduces reliance on manual data engineering in seismic data analysis, aligning with trends toward zero‑shot AI inference. This work demonstrates how graph‑centric retrieval can complement traditional spatiotemporal windowing methods.

## Implications
Practitioners can deploy GraphRAG to answer open‑ended seismological queries instantly, lowering costs and improving trustworthiness of results. The approach offers a transferable framework for other large tabular datasets requiring contextual reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24984v1)
