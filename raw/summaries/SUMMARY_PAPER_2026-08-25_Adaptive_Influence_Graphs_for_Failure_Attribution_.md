---
title: Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems
url: http://arxiv.org/abs/2608.24361v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_10-18-19Z_AdaptiveInfluenceGraphsforFailureAttributioninMult.md
generated_at: 2026-08-25 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes Adaptive Influence Graphs, a two‑stage agentic framework that converts failed traces into structured graphs and navigates them to pinpoint errors in multi‑agent LLM systems. Experiments across multiple models show richer trace representations improve failure attribution, with adaptive graph construction and agent‑directed traversal delivering the best results on the Who&When benchmark.

## Key Takeaways
- The framework transforms raw logs into a graph that captures component interactions and dependencies during a failed run.
- Adaptive graph construction dynamically adjusts node weights based on observed error propagation to highlight critical components.
- Agent‑directed traversal prioritizes exploration of high‑impact edges, leading to more accurate failure attribution than static methods.

## Context
Multi‑agent large language model deployments increasingly face costly failures that are hard to diagnose without human intervention. Current observability tools help engineers navigate traces but do not automate the attribution process for LLMs. This work bridges that gap by introducing a data‑driven graph representation and traversal strategy.

## Implications
The results suggest that improving trace representation is as important as model architecture in failure analysis, prompting developers to invest in richer logging pipelines. Practitioners can leverage AIGs to reduce debugging time and improve system reliability across distributed AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24361v1)
