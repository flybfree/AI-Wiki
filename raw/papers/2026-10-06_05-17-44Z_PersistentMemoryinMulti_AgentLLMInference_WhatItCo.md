---
title: Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell
published: 2026-10-06T05:17:44Z
authors: Hochan Son, Kyungdoe Han, Jaehan Koh, Xiaowu Dai, Wenlu Xu, Guang Cheng
url: http://arxiv.org/abs/2610.07782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell

## Abstract
Decomposing long-context inference across cooperating agents bounds the active KV cache per call rather than total evidence, which matters when KV-cache memory binds. Many such systems add a persistent tier storing and recalling reasoning traces, usually validated by an ablation reporting an accuracy gain. We measure both on one three-tier agent architecture. Decomposition delivers: peak KV working set of 14.3 MiB per query against 35.5 and 35.3 MiB for single-pass and retrieval-augmented baselines. The persistent tier does not: across eight controlled dataset pairs at n=100 per arm it costs +0.368 MiB [+0.167, +0.590] of peak cache and produces no detectable accuracy change (+0.015, 95% CI [-0.011, +0.046]). We argue the null is structural: single-question benchmarks supply each item with its own evidence and score it independently, and correctness requires resetting stored traces between conditions, so recall has nothing informative to retrieve. Reaching it took four measurement corrections -- three inflating the apparent benefit, the fourth making an effect that size look resolvable -- none visible in the results table. We give the conditions an agent-memory ablation must satisfy and detection procedures that need no knowledge of the specific defect.

## Metadata
- **Published**: 2026-10-06T05:17:44Z
- **Authors**: Hochan Son, Kyungdoe Han, Jaehan Koh, Xiaowu Dai, Wenlu Xu, Guang Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07782v1)