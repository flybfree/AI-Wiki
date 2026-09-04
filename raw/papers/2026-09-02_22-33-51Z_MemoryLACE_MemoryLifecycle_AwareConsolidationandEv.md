---
title: MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval
published: 2026-09-02T22:33:51Z
authors: Meriem Yacoubi, Pia Schmidt, Nenad Petrovic, Ahmed Frikha, Martin Kirchhoff, Alois Knoll
url: http://arxiv.org/abs/2609.03201v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval

## Abstract
Long-term LLM agents must preserve information across interactions while distinguishing repeated evidence, historical states, updates, and unresolved contradictions. Existing textual memory systems retrieve semantically relevant memories efficiently but often leave these relationships implicit, whereas richer structured approaches model them through global graphs, hierarchical abstractions, or reflection at greater complexity. We introduce MemoryLACE (MemLACE), a lightweight memory framework that explicitly models the lifecycle of textual evidence through sparse merge, supersession, and contradiction relations while preserving atomic natural-language memories and their provenance. Rather than retrieving memories independently, MemLACE reconstructs relation-aware evidence units that expose current, historical, supporting, and conflicting evidence for downstream reasoning. Across BEAM and StructMemEval, using open-weight and proprietary LLM backbones, MemLACE achieves the highest overall performance in same-backbone comparisons while reducing end-to-end runtime on BEAM by 66.6% relative to Hindsight, the strongest reported reflective-memory baseline. Ablation studies identify lifecycle expansion and temporal awareness as the principal contributors to these gains. Together, the results demonstrate that explicitly modeling the local lifecycle of textual evidence is sufficient to substantially improve long-term memory reasoning without requiring comprehensive knowledge graphs or global reflection.

## Metadata
- **Published**: 2026-09-02T22:33:51Z
- **Authors**: Meriem Yacoubi, Pia Schmidt, Nenad Petrovic, Ahmed Frikha, Martin Kirchhoff, Alois Knoll
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03201v1)