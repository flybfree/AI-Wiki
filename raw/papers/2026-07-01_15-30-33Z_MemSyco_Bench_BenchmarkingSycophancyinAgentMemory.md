---
title: MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
published: 2026-07-01T15:30:33Z
authors: Zhishang Xiang, Zerui Chen, Yunbo Tang, Zhimin Wei, Ruqin Ning, Yujie Lin, Qinggang Zhang, Jinsong Su
url: http://arxiv.org/abs/2607.01071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemSyco-Bench: Benchmarking Sycophancy in Agent Memory

## Abstract
Memory has emerged as a cornerstone of modern LLM-based agents, supporting their evolution from single-turn assistants to long-term collaborators. However, memory is not always beneficial: retrieved memories often induce a critical issue of sycophancy, causing agents to over-align with the user at the cost of factual accuracy or objective reasoning. Despite this emerging risk, existing memory benchmarks primarily evaluate whether memories are correctly stored, retrieved, or updated, while overlooking how retrieved memories influence downstream reasoning and decision-making. To bridge this gap, we propose MemSyco-Bench, a comprehensive benchmark for evaluating memory-induced sycophancy in agent systems. MemSyco-Bench measures when memory should influence a decision and how valid memory should be used. Specifically, it covers five tasks that assess whether agents can reject memory as factual evidence, respect its applicable scope, resolve conflicts between memory and objective evidence, track memory updates, and use valid memory for personalization. All related resources are collected for the community at https://github.com/XMUDeepLIT/MemSyco-Bench.

## Metadata
- **Published**: 2026-07-01T15:30:33Z
- **Authors**: Zhishang Xiang, Zerui Chen, Yunbo Tang, Zhimin Wei, Ruqin Ning, Yujie Lin, Qinggang Zhang, Jinsong Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01071v1)