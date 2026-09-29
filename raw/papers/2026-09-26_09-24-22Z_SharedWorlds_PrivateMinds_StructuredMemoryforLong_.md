---
title: Shared Worlds, Private Minds: Structured Memory for Long-Form Writing as World Creation
published: 2026-09-26T09:24:22Z
authors: Qiuyu Tian, Xiaowen Gu, Hang Su, Jianghan Chao, Haojie Yin, Fan Guo, Xin Zhang, Jinjing Shen, Ewing Luo, Youyong Kong, Yingce Xia, Zequn Liu
url: http://arxiv.org/abs/2609.32401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Shared Worlds, Private Minds: Structured Memory for Long-Form Writing as World Creation

## Abstract
LLM agents that write long-form fiction need an explicit memory of the evolving storyworld to keep new events consistent with established facts. Such memory must keep heterogeneous narrative information distinct, integrate story developments across granularities, and recover dependencies that a writing request leaves implicit. We present NarraWorld, a structured memory system for long-form writing that treats memory construction as world creation. From a shared evidence-grounded graph, NarraWorld derives four connected views: world facts, per-character beliefs, open developments, and hypothetical branches (possible-world continuations). Hierarchical aggregation with atomic closure consolidates events into scenes, plotlines, and plots, keeping each higher-level node traceable to its constituent source spans. For retrieval, planned reconstruction infers a query's dependencies from the current narrative situation and a preview of memory, then assembles the relevant records within a token budget. Across three writing benchmarks, NarraWorld achieves the strongest aggregate results. Its memory also transfers to situated role-playing and largely preserves recall on a general-purpose long-term memory benchmark, paving the way for agents that sustain coherent storyworlds across diverse narrative tasks.

## Metadata
- **Published**: 2026-09-26T09:24:22Z
- **Authors**: Qiuyu Tian, Xiaowen Gu, Hang Su, Jianghan Chao, Haojie Yin, Fan Guo, Xin Zhang, Jinjing Shen, Ewing Luo, Youyong Kong, Yingce Xia, Zequn Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32401v1)