---
title: FedV-KGQA: Multi-Hop Question Answering over Vertically Partitioned Knowledge Graphs
url: http://arxiv.org/abs/2608.24846v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_17-34-27Z_FedV_KGQA_Multi_HopQuestionAnsweringoverVertically.md
generated_at: 2026-08-25 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FedV-KGQA, a framework for multi-hop question answering over vertically partitioned knowledge graphs where organizations share entities but own disjoint relation sets. It combines local graph enrichment and embeddings to keep data within silos while enabling reasoning across them. Experiments on three benchmarks show strong performance comparable to centralized models.

## Key Takeaways
- FedV-KGQA enables multi-hop reasoning without any runtime inter-silo communication by anchoring questions in the correct graph neighborhood using a topic entity mechanism.
- The framework preserves raw triples and relation parameters within each silo, establishing a structural data boundary that prevents centralization.
- Evaluation across 12 model configurations demonstrates strong results, close alignment with centralized performance, support for three-hop reasoning, and robustness to embedding perturbations.

## Context
Knowledge graph question answering is challenged by real-world constraints where data resides in separate organizational silos. Centralized systems are impractical due to governance and privacy concerns. This work addresses the need for decentralized yet effective reasoning across such partitions.

## Implications
For industry practitioners, FedV-KGQA offers a scalable solution that respects data sovereignty while maintaining high accuracy. It can be adopted by organizations needing collaborative KG QA without compromising security or centralization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24846v1)
