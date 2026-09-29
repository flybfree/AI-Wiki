---
title: Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs
published: 2026-09-28T09:29:25Z
authors: Zhengxiang Huang, Shengheng Chen, Chaoyue Niu, Yujie Sun, Zhaode Wang, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen
url: http://arxiv.org/abs/2609.34727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs

## Abstract
On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost. Although KV caching is widely used to reduce latency in long-context inference, existing designs were primarily optimized for cloud GPUs with dynamic execution environments and abundant memory bandwidth. These architectural assumptions do not hold on mobile NPUs, where computation graphs must be statically compiled and both memory capacity and I/O bandwidth are severely constrained. In this work, we present a compute-storage co-design for mobile-centric prefix and non-prefix KV reuse. We first propose an intra-graph mechanism that maps selective KV recomputation onto static NPU graphs, reconciling algorithmic dynamicity with NPU staticity. We further develop an inter-graph scheduler to optimize chunk merging and minimize padding with dynamic programming. To address mobile bandwidth limitations, we introduce a hierarchical KV manager featuring a tree-hash-semantic hybrid structure, along with cost-aware prefetching and eviction policies. We also build a two-dimensional pipeline that overlaps KV loading, rerotation, and storage with NPU execution, hiding data-movement latency. Experiments across representative on-device workloads and LLMs show that our design reduces time-to-first-token (TTFT) by $40-60\%$ compared with no reuse and prefix-only caching.

## Metadata
- **Published**: 2026-09-28T09:29:25Z
- **Authors**: Zhengxiang Huang, Shengheng Chen, Chaoyue Niu, Yujie Sun, Zhaode Wang, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34727v1)