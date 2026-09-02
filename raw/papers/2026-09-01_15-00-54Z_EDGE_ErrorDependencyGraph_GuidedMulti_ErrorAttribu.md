---
title: EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems
published: 2026-09-01T15:00:54Z
authors: Jun Hou, Priya Pitre, Yi Fang, Xuan Wang
url: http://arxiv.org/abs/2609.01360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems

## Abstract
Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph guides a two-stage LLM-as-judge detector for error attribution, and the intervention-validated subgraph provides a more reliable basis for explanation and repair analysis. Experiments on TRAIL and MAST show that EDGE improves category-level multi-error attribution across most evaluated models and settings. Experiments with adapted Who&When-style prompts show that the graph helps across prompting strategies. These results suggest that dependency structure is a useful diagnostic prior for agent failures beyond isolated root-cause prediction.

## Metadata
- **Published**: 2026-09-01T15:00:54Z
- **Authors**: Jun Hou, Priya Pitre, Yi Fang, Xuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01360v1)