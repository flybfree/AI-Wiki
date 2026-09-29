---
title: GenMem: Generative Symbolic Memory for Self-Evolving Harness
published: 2026-09-28T08:50:44Z
authors: Xinke Jiang, Tao Feng, Weixuan Xu, Zhixin Zhang, Zhibang Yang, Wentao Zhang, Runchuan Zhu, Xu Chu, Junfeng Zhao, Yasha Wang
url: http://arxiv.org/abs/2609.34633v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GenMem: Generative Symbolic Memory for Self-Evolving Harness

## Abstract
Long-term memory supports the self-evolution of LLM agents by retaining experience and skills across tasks and enabling their retrieval, reuse, and revision in subsequent long-horizon decision-making. Yet existing memory management approaches remain limited to discriminative retrieval and to address the sparse, hierarchical, and highly redundant structure of reusable experience: only a small, task-dependent subset of trajectories and memories warrants retention, retrieval, or revision. Learning these operations is further complicated by sparse, delayed, and indirect task-level feedback, with weak supervision across the memory lifecycle. Moreover, continual memory evolution introduces an architectural tension as addressing invariance: stored experience is perpetually revised, yet the addressing interface consumed by learned retrieval policies must remain stable. To address, we present GenMem, which reformulates memory management as generative symbolic addressing. Its core mechanism is the Symbolic Identifier (SID), a multi-level discrete token tuple drawn from a Cartesian-product address space that factorizes a million-scale sparse memory space using fewer than one hundred discrete symbols. Instead of generating ever-changing raw content, the memory agent learns to generate SIDs, while memory evolution rewrites the payload at a fixed address without shifting the address itself. Architecturally, GenMem couples a MemRetriever and a MemEvolver within a multi-agent harness, trained via GRPO with dense process and outcome rewards with two-channels optimization. Under offline memory evolution, experiments spanning ALFWorld, WebShop, multi-hop QA, medical reasoning, and deep research evaluate GenMem against strong memory-augmented baselines...

## Metadata
- **Published**: 2026-09-28T08:50:44Z
- **Authors**: Xinke Jiang, Tao Feng, Weixuan Xu, Zhixin Zhang, Zhibang Yang, Wentao Zhang, Runchuan Zhu, Xu Chu, Junfeng Zhao, Yasha Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34633v1)