---
title: LITEWAY: LIghtweight HAR via Temporal Efficient highWAY
url: http://arxiv.org/abs/2608.09421v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_10-49-17Z_LITEWAY_LIghtweightHARviaTemporalEfficienthighWAY.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LITEWAY, a modality‑agnostic fully convolutional model for wearable human activity recognition that replaces recurrent networks with structured convolutional decomposition. The authors demonstrate that LITEWAY achieves competitive macro F1 scores while shrinking model size by up to ninefold and cutting energy consumption by more than twofold compared with existing lightweight baselines.

## Key Takeaways
- LITEWAY eliminates recurrent layers such as GRU and LSTM, enabling parallel convolutional processing and lower inference latency.  
- The framework reduces model size from 4.06x to 9.52x relative to TinyHAR/TinierHAR, with full‑depth versions offering reductions of up to ninefold.  
- Energy savings range from 2.29x to 3.14x versus TinierHAR and MLP‑HAR, highlighting efficient temporal modeling for resource‑constrained devices.

## Context
Wearable HAR systems must balance accuracy with computational efficiency due to limited battery life and processing power. Convolutional architectures are gaining traction as they can exploit GPU/TPU parallelism, but integrating temporal dependencies remains a challenge without recurrence. This work advances the field by providing a scalable convolution‑based alternative that meets both size and energy constraints.

## Implications
For developers of smart wearables, LITEWAY offers a practical path to deploy high‑quality activity recognition without sacrificing performance or battery life. The model’s modularity encourages integration into existing sensor pipelines, potentially lowering development costs and enabling broader adoption across consumer health devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09421v1)
