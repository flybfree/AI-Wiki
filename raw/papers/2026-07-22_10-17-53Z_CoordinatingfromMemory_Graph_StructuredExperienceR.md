---
title: Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing
published: 2026-07-22T10:17:53Z
authors: Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang
url: http://arxiv.org/abs/2607.19985v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing

## Abstract
Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations. Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation. In this paper, we propose a Graph-Structured Experiential Memory (GSEM) framework for multi-agent coordination in dynamic manufacturing. The framework encodes historical coordination episodes as heterogeneous relational graphs that capture task dependencies, machine states, and inter-agent collaboration patterns. When a new disturbance occurs, a graph neural network-based retrieval mechanism identifies structurally similar past episodes, enabling experience-guided policy adaptation rather than learning from scratch. Experiments on dynamic flexible job-shop scheduling benchmarks with three disturbance types show that GSEM reduces makespan by 4.1%-10.0% and adaptation time by 33%-38% compared to the strongest memory-augmented baseline, with the advantage increasing under higher disturbance frequency. Ablation studies and cross-disturbance transfer experiments further validate the necessity of graph-structured encoding and similarity-based retrieval and demonstrate the cross-disturbance generalizability of learned coordination patterns.

## Metadata
- **Published**: 2026-07-22T10:17:53Z
- **Authors**: Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19985v1)