---
title: CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery
published: 2026-08-24T01:56:01Z
authors: Donghui Zha, Lingwei Xu, Linxiao Wu, Yixue Dong, Haochen Li
url: http://arxiv.org/abs/2608.22708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery

## Abstract
Tool use in LLM systems faces a structural trade-off. Progressive disclosure keeps the prompt small by showing only the tools relevant to the current task, while prompt caching rewards a request prefix that stays fixed across calls; every change to the visible tool list invalidates the cached prefix. This paper treats the trade-off as a problem of request architecture and proposes a dual-path routing design that assigns tool selection and tool delivery to separate channels. The main model always sees a small, fixed set of core tools, so the head of its request is unchanged across calls; all other tools are reached through an independent routing channel, in which a router sub-model searches the full tool list, selects one tool, executes it, and returns the result. Tool registration is automated from source code and supports runtime updates, so the tool set can grow without modifying the main model's request prefix. The design generalizes progressive disclosure: capabilities are disclosed through the routing channel, and the main model's prefix stays stable. A prototype implementation was exercised on 55 functional queries and a 30-turn dialogue; token-level cache hit rates reached 90.99% and 95.2%, cutting input cost to about 12.0% and 8.0% of a no-cache baseline under DeepSeek's pricing, where cache-hit input tokens cost roughly 1/30 of cache-miss tokens.

## Metadata
- **Published**: 2026-08-24T01:56:01Z
- **Authors**: Donghui Zha, Lingwei Xu, Linxiao Wu, Yixue Dong, Haochen Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22708v1)