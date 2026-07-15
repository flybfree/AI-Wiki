---
title: "Summary: FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels"
date: 2026-04-22
tags: ['paper', 'research', 'ai']
---
# Summary: FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels


**Source**: [Original Paper](http://arxiv.org/abs/2604.20825v1)
Saved: 2026-05-07 22:24
Source: 2026-04-22_17-49-20Z_FedSIR_SpectralClientIdentificationandRelabelingfo.md
Model: None

---

## Summary
FedSIR is a multi-stage federated learning framework for handling noisy labels by using the spectral structure of client feature representations. It identifies clean versus noisy clients via spectral consistency, uses clean clients as references to help relabel corrupted samples on noisy clients, and adds a noise-aware training pipeline with logit-adjusted loss, knowledge distillation, and distance-aware aggregation. The paper reports consistent gains over prior methods on standard FL benchmarks.

## Key Takeaways
- Uses spectral consistency of class-wise feature subspaces to distinguish clean and noisy clients with low communication overhead.
- Relabels noisy samples using dominant class directions and residual subspaces from clean-client spectral references.
- Combines logit-adjusted loss, knowledge distillation, and distance-aware aggregation for more stable federated optimization.
- Claims state-of-the-art performance on standard noisy-label FL benchmarks.

## Original Reference
- Title: FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels
- Authors: Sina Gholami, Abdulmoneam Ali, Tania Haghighi, Ahmed Arafa, Minhaj Nur Alam
- URL: http://arxiv.org/abs/2604.20825v1
- Published: 2026-04-22T17:49:20Z