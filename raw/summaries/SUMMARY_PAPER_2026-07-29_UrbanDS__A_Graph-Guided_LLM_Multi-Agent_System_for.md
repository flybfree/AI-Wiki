---
title: UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks
url: http://arxiv.org/abs/2607.26724v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_10-14-02Z_UrbanDS_AGraph_GuidedLLMMulti_AgentSystemforData_I.md
generated_at: 2026-07-29 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UrbanDS, a graph-guided LLM multi-agent system designed to handle data-intensive urban tasks by organizing reusable dataset skills and relationships into a unified dataset graph. The Data Profiling Agent creates a skill for each dataset, enabling the system to understand what data can be processed. The System also integrates execution agents that share intermediate results via memory, enabling collaborative processing. It demonstrates that UrbanDS outperforms existing agents on both general and urban benchmarks and is deployed in real-world urban operations.

## Key Takeaways
- The Data Profiling Agent creates a skill for each dataset, enabling the system to understand what data can be processed.
- The Relation Agent builds a graph linking datasets, allowing planners to retrieve relevant ones based on task needs.
- UrbanDS-Bench provides a comprehensive benchmark showing consistent performance gains over prior methods.

## Context
Current LLM agents often rely on static datasets and struggle with large-scale, multi-source urban data where spatial, temporal, and semantic connections matter. This work addresses that gap by introducing a dynamic graph structure that captures these relationships, enabling more flexible and efficient data science workflows.

## Implications
For practitioners, UrbanDS offers a scalable framework to automate complex urban analytics without manual dataset curation. For industry, it can integrate diverse city data sources into unified models, improving decision-making in smart city applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26724v1)
