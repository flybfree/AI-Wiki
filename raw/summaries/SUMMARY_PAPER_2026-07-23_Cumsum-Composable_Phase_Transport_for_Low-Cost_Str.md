---
title: Cumsum-Composable Phase Transport for Low-Cost Streaming Keyword Spotting
url: http://arxiv.org/abs/2607.20086v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_12-36-53Z_Cumsum_ComposablePhaseTransportforLow_CostStreamin.md
generated_at: 2026-07-23 23:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces cumsum‑composable phase transport as a streaming‑native temporal layer for keyword spotting. The method projects acoustic frames to complex channels, applies unitary rotations, accumulates a finite window with prefix differences, and updates via gated residuals, achieving exact batched training and online inference with minimal latency.

## Key Takeaways
- The unitary rotation constraint ensures that inverse rotations have unit norm, which keeps the prefix representation well‑conditioned while memory is supplied by fixed windows or block readouts.  
- A 24.8K‑parameter model reaches 96.8% test accuracy on Google Speech Commands v2, matching a 51.6K tied model and beating a 25.6K MelCNNMaxPool baseline at 97.3%.  
- Training is 1.07× faster than scan‑style baselines and single‑example latency drops from 7.09 ms to 5.01 ms on a Tesla T4.

## Context
Streaming speech tasks demand models that maintain compact recurrent state yet avoid the high constants of traditional scan kernels. This work offers a low‑cost alternative that fits within the streaming paradigm, aligning with ongoing efforts to reduce model size and inference time for real‑time applications.

## Implications
The proposed phase transport can be integrated into existing streaming pipelines without major architectural changes, enabling faster training cycles and lower latency for edge devices. Practitioners may adopt it to improve keyword spotting performance while keeping resource constraints in check.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20086v1)
