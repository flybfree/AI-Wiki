---
title: Adaptive Data Admission and Retention for Streaming Federated Learning
url: http://arxiv.org/abs/2607.23987v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_04-31-12Z_AdaptiveDataAdmissionandRetentionforStreamingFeder.md
generated_at: 2026-07-27 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses streaming federated learning where clients have limited memory and each new sample incurs a time‑varying sampling cost. It proposes an Active‑Constraint Drift‑Plus‑Penalty policy that jointly decides which samples to admit on the server and how long to keep them on the client, aiming to minimize excess population risk within budget and buffer limits.

## Key Takeaways
- The effective sample size is derived to capture instantaneous training sample size, distinct‑sample growth, and reuse imbalance, providing a learning error bound that links these factors. 
- A surrogate penalty based on this bound yields an Active‑Constraint Drift‑Plus‑Penalty policy combining a K‑step retention rule with an online admission region. 
- The paper shows sublinear regret guarantees and controls sampling‑cost and buffer violations, while buffer occupancy is managed offline via horizon selection.

## Context
Federated learning systems often face the challenge of continuously adding data without exceeding client memory or server bandwidth constraints. This work tackles those practical limits by formalizing admission and retention decisions as an optimization problem with clear risk bounds.

## Implications
For practitioners, the approach offers a near‑optimal strategy that can be deployed in real‑time federated setups, reducing unnecessary data storage and computational waste while preserving model quality. It also provides theoretical tools to evaluate similar streaming policies under resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23987v1)
