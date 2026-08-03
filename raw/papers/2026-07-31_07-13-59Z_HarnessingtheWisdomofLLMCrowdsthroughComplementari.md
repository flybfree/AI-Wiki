---
title: Harnessing the Wisdom of LLM Crowds through Complementarity-Driven Iterative Collaboration
published: 2026-07-31T07:13:59Z
authors: Yanbin Fang, Xuan Wei, Wei Chen
url: http://arxiv.org/abs/2607.29087v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harnessing the Wisdom of LLM Crowds through Complementarity-Driven Iterative Collaboration

## Abstract
Large language models (LLMs) are increasingly deployed in enterprise settings, yet individual models remain bounded by model-specific capability limitations. These heterogeneous boundaries pose a deployment challenge, but also create an opportunity: strategically coordinating multiple LLMs may unlock collective intelligence exceeding any single model. Existing approaches fix how models are combined in advance, overlooking the dynamic, state-dependent role of complementarity in complex problem solving. Drawing on the wisdom-of-crowds paradigm, we reconceptualize collective LLM intelligence as relay-style complementarity: a sequential process in which each successor model is selected to address the specific bottleneck identified in its predecessor's output. To operationalize this, we propose WILC (Wisdom Integration of LLM Crowds), a framework grounded in two design principles. First, iterative reflection-and-refinement establishes a state-preserving workflow through which models diagnose and refine prior outputs. Second, complementarity-driven model selection governs transitions via a dual-gate mechanism: prospective complementarity fit (PCF) identifies the worker most suited to the current bottleneck, while posterior complementarity gain (PCG) evaluates whether the selected transition improves the evolving solution. Experiments across four diverse benchmarks show that WILC outperforms existing approaches, including single-model self-refinement, ensemble methods, and query-routing methods. Under standardized pricing assumptions, WILC matches the average benchmark performance of GPT-5.2 at roughly 7 times lower estimated per-query cost, while facilitating data sovereignty through self-hosted deployment. This study extends wisdom-of-crowds theory from static aggregation to sequential AI complementarity and provides transferable design principles for multi-AI coordination.

## Metadata
- **Published**: 2026-07-31T07:13:59Z
- **Authors**: Yanbin Fang, Xuan Wei, Wei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29087v1)