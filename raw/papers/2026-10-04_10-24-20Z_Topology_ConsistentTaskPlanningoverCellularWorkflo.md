---
title: Topology-Consistent Task Planning over Cellular Workflow Complexes for LLM-based Agents
published: 2026-10-04T10:24:20Z
authors: Sen Zhao, Jia Tang, Ruiqi Kong, Zuyu Zhang, Lifeng Shen, Ding Zou, Xinyu He, Xu Zhang, Junwei Han
url: http://arxiv.org/abs/2610.07004v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topology-Consistent Task Planning over Cellular Workflow Complexes for LLM-based Agents

## Abstract
Task planning for LLM agents requires workflows that satisfy both user intent and complex sub-task dependencies. While existing planners work well for sequential or directed acyclic graph (DAG)-like structures, they struggle with workflow patterns such as verification-correction loops, convergent branch merging, and reusable intermediate states that arise naturally in real-world tool orchestration. We present TopoPlanner, a topology-consistent planning framework that lifts tool dependency graphs into cellular workflow complexes and uses them as topologyaware context for LLM tool planning. TopoPlanner retrieves a request-relevant closed subcomplex through cosheaf-consistent cellular retrieval, performs multidimensional structural reasoning over the retrieved topology, and interfaces the resulting cellular representation with the planner LLM for tool-sequence generation. Experiments on four tool-planning benchmarks with topology-guided loop, merge, and loop-merge workflows show consistent improvements over prompt-based and graph-enhanced baselines across different local LLM backbones.

## Metadata
- **Published**: 2026-10-04T10:24:20Z
- **Authors**: Sen Zhao, Jia Tang, Ruiqi Kong, Zuyu Zhang, Lifeng Shen, Ding Zou, Xinyu He, Xu Zhang, Junwei Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07004v1)