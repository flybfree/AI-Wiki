---
title: GBU-Palm: A Multimodal Video Dataset and Benchmark for Palm Presentation Attack Detection
url: http://arxiv.org/abs/2608.14389v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-31-48Z_GBU_Palm_AMultimodalVideoDatasetandBenchmarkforPal.md
generated_at: 2026-08-16 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GBU-Palm, a multimodal video dataset with 21,326 videos from 105 subjects and 210 palms across six acquisition environments. The benchmark includes synchronized RGB-NIR samples and evaluates four video architectures under both environment-matched and held-out settings. Results show architecture-specific degradation when moving between environments.

## Key Takeaways
- GBU-Palm provides a large multimodal video dataset with synchronized RGB-NIR frames, enabling evaluation of palm presentation attack detection across diverse acquisition conditions.
- The study demonstrates that architectural performance drops significantly under environmental shifts, highlighting the importance of environment consistency for model robustness.
- Analysis using true accept/reject and false rates reveals that RGB-NIR fusion does not consistently outperform RGB-only inputs, indicating trade‑offs in feature utilization.

## Context
Current palm presentation attack detection research often relies on static images or limited video samples, making cross‑environment comparisons difficult. This work addresses the gap by offering a comprehensive video benchmark that captures both visual and infrared cues under varied lighting and capture setups.

## Implications
For practitioners developing PAD systems, GBU-Palm offers a standardized test suite to stress‑test multimodal models against real‑world deployment variations. Industry adoption of such benchmarks could lead to more reliable security solutions for high‑value events where palm attacks are a concern.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14389v1)
