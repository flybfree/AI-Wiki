---
title: MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents
published: 2026-10-15T07:23:03Z
authors: Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
url: http://arxiv.org/abs/2610.21405v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents

## Abstract
Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this capability, we introduce MemCut, a systematic benchmark for user-requested forgetting. Its 456 hand-designed secrets in long-horizon conversations have fully annotated evidence trails to test recovery after deletion, including from messages that never state the secrets directly. We propose two recovery metrics. Native recovery measures reader success through the system's retrieval, whereas residual recovery measures the same reader's success when directly given surviving objects traced to annotated disclosures or evidence. We establish three reference deletion baselines to test how far existing retrievers and write models support forgetting across five memory designs and four LLMs. Disclosure removal reduces native recovery far more than residual recovery. LLM-guided deletion of ten additional turns from twenty retrieval candidates leaves 39-76% residual recovery. Subset sweeps (144 facts, three systems, two models) show that widening the pool at a fixed budget reduces residual recovery more than deleting all original candidates. These sweeps identify candidate coverage as a bottleneck in the reference baselines.

## Metadata
- **Published**: 2026-10-15T07:23:03Z
- **Authors**: Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21405v1)