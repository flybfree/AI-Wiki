---
title: LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving
url: http://arxiv.org/abs/2608.08382v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_00-28-05Z_LLMVisor_AReal_TimeLatencyAttributionModelforMulti.md
generated_at: 2026-08-11 12:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LLMVisor, a real-time latency attribution model for multi‑tenant LLM serving that decomposes batch latency into additive per‑request shares using a roofline‑guided piecewise‑linear form. The model captures both memory‑bound and compute‑bound phases through features proportional to FLOPs and memory I/O traffic, achieving near‑perfect R‑squared and reducing relative error up to 4.4× at the p99 for decode tasks compared with a token‑count baseline.

## Key Takeaways
- The model captures memory‑bound and compute‑bound phases via concise piecewise‑linear features proportional to FLOPs and memory I/O traffic, enabling accurate per‑request latency attribution.
- LLMVisor runs efficiently at microsecond scale inside the scheduling loop, providing additive per‑request shares that are lightweight for real‑time use.
- Evaluation on Llama 3.1‑8B and Qwen 2.5 models shows near‑perfect R‑squared with relative error reductions up to 4.4× at p99 for decode tasks.

## Context
Multi‑tenant LLM serving faces challenges in isolating per‑tenant usage due to co‑batching, which complicates resource allocation and control. Real‑time latency attribution is needed to allocate GPU resources fairly and efficiently across tenants.

## Implications
This model enables more transparent and fair scheduling of GPU clusters, improving throughput and user experience. Practitioners can integrate LLMVisor into existing inference pipelines without significant overhead, supporting scalable multi‑tenant AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08382v1)
