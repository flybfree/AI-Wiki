---
title: CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding
url: http://arxiv.org/abs/2609.29474v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_12-31-05Z_CodeGraph_Open_TaxonomyKnowledgeGraphforSourceCode.md
generated_at: 2026-09-27 16:19
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces CodeGraph, a large-scale open-taxonomy knowledge graph derived from source code by leveraging a code-specialized Large Language Model for semantic annotation and grounding entities in Wikidata. By processing the Stack-Edu corpus of 167 million files, the authors created a graph with approximately 158 million nodes and 1 billion edges that connect files to algorithms, paradigms, design patterns, and application domains across 14 programming languages. A calibrated quality-assurance protocol combining human gold sets and LLM-as-a-judge filters ensures high annotation precision, addressing the limitations of current tools restricted to syntactic analysis.

## Key Takeaways
- The authors developed a three-stage linking procedure to ground extracted code entities in Wikidata, utilizing deterministic SPARQL queries for unambiguous matches, a Deep Research Agent for resolving long-tail entities, and a hierarchy-rollup stage to import parent-of closures, thereby creating a robust semantic bridge between source code concepts and established knowledge bases.
- CodeGraph represents the first large-scale open-taxonomy knowledge graph for source code, materialized from 167 million files in the Stack-Edu corpus to contain roughly 158 million nodes (including ~145

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.29474v1)
