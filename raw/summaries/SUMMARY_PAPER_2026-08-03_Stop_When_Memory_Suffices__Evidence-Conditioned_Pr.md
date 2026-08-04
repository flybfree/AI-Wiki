---
title: Stop When Memory Suffices: Evidence-Conditioned Progressive Execution for LLM Agents
url: http://arxiv.org/abs/2608.01285v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_14-49-24Z_StopWhenMemorySuffices_Evidence_ConditionedProgres.md
generated_at: 2026-08-03 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Router-Mem, an evidence-conditioned progressive execution framework that balances answer quality with low latency in long-horizon LLM agents. By using a shared retrieval prefix and a sufficiency router, it can decide early whether the context is enough to terminate inference. Experiments show improved scores on AMA-Bench and BEAM while cutting average inference time.

## Key Takeaways
- Router-Mem uses a low‑cost retrieval prefix to fetch evidence quickly, enabling fast online access.
- The sufficiency router predicts if the retrieved evidence supports early termination, allowing single‑token decisions at inference time.
- When evidence is insufficient, the system expands memory blocks and performs deeper analysis, improving answer quality.

## Context
Long‑term memory in LLMs remains a bottleneck because either full history processing incurs high latency or compressed retrieval may miss temporal dependencies. This work addresses that trade‑off by proposing an adaptive execution strategy that dynamically decides how much to retrieve versus analyze.

## Implications
Practitioners can implement Router-Mem to reduce inference costs without sacrificing performance, making persistent agents more scalable for real‑time applications. The approach opens a path toward truly efficient long‑horizon reasoning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01285v1)
