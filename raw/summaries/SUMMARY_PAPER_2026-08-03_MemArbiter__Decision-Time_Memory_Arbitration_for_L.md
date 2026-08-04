---
title: MemArbiter: Decision-Time Memory Arbitration for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2608.02113v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_12-10-52Z_MemArbiter_Decision_TimeMemoryArbitrationforLong_H.md
generated_at: 2026-08-03 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
MemArbiter tackles the Memory-Action Gap by providing a function‑aware arbitration mechanism that organizes long‑horizon LLM agent memory into structured banks and dynamically controls which information influences decisions. The framework improves action success rates under limited per‑step token budgets, outperforming baselines by up to 25 percentage points on ALFWorld. These gains demonstrate that accessible yet prioritized memory can guide coherent actions.

## Key Takeaways
- MemArbiter decomposes interaction histories into atomic items and groups them into five functional Memory Banks to organize information for later retrieval.  
- The system combines bank‑level demand, item‑level relevance, focal‑ambient representations, and a temporal presentation gate to dynamically adjust memory salience at each decision step.  
- Under 500‑token and 750‑token budgets, MemArbiter achieves success rates of 82.8% and 92.5%, respectively, surpassing the strongest baseline by significant margins.

## Context
Long‑horizon LLM agents face challenges in retaining cross‑step information that remains actionable despite being stored in memory. Existing retrieval methods focus on accessibility but not on how memory is prioritized or presented at decision time. MemArbiter addresses this gap by introducing a structured arbitration layer that aligns memory organization with functional demands.

## Implications
The results suggest that function‑aware memory management can be integrated into action‑generation pipelines to boost performance without increasing token budgets, offering a practical improvement for industry practitioners developing long‑term AI agents. This work may inspire further research on adaptive memory systems in autonomous software and robotics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02113v1)
