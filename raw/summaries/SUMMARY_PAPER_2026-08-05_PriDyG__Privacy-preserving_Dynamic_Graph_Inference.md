---
title: PriDyG: Privacy-preserving Dynamic Graph Inference with LLM-GNN Collaboration
url: http://arxiv.org/abs/2608.04255v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_22-23-19Z_PriDyG_Privacy_preservingDynamicGraphInferencewith.md
generated_at: 2026-08-05 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces PriDyG, a privacy‑preserving framework that merges GNN structural learning with LLM semantic reasoning to perform dynamic graph inference without leaking edge details. Experiments show PriDyG outperforms geometrically decaying baselines under the same privacy budget while matching the utility of naive per‑update retraining and reducing cumulative privacy cost by up to three orders of magnitude.

## Key Takeaways
- EDG’s incremental private multi‑hop aggregation buffers new edges so each edge is processed exactly once, keeping total privacy cost constant regardless of update frequency.  
- The parallel composition ensures the noise budget equals that of a single static release, avoiding exponential growth in privacy loss while preserving exact one‑hop signals and at least half of two‑hop information transfers.  
- LLM predictions are derived only from node text, incurring no additional edge‑level privacy cost.

## Context
Dynamic graph inference is increasingly common in real‑time recommendation systems where models must adapt to new relational data without exposing sensitive edges. Traditional approaches suffer from cumulative differential privacy violations as updates accumulate, limiting model utility and scalability. This work addresses that challenge by designing a framework that balances privacy guarantees with high performance.

## Implications
For practitioners, PriDyG offers a practical way to maintain strong privacy while continuously updating graph models, reducing the need for costly re‑training cycles. The industry can adopt this approach in large‑scale recommendation platforms where user data sensitivity is paramount and model latency must be minimized.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04255v1)
