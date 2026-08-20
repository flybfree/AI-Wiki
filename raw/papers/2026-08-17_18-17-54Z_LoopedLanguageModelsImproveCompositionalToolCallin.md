---
title: Looped Language Models Improve Compositional Tool Calling
published: 2026-08-17T18:17:54Z
authors: Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò
url: http://arxiv.org/abs/2608.18171v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looped Language Models Improve Compositional Tool Calling

## Abstract
Looped language models have shown promising results on reasoning benchmarks, yet their potential for agentic tool use remains largely unexplored. We study this question in compositional tool-calling settings, where models must coordinate multiple API calls, maintain intermediate state, and preserve dependencies across tool interactions. We evaluate native and retrofitted looped language models on API-Bank, BFCL, and NESTful, comparing looped and non-looped models trained under matched supervised fine-tuning recipes and varying recurrent depth at inference time. In controlled experiments, recurrent computation generally benefits compositional and dependency-aware tool use, while providing smaller and more model-dependent gains on isolated API invocation. Accuracy on multi-step tool use generally increases with recurrent depth; adaptive inference, however, achieves a more favorable compute-performance trade-off by allocating additional computation only when needed. Our results suggest that looped language models are a promising architecture for agentic systems that require reliable planning, coordination, and execution of compositional tool use workflows.

## Metadata
- **Published**: 2026-08-17T18:17:54Z
- **Authors**: Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18171v1)