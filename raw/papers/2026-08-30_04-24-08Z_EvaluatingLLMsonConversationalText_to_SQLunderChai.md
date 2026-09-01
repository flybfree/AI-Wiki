---
title: Evaluating LLMs on Conversational Text-to-SQL under Chain Ambiguity and Intent Drift
published: 2026-08-30T04:24:08Z
authors: Yujia Liu, Jiayan Lin, Zijin Hong, Zheng Yuan, Shengyuan Chen, Hao Chen, Qinggang Zhang, Xiao Huang, Feiran Huang
url: http://arxiv.org/abs/2608.29543v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating LLMs on Conversational Text-to-SQL under Chain Ambiguity and Intent Drift

## Abstract
Recent advances in large language models (LLMs) have established conversational text-to-SQL as a practical interface between users and databases, often involving multiple turns of clarification and revision. However, existing benchmarks primarily evaluate execution accuracy, leaving the unfolding and shifting of user intent across turns largely uncovered. To address this, we introduce TIDE-Bench, a benchmark for conversational text-to-SQL under chain ambiguity and intent drift evaluation, targeting two recurring patterns: chain ambiguity, where an underspecified question triggers layered clarification with conditional dependencies, and intent drift, where the user retracts and replaces a previously committed request element. Built on 514 anchor SQLs from BIRD, TIDE-Bench comprises 1,542 samples and introduces dedicated metrics for chain identification and drift recognition-resolution beyond execution accuracy. Evaluating 12 advanced LLMs reveals a persistent chain identification bottleneck unaffected by clarification frequency, a wide drift recognition-resolution gap, and overlap between failure modes when jointly activated. The corresponding code of TIDE-Bench is released for further research.

## Metadata
- **Published**: 2026-08-30T04:24:08Z
- **Authors**: Yujia Liu, Jiayan Lin, Zijin Hong, Zheng Yuan, Shengyuan Chen, Hao Chen, Qinggang Zhang, Xiao Huang, Feiran Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29543v1)