---
title: Pretraining on Call Graphs: When Binary Analysis Tasks Profit From Context
url: http://arxiv.org/abs/2608.02084v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-44-09Z_PretrainingonCallGraphs_WhenBinaryAnalysisTasksPro.md
generated_at: 2026-08-03 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how adding call‑graph information to binary function embeddings affects performance on binary analysis tasks. Experiments with graph‑based models show that while call‑graph context improves code similarity detection, it does not translate into better results for semantic or syntactic downstream tasks. The study also finds that the benefit is strongest for functions tied to namespaces rather than isolated logic.

## Key Takeaways
- Call‑graph enhancements boost binary code similarity detection but do not generalize to other analysis tasks.
- Optimizing embeddings for semantic similarity can degrade performance on syntactic tasks, indicating a trade‑off in model design.
- The added context is most effective for namespace‑related functions than for individual logic functions.

## Context
Binary function embeddings aim to capture the meaning of code snippets for reverse engineering. Incorporating inter‑procedural relationships via call graphs is a promising way to enrich these representations, but its impact remains understudied across diverse tasks.

## Implications
Practitioners should consider task specificity when augmenting embeddings with graph data rather than assuming universal gains. This research guides model selection and highlights the need for careful evaluation across related binary analysis problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02084v1)
