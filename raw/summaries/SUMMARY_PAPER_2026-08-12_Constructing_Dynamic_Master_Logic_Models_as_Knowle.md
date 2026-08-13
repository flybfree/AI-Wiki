---
title: Constructing Dynamic Master Logic Models as Knowledge Graphs for Complex System Diagnostics Using Retrieval-Augmented Large Language Models
url: http://arxiv.org/abs/2608.12304v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-50-39Z_ConstructingDynamicMasterLogicModelsasKnowledgeGra.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a framework for automatically constructing Dynamic Master Logic (DML) models from system descriptions, representing them as Knowledge Graphs using Retrieval-Augmented Generation and Large Language Models. The approach scales to large complex systems and enables diagnostic reasoning, safety assessment, failure propagation, and dependency tracing. The framework demonstrates consistent reconstruction across repeated runs, confirming its reliability.

## Key Takeaways
- DML construction is automated via targeted retrieval preserving functional dependencies.
- KG-DML supports diagnostic reasoning, safety assessment, upward failure propagation, downward dependency tracing.
- Multi-level validation evaluates layer-specific precision/recall, logical gate consistency, and structural integrity.

## Context
In AI research, knowledge graphs are used to encode complex systems, but building them from text remains challenging. Retrieval-Augmented Generation bridges this gap by fetching relevant information and generating structured outputs. This aligns with trends toward multimodal AI that combine language understanding with graph representation for system modeling.

## Implications
This work enables engineers to convert technical documentation into executable models for reliability analysis, accelerating system diagnostics and improving safety verification in critical infrastructure like nuclear plants. Practitioners can integrate these models into existing reliability assessment pipelines, reducing manual model-building effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12304v1)
