---
title: Curate Before You Connect: Identity and Ontology Tagging in a Production Knowledge Graph
url: http://arxiv.org/abs/2608.10644v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-30-37Z_CurateBeforeYouConnect_IdentityandOntologyTaggingi.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a production‑grade ingestion and ontology‑tagging layer that converts validated extraction streams into a knowledge graph of over five hundred thousand entities and millions of relationships. It explains how the record‑identity ladder determines sameness using identifier, name, display‑name, and type‑scoped position columns rather than similarity measures, and why this approach can cause irreversible merges that erase errors.

## Key Takeaways
- The identity decision is made at ingestion time via a ladder that relies on exact matches of identifiers or canonical names, which prevents later correction of wrong types.  
- Over‑merges are undetectable because the system only flags candidates and never reports benchmarked over‑merges.  
- Multi‑class ontology tagging creates an evidence asymmetry: treating name fragments as type assertions inflates classifications, dropping valid assignments from 36 to 4 when anchored evidence is required.

## Context
This work addresses a critical gap in automated knowledge graph construction where identity resolution is treated as a one‑way merge operation. In AI pipelines that rely on extraction and graph formation, the lack of reversible identity decisions leads to data loss and corruption that cannot be recovered after writing records into the graph.

## Implications
For practitioners building large‑scale knowledge graphs, this paper highlights the need for reversible, evidence‑driven identity resolution rather than irreversible merges. The findings suggest that current automation lines should focus on flagging candidates while preserving original records to avoid hidden data loss and classification errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10644v1)
