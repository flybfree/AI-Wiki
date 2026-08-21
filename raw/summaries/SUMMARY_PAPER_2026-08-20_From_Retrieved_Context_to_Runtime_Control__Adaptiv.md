---
title: From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG
url: http://arxiv.org/abs/2608.19535v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_01-13-29Z_FromRetrievedContexttoRuntimeControl_AdaptiveCompr.md
generated_at: 2026-08-20 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces telemetry‑informed adaptive compression for edge‑based retrieval‑augmented generation (RAG), showing that dynamic control of context size can cut GPU energy by up to 48% and SoC power by up to 53% without harming quality. The authors demonstrate the method on NVIDIA Jetson AGX Thor using Llama and Qwen models, finding that compression is a dominant cost driver for larger generators.

## Key Takeaways
- Generation consumes roughly 90% of per‑query latency and 91% of GPU energy for 7B–8B models, making context length a major bottleneck.  
- Compression rates are not static; mild compression saves little while aggressive compression degrades inference quality, revealing an optimal operating region.  
- Runtime policies that adjust compression based on live workload telemetry can achieve up to 48% SoC energy reduction and 53% GPU energy saving with negligible quality loss.

## Context
Edge AI systems face tight constraints where every millisecond of latency and unit of power matters, especially for real‑time applications. Traditional RAG pipelines treat context compression as a one‑off offline setting, ignoring the dynamic workload and device state that affect both performance and resource usage.

## Implications
Adaptive compression offers a practical path to lower energy consumption in edge deployments without sacrificing user experience, supporting sustainable AI services. Practitioners can implement telemetry‑driven policies to balance latency, cost, and quality, making large language models more viable on constrained hardware.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19535v1)
