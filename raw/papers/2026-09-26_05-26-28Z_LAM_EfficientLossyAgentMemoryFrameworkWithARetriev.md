---
title: LAM: Efficient Lossy Agent Memory Framework With A Retrieval-Score Error Bound
published: 2026-09-26T05:26:28Z
authors: Baixi Sun, Le Chen, Anjir Ahmed Chowdhury, Xiaolong Ma, Chih-Hsuan Yang, Mingze Xia, Syed Zawad, Sheng Di, Rajkumar Kettimuthu, Huihuo Zheng, Rajeev Thakur, Venkatram Vishwanath, Feng Yan
url: http://arxiv.org/abs/2609.32256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LAM: Efficient Lossy Agent Memory Framework With A Retrieval-Score Error Bound

## Abstract
Agent memory grows as agents read inputs, reason, and call tools. Longer histories increase inference cost and eventually exceed the context window. LLM-based summarization reduces this history but adds latency and provides no explicit bound on information loss. We propose LAM, a Lossy Agent Memory system with three components: a deterministic deduplication rule with a substitution bound on retrieval scores - a bound on score perturbation, not a certificate of unchanged ranking; a memory manager that preserves the cached prefix and overlaps compaction with inference; and a performance model that estimates compaction costs before deployment. On 600 agent trajectories, LAM removes 22.47% of observation tokens while retaining 99.984% of the measured gold-patch evidence. At a fixed deletion set, the performance model predicts a 71.4x-91.6x end-to-end speedup from removing records before prefill instead of deleting them from a prefilled context. That benefit comes from the schedule rather than the rule and applies to any prefix-preserving test.

## Metadata
- **Published**: 2026-09-26T05:26:28Z
- **Authors**: Baixi Sun, Le Chen, Anjir Ahmed Chowdhury, Xiaolong Ma, Chih-Hsuan Yang, Mingze Xia, Syed Zawad, Sheng Di, Rajkumar Kettimuthu, Huihuo Zheng, Rajeev Thakur, Venkatram Vishwanath, Feng Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32256v1)