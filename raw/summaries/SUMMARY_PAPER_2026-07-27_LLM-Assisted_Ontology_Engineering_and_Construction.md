---
title: LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph
url: http://arxiv.org/abs/2607.24551v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_15-26-26Z_LLM_AssistedOntologyEngineeringandConstructionofaF.md
generated_at: 2026-07-27 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a two-stage LLM-assisted workflow that converts French maintenance regulations into an ontology and then builds a knowledge graph. It extracts typed entities, normalizes labels via embedding fusion, induces object properties, and uses the resulting ontology to close extraction over the full corpus. Experiments with GPT-4.1 and mistral-large-2512 achieve robust structured outputs, near-complete class alignment, and reduced duplication.

## Key Takeaways
- The workflow combines open extraction of typed entities from a stratified sample with embedding-based fusion to normalize labels, producing candidate object properties that capture domain and range signatures.
- Closed extraction guided by the ontology yields an RDF graph over the full corpus, achieving near-complete class alignment while cutting duplicated entities and predicates after fusion.
- Less than 20% of triples introduce unseen property types, indicating predicate normalization is crucial for industrial maintenance settings.

## Context
This approach leverages large language models to automate the labor‑intensive tasks of ontology engineering and knowledge graph construction in legal domains. By integrating embedding fusion and signature induction, it bridges natural language processing with structured data representation, a trend that enhances AI‑driven semantic analysis across regulatory texts.

## Implications
For practitioners, the method offers a scalable pipeline to transform complex maintenance regulations into machine‑readable ontologies, reducing manual annotation effort. Industry adoption could improve compliance monitoring, case analysis, and integration with operational systems, fostering trustworthy AI solutions in regulated environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24551v1)
