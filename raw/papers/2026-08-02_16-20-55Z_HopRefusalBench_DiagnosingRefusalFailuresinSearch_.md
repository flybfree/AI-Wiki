---
title: HopRefusalBench: Diagnosing Refusal Failures in Search-Augmented Agents for Multi-Hop Reasoning
published: 2026-08-02T16:20:55Z
authors: Jianan Xie, Xin Sun, Zhongqi Chen, Xing Zheng, Qiang Liu, Bowen Song
url: http://arxiv.org/abs/2608.01358v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HopRefusalBench: Diagnosing Refusal Failures in Search-Augmented Agents for Multi-Hop Reasoning

## Abstract
Search-augmented large language model agents are increasingly capable of solving knowledge-intensive tasks, but their behavior when a multi-hop question is fundamentally unanswerable remains poorly understood. Existing abstention benchmarks largely expose defects at the surface of single-hop queries and therefore cannot reveal failures that emerge only after valid intermediate reasoning and retrieval. We introduce HopRefusalBench, the first controlled benchmark of refusal within multi-hop search, comprising 889 unanswerable questions constructed from KILT-grounded entity paths. It crosses three causes of unanswerability (answer unknown, false premise, and underspecified context) with root, middle, and terminal topologies, making premise verification, intermediate-bridge validation, and terminal stopping separately observable. We further propose a final-outcome taxonomy spanning target-aware refusal, pseudo-refusal, hallucinated completion, and search-budget exhaustion, together with source-aware trajectory metrics for post-trigger continuation and token waste. Across ten frontier proprietary and open-weight models in search-augmented mode, the best model achieves a target-aware correct halting rate (TCHR) of only 42.9%. Root and middle items are consistently harder than terminal items, and all models attain their highest TCHR on false premises and their lowest on underspecified questions. Yet when pooled across categories, 84.7--98.4% of each model's explicit refusal-like responses identify the correct rationale, localizing the main bottleneck to committing to an appropriate non-answer; failed trajectories instead diverge into hallucination or search-budget exhaustion. These results establish refusal in multi-hop search as a consequential evaluation problem and provide a foundation for diagnosing and improving the reliability of search-augmented agents.

## Metadata
- **Published**: 2026-08-02T16:20:55Z
- **Authors**: Jianan Xie, Xin Sun, Zhongqi Chen, Xing Zheng, Qiang Liu, Bowen Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01358v1)