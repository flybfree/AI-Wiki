---
title: A Comparative Analysis of MLP and Kolmogorov-Arnold Networks (KAN) for Faster-than-Nyquist (FTN) Signaling Detection
url: http://arxiv.org/abs/2608.02062v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_11-07-20Z_AComparativeAnalysisofMLPandKolmogorov_ArnoldNetwo.md
generated_at: 2026-08-03 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares multilayer perceptrons (MLPs) and Kolmogorov-Arnold networks (KANs) for detecting faster‑than‑Nyquist BPSK signals in additive white Gaussian noise. Using a dataset of nearly four million labeled windows, the authors find that a KAN with hidden width 4 and spline grid size 5 achieves a lower bit error rate than an MLP of similar depth, while using far fewer parameters.

## Key Takeaways
- The KAN reaches a BER of 7×10⁻⁶ at ten decibels, which is about 18.6 times better than the MLP’s 1.3×10⁻⁴ BER under identical conditions.  
- The KAN requires only one‑eighth of the hidden width used by the best MLP (four versus thirty‑two), demonstrating superior parameter efficiency.  
- Despite its simplicity, the KAN outperforms the more complex MLP baseline in both performance and computational cost for FTN BPSK detection.

## Context
The study addresses a longstanding challenge in neural network design: balancing model complexity with inference speed for time‑packed signaling tasks. By leveraging data‑driven methods to select hidden widths, it illustrates how lightweight architectures can surpass heavier ones when evaluated on realistic channel conditions.

## Implications
For practitioners developing real‑time communication systems, this work suggests that KANs may be a viable alternative to traditional MLP pipelines, reducing hardware load and latency without sacrificing detection accuracy. The findings encourage further research into adaptive network structures for other FTL signaling scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02062v1)
