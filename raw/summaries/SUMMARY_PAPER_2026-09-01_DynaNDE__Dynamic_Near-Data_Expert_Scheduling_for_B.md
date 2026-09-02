---
title: DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference
url: http://arxiv.org/abs/2609.00407v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_21-38-59Z_DynaNDE_DynamicNear_DataExpertSchedulingforBatched.md
generated_at: 2026-09-01 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
DynaNDE is a dynamic near-data expert scheduling framework that leverages NPU‑NDP collaboration to accelerate batched MoE inference. The paper demonstrates substantial speedups, achieving average gains of 2.6× for prefill and 2.2× for decoding stages over existing state‑of‑the‑art systems.

## Key Takeaways
- DynaNDE introduces an analytical model that captures hardware heterogeneity, data‑movement costs, and communication‑computation overlap in NPU‑NDP execution.
- The framework schedules experts per layer across both devices while respecting expert‑level concurrency, reducing unnecessary parameter movement.
- A reuse‑aware runtime avoids redundant memory accesses when experts reside in NPU memory during batched inference.

## Context
Large language models rely on MoE architectures to scale efficiently, yet deployment on heterogeneous hardware such as NPUs introduces bottlenecks due to data transfer. Near‑Data Processing (NDP) aims to mitigate these bottlenecks by executing computation close to the data, but current solutions lack dynamic scheduling that adapts to varying workloads and device capabilities.

## Implications
This work offers a practical solution for deploying MoE models on edge or low‑power devices where latency and power efficiency are critical. Practitioners can expect measurable throughput improvements without redesigning model architectures, encouraging broader adoption of MoE in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00407v1)
