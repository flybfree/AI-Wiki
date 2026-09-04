---
title: GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving
url: http://arxiv.org/abs/2609.03494v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_07-53-05Z_GrowPage_On_DemandKVBudgetingforEfficientLLMReason.md
generated_at: 2026-09-03 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes GrowPage, an on‑demand KV budgeting framework that dynamically allocates memory for large language model reasoning tasks. Experiments demonstrate that GrowPage improves the throughput‑accuracy trade‑off compared with static compression methods.

## Key Takeaways  
- GrowPage treats KV capacity as a runtime resource rather than a fixed per‑request limit, allowing it to adapt to varying attention demands during generation.  
- It uses lightweight dual‑timescale query summaries to capture recent and long‑term attention patterns, providing estimates for demand evolution at each capacity boundary.  
- When broader demand is detected, GrowPage either compresses existing KV states or requests an additional physical page, preserving continuous batching and prefix caching.

## Context  
LLM serving faces memory bottlenecks as reasoning tasks generate large key‑value caches. Traditional compression techniques lock in a static budget, which can lead to underutilization or overflow. Dynamic budgeting approaches like GrowPage address this by aligning memory usage with actual workload variability.

## Implications  
GrowPage enables more efficient resource utilization, reducing latency and increasing throughput for demanding reasoning applications. Practitioners can adopt its page‑level abstraction to scale models without sacrificing batching benefits, supporting broader deployment of large language systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03494v1)
