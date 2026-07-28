---
title: HiTMS: A High-Throughput Multi-Stream Linguistic Steganography Framework
url: http://arxiv.org/abs/2607.23597v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_10-54-44Z_HiTMS_AHigh_ThroughputMulti_StreamLinguisticStegan.md
generated_at: 2026-07-27 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HiTMS, a high‑throughput multi‑stream linguistic steganography framework that hides secret bits across multiple model responses within large language models. It achieves up to 4.3 times faster embedding and extraction compared with single‑stream baselines while lowering detection accuracy.

## Key Takeaways
- The framework spreads the secret over several rounds, each containing multiple streams in a batched call, which amortizes model invocation cost.
- Each response is wrapped in a self‑describing frame and uses a key‑derived schedule to bind streams to slots, filling unused slots with decoys so recovery is exact and slot occupancy remains hidden.
- Across eight experimental settings, HiTMS outperforms single‑stream methods by delivering higher throughput and reducing steganalyzer AUROC from 0.681 to 0.601.

## Context
Current linguistic steganography relies on a single response per secret, limiting scalability for batched inference tasks. As AI models generate responses in parallel, efficient multi‑stream embedding is needed to exploit concurrency without sacrificing concealment.

## Implications
HiTMS enables developers to embed multiple secrets simultaneously, improving system efficiency and reducing latency. This approach could be adopted by security tools that need covert data transfer within AI interactions, offering a practical balance between speed and stealth.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23597v1)
