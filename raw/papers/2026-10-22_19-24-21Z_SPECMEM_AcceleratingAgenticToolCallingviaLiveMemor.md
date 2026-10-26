---
title: SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management
published: 2026-10-22T19:24:21Z
authors: Zihe Song, Wenting Zhao, Ye Liu, Yuanjie Zhu, Ke Xu, Shanghao Li, Philip S. Yu
url: http://arxiv.org/abs/2610.31840v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management

## Abstract
Tool-calling agents are mostly optimized for accuracy; in deployment, however, their growing cost is latency: every tool call is decoded autoregressively. Speculative decoding accelerates this without changing the output, and retrieved past calls make strong drafts under real use, where each user's behavior tends to repeat. Yet existing systems keep no cross-session memory, or build the draft store once and never update it. We propose SpecMem, a tool-call memory kept alive and managed throughout deployment: verified calls are written back online into bounded per-user stores with LRU eviction, and a side-effect gate defers irreversible calls until verification confirms. On multi-session, multi-user query streams served by three open-weight models, a frozen store steadily loses acceptance while SpecMem holds it: a 27% gap in mean accepted tokens (+11% to +34% across benchmarks, tracking how much novel work arrives after the store is built) and up to 1.74x wall-clock speedup. Ablations attribute the gain almost entirely to keeping the store live; local per-user scoping adds no acceptance but closes a measured cross-user leakage channel, and gating on declared side effects, rather than on retrieval confidence, is what eliminates irreversible mistakes.

## Metadata
- **Published**: 2026-10-22T19:24:21Z
- **Authors**: Zihe Song, Wenting Zhao, Ye Liu, Yuanjie Zhu, Ke Xu, Shanghao Li, Philip S. Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31840v1)