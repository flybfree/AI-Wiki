---
title: Capacity Confounds and Coverage Guarantees in Adaptive Sub-model Federated Learning
published: 2026-08-07T12:26:03Z
authors: Alireza Moayedikia, Alicia Troncoso Lora
url: http://arxiv.org/abs/2608.07157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Capacity Confounds and Coverage Guarantees in Adaptive Sub-model Federated Learning

## Abstract
Sub-model federated learning lets resource-constrained clients train width-reduced versions of a global model, but existing methods allocate capacity by device resources alone. A natural next step, allocating capacity by each client's data heterogeneity as estimated from the updates the server already observes, has been repeatedly suggested. We ask whether that step is possible, using HAS-FL, an adaptive capacity-allocation framework, as a test case. Our findings are threefold. First, validated against ground-truth label-distribution divergence on reproducible partitions, update-divergence estimates of client heterogeneity are dominated by capacity rather than data: across two corrected estimators, multiple datasets, and all seeds, the estimates correlate strongly and negatively with device capacity, and no data signal remains once capacity is controlled for. This previously undocumented confound affects any method estimating client statistics from sub-model updates. Second, adaptive allocation has a hidden failure mode: when every client is capped below full width, the uncovered parameters stay at random initialization and progressively corrupt the global model. A simple coverage guarantee removes the failure and explains why uniform allocation collapses. Third, a matched-budget control settles what adaptivity contributes: random allocation to the same average budget performs no differently on both image benchmarks, and on the naturally partitioned text benchmark the adaptive policy is the weakest of the three strategies while consuming the most capacity. Sub-model training remains valuable because it admits constrained clients at quadratically reduced cost, but what protects accuracy is parameter coverage rather than allocation intelligence. Its apparent benefits come from capacity budgeting and coverage, and future designs need heterogeneity signals separable from capacity effects.

## Metadata
- **Published**: 2026-08-07T12:26:03Z
- **Authors**: Alireza Moayedikia, Alicia Troncoso Lora
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07157v1)