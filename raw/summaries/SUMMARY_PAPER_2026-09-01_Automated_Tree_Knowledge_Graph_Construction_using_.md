---
title: Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks
url: http://arxiv.org/abs/2609.00763v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_05-52-50Z_AutomatedTreeKnowledgeGraphConstructionusingOntolo.md
generated_at: 2026-09-01 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an end‑to‑end pipeline that automatically constructs a hierarchical knowledge graph from Vietnamese high school history textbooks and evaluates retrieval strategies using three graph traversal approaches. The constructed tree KG contains 750 nodes and 4,341 semantic edges with controlled ontology growth. Among the evaluation methods, the Top‑Down strategy with structural awareness outperforms a vector baseline by 4.7 percentage points in NDCG@10.

## Key Takeaways
- The paper addresses the lack of automatic knowledge graph construction using ontology expansion for low‑resource languages like Vietnamese, introducing a hybrid relation extraction pipeline that reduces prompt size and prevents bloated ontologies.
- It introduces systematic evaluation of knowledge retrieval strategies that exploit hierarchical structures, testing Top‑Down, Horizontal, and Bottom‑Up traversal methods on a synthetic benchmark of 1,210 queries across 109 subgraphs.
- The results show that the Top‑Down strategy with structural information achieves higher NDCG@10 than flat cosine similarity baselines, indicating value in preserving tree structure for retrieval.

## Context
In AI research, retrieval augmented generation (RAG) relies heavily on knowledge graphs to ground language models. Constructing such graphs automatically is especially challenging for low‑resource languages where ontological resources are scarce. This work contributes a scalable method that combines ontology expansion with LLM extraction and evaluation frameworks that respect hierarchical data organization.

## Implications
The framework offers practitioners a practical way to generate structured knowledge from textual corpora without extensive manual annotation, supporting the deployment of RAG systems in multilingual contexts. By demonstrating that structural information improves retrieval beyond flat similarity measures, it encourages developers to preserve document hierarchy when building knowledge bases for AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00763v1)
