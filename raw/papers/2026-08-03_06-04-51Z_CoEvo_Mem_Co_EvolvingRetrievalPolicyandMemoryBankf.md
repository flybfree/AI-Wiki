---
title: CoEvo-Mem: Co-Evolving Retrieval Policy and Memory Bank for LLM Agents
published: 2026-08-03T06:04:51Z
authors: Bowen Ye, Yongchao Xu, Zhijian Li, Xiang Yin, Junkai Ma, Wenzhao Li
url: http://arxiv.org/abs/2608.01739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoEvo-Mem: Co-Evolving Retrieval Policy and Memory Bank for LLM Agents

## Abstract
As memories accumulate across tasks and sessions, the performance of long-term LLM agents depends jointly on query-specific retrieval and continual memory refinement. However, existing methods typically optimize either memory access, through iterative query refinement or adaptive retrieval policies, or memory evolution such as structural update. This separation overlooks a fundamental feedback loop: retrieval determines which memories receive usage signals, while updated memory bank reshape future retrieval. We propose \textbf{CoEvo-Mem}, a closed-loop framework for co-evolving the retrieval policy and memory bank. For each query, a frozen LLM generates route-specific query rewrites and a routing prior, which a lightweight residual router corrects online. The retrieved context serves as the coupling interface between the two learning processes: task outcomes assign credit to routing decisions, while trajectory-conditioned feedback updates memory values and graph relations. These updates alter how memories are ranked and selected for subsequent queries, thereby closing the feedback loop. To mitigate coupling induced non-stationarity, CoEvo-Mem alternates between updating the router with the memory bank fixed and evolving the memory bank with the retrieval policy fixed. Across seven diverse benchmarks, \textbf{CoEvo-Mem} achieves state-of-the-art performance, demonstrating the importance of retrieval-memory coevolution.

## Metadata
- **Published**: 2026-08-03T06:04:51Z
- **Authors**: Bowen Ye, Yongchao Xu, Zhijian Li, Xiang Yin, Junkai Ma, Wenzhao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01739v1)