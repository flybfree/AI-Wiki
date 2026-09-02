---
title: mzCache: On-Device LLM Memory Management under Multitasking
url: http://arxiv.org/abs/2609.01338v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-49-20Z_mzCache_On_DeviceLLMMemoryManagementunderMultitask.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces mzCache, an on‑device LLM inference system designed to manage model weights and key‑value cache under mobile multitasking pressure. By partitioning memory into fine‑grained shared buffers and using hybrid eviction policies, it enables zero‑wait GPU inference with concurrent CPU restoration, achieving a 2.1–5.5× speedup over storage‑backed partial offload.

## Key Takeaways
- mzCache partitions LLM memory into fine‑grained shared buffers that allow partial evictions and restorations while keeping cross‑processor access possible.
- It employs hybrid swap and backward‑out eviction policies to guarantee low‑latency restoration from any eviction state, avoiding full recomputation of the KV cache.
- The system is implemented in llama.cpp and deployed as an Android app, delivering 2.1–5.5× reduction in Time‑to‑First‑Token compared with storage‑backed partial offload.

## Context
Mobile devices face unpredictable memory pressure when users switch applications, forcing LLM components to be evicted from RAM or storage. Traditional approaches either store all model data on slow external storage or recompute the entire KV cache, both of which degrade responsiveness and battery efficiency. mzCache addresses these bottlenecks by leveraging the unified memory architecture of modern mobile SoCs.

## Implications
This work demonstrates that intelligent memory management can make LLM inference feel instantaneous even under heavy multitasking loads, encouraging developers to embed such systems in production apps. For industry stakeholders, it reduces latency‑related churn and improves user experience on resource‑constrained devices, setting a new standard for on‑device AI performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01338v1)
