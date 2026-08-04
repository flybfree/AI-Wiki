---
title: CoEvo-Mem: Co-Evolving Retrieval Policy and Memory Bank for LLM Agents
url: http://arxiv.org/abs/2608.01739v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_06-04-51Z_CoEvo_Mem_Co_EvolvingRetrievalPolicyandMemoryBankf.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoEvo-Mem, a framework that jointly evolves both the retrieval policy and the memory bank of long‑term LLM agents. By closing the feedback loop between query routing decisions and memory updates, CoEvo-Mem improves performance across multiple benchmarks. The authors report state‑of‑the‑art results on seven diverse tasks.

## Key Takeaways
- Retrieval determines which memories receive usage signals, while updated memory values reshape future retrieval, forming a continuous co‑evolution loop.
- The framework alternates between fixing the router and updating the memory bank to avoid non‑stationary coupling effects.
- CoEvo-Mem achieves state‑of‑the‑art performance on seven benchmarks, highlighting the importance of integrating retrieval and memory evolution.

## Context
Long‑term LLM agents accumulate memories across sessions, but current methods treat retrieval and memory updates as separate processes. This separation limits learning efficiency and can lead to suboptimal performance over time. CoEvo-Mem addresses this gap by embedding both components in a unified, closed‑loop system.

## Implications
For AI practitioners, CoEvo-Mem offers a practical approach to maintain consistent agent behavior across extended interactions without manual re‑training. The method could be adopted by companies building autonomous agents that require persistent memory and adaptive retrieval.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01739v1)
