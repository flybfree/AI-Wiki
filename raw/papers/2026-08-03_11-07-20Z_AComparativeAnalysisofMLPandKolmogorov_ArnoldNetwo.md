---
title: A Comparative Analysis of MLP and Kolmogorov-Arnold Networks (KAN) for Faster-than-Nyquist (FTN) Signaling Detection
published: 2026-08-03T11:07:20Z
authors: Sude Ertan, Osman Tokluoglu, Enver Cavus
url: http://arxiv.org/abs/2608.02062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Comparative Analysis of MLP and Kolmogorov-Arnold Networks (KAN) for Faster-than-Nyquist (FTN) Signaling Detection

## Abstract
Faster-than-Nyquist signaling improves spectral ef- ficiency by deliberately introducing inter-symbol interference. Classical sequence detectors such as BCJR can approach optimal performance, but their computational cost grows rapidly with channel memory. This paper investigates data-driven FTN BPSK detection under AWGN through a direct comparison between multilayer perceptrons and Kolmogorov Arnold Networks. A large-scale Monte Carlo dataset containing nearly four million labeled windows is generated for a time-packing factor of zero point eight and signal-to-noise ratio values from seven to ten decibels. The best MLP obtained from width sweeping uses hidden width thirty two, whereas the selected KAN uses hidden width four with spline grid size five. At ten decibels, the MLP produces a bit error rate of one point three times ten to the minus four, while the KAN reaches seven times ten to the minus six. This corresponds to an eighteen point six times lower bit error rate while using only one eighth of the MLP hidden width. The results show that KAN provides a more effective and more parameter-efficient neural decision model than the MLP baseline for FTN BPSK detection.

## Metadata
- **Published**: 2026-08-03T11:07:20Z
- **Authors**: Sude Ertan, Osman Tokluoglu, Enver Cavus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02062v1)