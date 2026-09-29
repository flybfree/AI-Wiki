---
title: TempoKV: Timely Staging of LLM KV Caches for Memory-Semantic Flash
published: 2026-09-28T12:55:20Z
authors: Jay H. Park, Hyungjun Kim, Dong Kim
url: http://arxiv.org/abs/2609.35065v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TempoKV: Timely Staging of LLM KV Caches for Memory-Semantic Flash

## Abstract
Reusable prefix key-value (KV) caches can outgrow GPU memory in large language model (LLM) serving. A memory-semantic flash hierarchy offers SSD-backed capacity with a limited fast tier, but a logical KV hit is not necessarily ready for GPU retrieval. Demand staging exposes SSD latency, whereas immediate staging can reserve fast-tier capacity long before retrieval begins. We present TempoKV, a timing-aware resource-commitment layer that separates early knowledge of reuse from the acquisition of staging resources. It records reusable-KV hits as metadata-only claims and requests commitment when the runtime-estimated time until retrieval falls to the storage-estimated time needed to make KV resident and protected against eviction. These estimates adapt to runtime progress and staging state, while commitment remains subject to available protected capacity. We implement TempoKV in vLLM and LMCache on an SSD-backed CXL memory device without changing request scheduling. Across two models and three prefix cache ratios, TempoKV reduces protected fast-tier byte-time per request by 63-91% versus immediate staging while retaining much of the serving benefit of advance staging. In a fast-tier capacity sweep, output throughput and p95 time to first token (TTFT) remain nearly unchanged as capacity decreases from 100 to 25 GiB. Compared with unmodified LMCache's Device-DAX L1 configuration, TempoKV reduces p95 TTFT by up to 48.0% and increases output throughput by up to 27.8%.

## Metadata
- **Published**: 2026-09-28T12:55:20Z
- **Authors**: Jay H. Park, Hyungjun Kim, Dong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35065v1)