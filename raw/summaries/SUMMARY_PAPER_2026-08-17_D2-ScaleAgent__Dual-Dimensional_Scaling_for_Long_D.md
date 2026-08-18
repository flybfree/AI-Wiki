---
title: D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding
url: http://arxiv.org/abs/2608.16417v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_11-15-27Z_D2_ScaleAgent_Dual_DimensionalScalingforLongDocume.md
generated_at: 2026-08-17 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces D2‑ScaleAgent, a dual‑dimensional scaling framework that dynamically expands retrieval and reasoning in multi‑agent RAG for long document understanding. By continuously updating an evidence bank, the system routes outward to retrieve more pages when needed and inward to select fine‑grained sub‑agents for reasoning, achieving logical closure of the evidence chain. Experiments on benchmarks such as MMLongBench‑Doc and LongDocURL show significant improvements over fixed workflows.

## Key Takeaways
- The framework introduces a dynamic routing loop that separates retrieval scaling (outward) from reasoning scaling (inward), allowing the agent to adaptively expand or contract evidence based on query difficulty.
- It uses an intrinsically updated evidence bank as working memory, ensuring comprehensive coverage and preventing insufficient evidence accumulation.
- The system performs parallel page retrieval for attributes and adaptive pruning, which improves efficiency while maintaining logical closure of the reasoning chain.

## Context
Current RAG pipelines rely on static workflows that cannot scale computation at test time, limiting their ability to handle long, visually rich documents. This paper addresses a key limitation by proposing an agentic approach that dynamically balances retrieval effort and reasoning granularity.

## Implications
For practitioners developing document understanding systems, D2‑ScaleAgent offers a scalable architecture that reduces unnecessary computation and improves answer quality on large corpora. The method may lead to more efficient deployment of RAG agents in industry applications where latency and evidence completeness are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16417v1)
