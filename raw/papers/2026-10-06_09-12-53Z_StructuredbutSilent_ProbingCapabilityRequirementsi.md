---
title: Structured but Silent: Probing Capability Requirements in LLM Hidden States
published: 2026-10-06T09:12:53Z
authors: Kyojun Choo, Minsoo Song, Yunju Kang, Chanjun Park
url: http://arxiv.org/abs/2610.08018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structured but Silent: Probing Capability Requirements in LLM Hidden States

## Abstract
Reliable tool use requires more than triggering a mechanism or matching a query to an API description. Before selecting a specific tool, an agent must first infer the capability requirements implied by the user query. In this paper, we investigate whether these query-side capability requirements are linearly decodable from LLM hidden representations prior to generation, and how this hidden-state accessibility compares with explicit verbal classification. We introduce TACIT, a framework that decomposes external requirements along three fundamental axes: Source, Transformation, and World Effect, defining eight structurally distinct capability classes. Using 1,600 balanced training queries from benchmarks, synthetic examples, and new domain scenarios, we train linear probes on pre-generation hidden states from four open-weight LLM families. Our empirical results demonstrate that fine-grained capability structures are linearly decodable with high accuracy across all models. Crucially, however, we expose a representation-to-verbalization gap: these same models are significantly less reliable when asked to explicitly classify the same queries in natural language. This disconnect indicates that information about required external capabilities is linearly accessible in LLM hidden representations but not reliably expressed, a phenomenon we define as "structured but silent."

## Metadata
- **Published**: 2026-10-06T09:12:53Z
- **Authors**: Kyojun Choo, Minsoo Song, Yunju Kang, Chanjun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08018v1)