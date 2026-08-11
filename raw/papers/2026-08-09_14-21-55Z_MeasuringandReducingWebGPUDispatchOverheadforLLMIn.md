---
title: Measuring and Reducing WebGPU Dispatch Overhead for LLM Inference
published: 2026-08-09T14:21:55Z
authors: Jędrzej Maczan
url: http://arxiv.org/abs/2608.08730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring and Reducing WebGPU Dispatch Overhead for LLM Inference

## Abstract
Large Language Models are deployed to multiple types of environments, from internet browsers to edge devices, and WebGPU serves as a modern cross-platform standard. The engines for browser-based LLM inference have proliferated, yet the overhead of WebGPU per-operation dispatch remains poorly characterized. In this work, we introduce a sequential-dispatch measurement method and show that naive single-operation measurements overestimate per-dispatch cost by conflating dispatch with synchronization. Using our method, we measure the per-dispatch cost and show that it is independent of data type used. We show that the dispatch overhead, not kernel quality, is the bottleneck at batch size 1, and isolate the dispatch count as the cause. Therefore, we conclude that at batch size 1, the effective approach to LLM inference optimization in WebGPU is reducing dispatch count. Our findings point to dispatch amortization, in the inference engines and in the WebGPU specification, as a path to practical browser-based inference.

## Metadata
- **Published**: 2026-08-09T14:21:55Z
- **Authors**: Jędrzej Maczan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08730v1)