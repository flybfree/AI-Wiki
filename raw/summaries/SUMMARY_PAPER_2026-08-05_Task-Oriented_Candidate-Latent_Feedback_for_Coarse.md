---
title: Task-Oriented Candidate-Latent Feedback for Coarse-to-Fine Sensing in Distributed OFDM-ISAC Networks
url: http://arxiv.org/abs/2608.03319v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_08-26-06Z_Task_OrientedCandidate_LatentFeedbackforCoarse_to_.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a task-oriented feedback scheme for coarse-to-fine sensing in distributed OFDM-ISAC networks that reduces communication overhead while preserving detection accuracy. It demonstrates that candidate-latent feedback can achieve high detection rates with minimal data transmission compared to full DDAE tensors. The proposed pipeline yields 96.33–98.88% detection across three design points.

## Key Takeaways
- The lightweight convolutional scorer generates a dense delay-Doppler proposal map from pilot-based OFDM estimates, enabling compact candidate selection.
- Learned encoder compresses per-candidate azimuth-elevation patches into K tokens using b bits, achieving compression ratios up to 9.2×10^4 over the full magnitude tensor.
- Uniform quantization and a fixed feedback budget B_fb = bKC + 18K + 16 bits allow sub‑Mbit/s transmission while maintaining detection at or above 96% across urban and campus scenes.

## Context
This work addresses the communication bottleneck in integrated sensing and communication systems where raw channel data is costly to forward. By leveraging AI‑driven candidate latent encoding, it enables real‑time inference without sacrificing performance, aligning with trends toward edge‑centric and low‑bandwidth ISAC architectures.

## Implications
For industry, the approach reduces sensor network latency and power consumption while supporting high‑resolution target tracking. Practitioners can adopt this feedback framework to design scalable distributed sensing platforms that operate efficiently in cluttered environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03319v1)
