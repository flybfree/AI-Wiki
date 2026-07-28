---
title: Adaptive Data Admission and Retention for Streaming Federated Learning
published: 2026-07-27T04:31:12Z
authors: Zhuoyi Zhao, Ben Liang
url: http://arxiv.org/abs/2607.23987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Data Admission and Retention for Streaming Federated Learning

## Abstract
We study streaming federated learning with limited client memory, where newly generated training data incur time-varying sampling costs and must be selectively admitted and retained over time. We consider a joint server-side admission and client-side memory-management framework with the objective of minimizing the cumulative excess population risk under a sampling-cost budget and buffer constraints. We first derive a learning-error bound that explicitly captures the effects of instantaneous training sample size, distinct-sample growth, and reuse imbalance through a characterization of the effective sample size. Through a surrogate penalty obtained from this bound, we develop an Active-Constraint Drift-Plus-Penalty (ACDPP) policy that combines a structured client-side $K$-step retention rule with a server-side online admission rule and a time-varying rectangular admission region. We further present a sequence of comparison arguments, via an auxiliary constant-admission policy, that connects the ACDPP learning bound to a costless oracle benchmark. This yields explicit guarantees in terms of sublinear regret and sampling-cost violation, while the buffer-occupancy violation is controlled through offline selection of the retention horizon. Experiments on multiple datasets demonstrate that the proposed policy remains close to the oracle benchmark while satisfying the sampling-cost and buffer constraints.

## Metadata
- **Published**: 2026-07-27T04:31:12Z
- **Authors**: Zhuoyi Zhao, Ben Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23987v1)