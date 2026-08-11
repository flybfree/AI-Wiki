---
title: Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation
published: 2026-08-09T04:22:57Z
authors: Kaichen Zhang, Wei Huang, Keming Wu, Bo Li, Xiaojuan Qi
url: http://arxiv.org/abs/2608.08469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aero Realtime: Fully Aligned Input-Output Streams for Low-Latency Streaming Multimodal Generation

## Abstract
Existing streaming multimodal models process observations incrementally but still follow a turn-based prefill-then-decode pattern, making them non-duplex: new observations cannot naturally enter an active generation stream. Proactive alternatives use micro-turn polling or external response gates, which fragment continuous interaction, decouple response timing from language generation, and complicate KV-cache-friendly serving. We introduce Aero Realtime, a 4B streaming multimodal model with a duplex architecture for realtime generation. Aero Realtime aligns video, audio, and textual output on a shared temporal grid, where each approximately 80-ms audio slot predicts either a lexical token or a silence token. This allows input and output to advance together, enabling one autoregressive objective to learn both when to respond and what to generate. During inference, Aero Realtime appends only the newest multimodal slot, carries forward the previous output state, and reuses the KV cache for efficient incremental execution. We further provide a complete training and serving recipe, including realtime QA construction, slot-aligned supervision, hardware-aware distributed training, and resumable inference. On four NVIDIA A6000 workstation GPUs, Aero Realtime maintains 84-ms median and 173-ms P95 processing lag over 20 minutes of a continuously streamed video, remaining within 200~ms of the source timeline. These results demonstrate the feasibility of fully aligned input-output modeling for duplex, proactive, and hardware-aligned multimodal interaction.

## Metadata
- **Published**: 2026-08-09T04:22:57Z
- **Authors**: Kaichen Zhang, Wei Huang, Keming Wu, Bo Li, Xiaojuan Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08469v1)