---
title: DG-FedReuse: Proxy-Gradient-Gated Cached-Update Reuse with Matched Sparse Uplink Accounting
url: http://arxiv.org/abs/2608.05358v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_19-30-04Z_DG_FedReuse_Proxy_Gradient_GatedCached_UpdateReuse.md
generated_at: 2026-08-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DG-FedReuse, a simulator‑level mechanism that lets selected federated clients reuse cached model updates when a stochastic head‑gradient discrepancy stays below a round‑dependent threshold. Experiments on six image classification datasets with 50 virtual clients show an uplink saving of 83.4 % compared to matched Top‑K FedAvg while only trading off up to 0.45 percentage points in test accuracy.

## Key Takeaways
- The reuse rule allows age‑decayed cached updates to be sent when a proxy discrepancy is low, limiting cache‑age with a hard limit and enforcing a minimum fresh client quota.
- Fresh updates are represented adaptively using a per‑tensor Top‑K field, which balances novelty and compression without sacrificing model fidelity.
- The communication savings remain high even under test‑controlled checkpointing, but the headline saving drops to 41.7 % when dense downlinks are considered, highlighting dependence on accounting boundaries.

## Context
Federated learning struggles with repeated transmission of locally optimized models, inflating bandwidth and energy costs. Prior work focuses on stale‑update mechanisms or lazy aggregation, yet few address how reuse can be safely bounded while preserving model quality across heterogeneous label distributions.

## Implications
For practitioners, DG-FedReuse offers a practical way to reduce uplink traffic without requiring full model re‑training, which could lower cloud costs and improve privacy. However, the method’s effectiveness hinges on careful selection of thresholds and quota enforcement, making it a tool for iterative optimization rather than a universal solution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05358v1)
