---
title: D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding
published: 2026-08-17T11:15:27Z
authors: Hao Zhang, Longrong Yang, Lunhao Duan, Ziyang Wang, Qing-Guo Chen, Shanshan Zhao
url: http://arxiv.org/abs/2608.16417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding

## Abstract
Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages. However, these methods typically rely on fixed workflows and lack the ability to dynamically scale computation at test time, often leading to insufficient evidence. To address this, we propose D2-ScaleAgent, an agentic framework that introduces a dual-dimensional scaling paradigm for retrieval and reasoning. The core of D2-ScaleAgent is a Verifier agent-driven dynamic routing loop based on the intrinsic difficulty of the query, centered around a continuously updated evidence bank that serves as the agent's dynamic working memory: when retrieval needs to be expanded, the agent routes outward (retrieval scaling), decomposing the query into attributes and performing parallel page retrieval, followed by adaptive pruning to ensure comprehensive evidence coverage. When fine-grained reasoning is required, the agent routes inward (reasoning scaling), dynamically selecting sub-agents with varying granularity and count to extract evidence from pages. Finally, D2-ScaleAgent achieves logical closure over the evidence chain. Extensive experiments demonstrate that D2-ScaleAgent is effective on long and visually rich document benchmarks like MMLongBench-Doc, LongDocURL, etc.

## Metadata
- **Published**: 2026-08-17T11:15:27Z
- **Authors**: Hao Zhang, Longrong Yang, Lunhao Duan, Ziyang Wang, Qing-Guo Chen, Shanshan Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16417v1)