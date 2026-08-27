---
title: Query-Side Attacks on GNN-Based KGQA: Tracing Failures from Entity Linking to Answer Generation
url: http://arxiv.org/abs/2608.25922v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_15-34-29Z_Query_SideAttacksonGNN_BasedKGQA_TracingFailuresfr.md
generated_at: 2026-08-26 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how adversarial perturbations on input questions affect a GNN‑based knowledge graph question answering pipeline, which consists of entity linking, subgraph retrieval, GNN reasoning, and answer generation. By isolating failures at each stage using two attack types—Compositional Restructuring (CR) and Relation Synonym Swap (RS)—the authors show that the collapse is primarily caused by errors in subgraph construction rather than downstream reasoning.

## Key Takeaways
- The GNN reasoning stage maintains near‑baseline accuracy when the correct subgraph is retrieved, indicating that model performance is not the main source of failure.  
- Subgraph construction accounts for over 99 % of the end‑to‑end collapse under CR attacks, even though the gold answer appears in only 74 % of retrieved subgraphs, highlighting a disconnect between answer presence and reachability.  
- Standard robustness metrics that treat all pipeline stages as a single metric mask these stage‑specific failures, obscuring where mitigation efforts should be directed.

## Context
In AI research on knowledge graphs, end‑to‑end evaluation often hides the source of brittleness, leading to misguided improvements. This work clarifies that subgraph construction is a critical bottleneck, aligning with broader trends toward modular robustness analysis and stage‑level debugging in multimodal pipelines.

## Implications
For practitioners building KGQA systems, focusing on robust subgraph extraction will yield more reliable answers than merely fine‑tuning the reasoning model. The findings also suggest that evaluation frameworks should support isolated failure detection to guide targeted defenses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25922v1)
