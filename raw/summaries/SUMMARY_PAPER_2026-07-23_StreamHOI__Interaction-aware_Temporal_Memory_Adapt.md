---
title: StreamHOI: Interaction-aware Temporal Memory Adaptation for Streaming HOI Video Generation
url: http://arxiv.org/abs/2607.20174v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_14-06-39Z_StreamHOI_Interaction_awareTemporalMemoryAdaptatio.md
generated_at: 2026-07-23 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces StreamHOI, a low‑latency streaming framework for generating long‑duration human‑object interaction videos in real time. The authors address the trade‑off between historical memory usage and latency by profiling transformer blocks offline and applying bias‑guided training to specialize memory layouts per block. A distance scaling module is added to improve access to early interaction states, achieving 17.6 FPS with a 0.75 s first‑chunk latency.

## Key Takeaways
- The standard sink‑local memory design creates a trade‑off between historical memory and streaming latency in HOI video generation.
- Offline profiling of transformer blocks reveals block‑specific preferences for interaction versus surrounding regions, prompting bias‑guided training to adapt memory layouts.
- A distance scaling module enhances long‑range access to early interaction states, boosting plausibility and efficiency.

## Context
Real‑time interactive video generation remains a bottleneck in AI research because existing methods are designed for offline short clips with complex conditions. StreamHOI tackles this gap by rethinking how historical memory is organized within streaming pipelines, offering a practical path toward low‑latency applications such as AR and telepresence.

## Implications
For industry practitioners, StreamHOI provides a template to integrate interactive video generation into live systems without sacrificing frame rates or interaction quality. Researchers can leverage its block‑specific profiling approach to further optimize memory architectures for other streaming tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20174v1)
