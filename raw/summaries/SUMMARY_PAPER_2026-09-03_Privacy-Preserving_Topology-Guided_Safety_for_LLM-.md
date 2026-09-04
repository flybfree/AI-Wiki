---
title: Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning
url: http://arxiv.org/abs/2609.02967v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_07-57-12Z_Privacy_PreservingTopology_GuidedSafetyforLLM_Base.md
generated_at: 2026-09-03 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FGLGuard, a privacy‑preserving safety framework for large language model based multi‑agent systems that learns a topology‑aware detector using federated graph learning instead of centralizing labeled traces. Experiments show federated training outperforms centralized models across multiple benchmarks and maintains high detection accuracy while preserving data privacy.

## Key Takeaways
- FGLGuard treats safety as a graph attention problem where each operator trains an edge‑feature detector on its own judge‑labeled episode graphs and shares only model updates, avoiding any single entity seeing the full attack distribution. - The method employs proximal local objectives for non‑IID clients, domain‑balanced aggregation, over‑refusal constrained threshold calibration, and a guarded rewrite to block unsafe answers, ensuring robust performance under distribution shift. - On Agent‑SafetyBench, R‑Judge, and AgentDojo the federated approach exceeds centralized ceiling scores without pooling any data, while unsupervised anomaly guards and local‑only training fail.

## Context
Current safety research often assumes a single operator can collect all labeled interactions, which is unrealistic in multi‑domain deployments. Federated learning enables collaborative model improvement across organizations while respecting privacy constraints, aligning with trends toward decentralized AI governance.

## Implications
This work demonstrates that privacy‑preserving safety can be achieved without sacrificing detection performance, encouraging industry adoption of federated approaches for LLM‑based agent coordination. Practitioners should prioritize topology‑aware detectors and federated aggregation to maintain utility while protecting proprietary workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02967v1)
