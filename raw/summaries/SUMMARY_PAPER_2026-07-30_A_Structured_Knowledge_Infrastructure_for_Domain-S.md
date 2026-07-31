---
title: A Structured Knowledge Infrastructure for Domain-Specific Data Asset Discovery
url: http://arxiv.org/abs/2607.27748v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_06-40-05Z_AStructuredKnowledgeInfrastructureforDomain_Specif.md
generated_at: 2026-07-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a structured knowledge infrastructure that solves two failures in enterprise data analytics: generic RAG retrieving wrong assets and lacking usage knowledge. This solution is deployed in the commercial advertising data warehouse at Xiaohongshu, which contains over 5,300 Hive tables across 14 domains.

## Key Takeaways
- The Graph-Guided Retriever reduces token usage by 71.6x while improving retrieval speed.
- Negative knowledge contributes 25 percentage points of Hit@10 gain through explicit scenario annotations.
- End-to-end latency is 4.84--5.33 seconds on benchmark queries.

## Context
Enterprise data analytics systems often rely on generic RAG pipelines that ignore domain-specific context, leading to poor performance and misinterpretation of metrics. This work demonstrates how integrating structured knowledge graphs with scene-aware ranking can address these gaps in large-scale advertising data warehouses. The integration aligns with current trends toward multimodal AI systems that combine retrieval with contextual understanding.

## Implications
Practitioners can implement similar two-layer knowledge bases to boost retrieval relevance without sacrificing speed. This approach is scalable across multiple domains, offering a template for future AI-driven data discovery systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27748v1)
