---
title: Sustaining Plasticity via Learnable Wavelet Activations in Continual Learning
published: 2026-08-13T06:38:04Z
authors: Zeyang Zhang, Tieliang Gong, Junyan Lu, Weizhan Zhang
url: http://arxiv.org/abs/2608.12874v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sustaining Plasticity via Learnable Wavelet Activations in Continual Learning

## Abstract
Plasticity loss has emerged as a critical challenge in continual learning that significantly hinders the acquisition of sequential tasks. While optimizing activation designs offers a potential solution, current fixed-form functions suffer from an inherent spectral bias towards low-frequency variations, whereas learnable variants permit unconstrained updates that induce catastrophic forgetting. To address these limitations, we propose a novel learnable wavelet activation that decomposes the activation function into low-frequency and high-frequency components to explicitly counter spectral bias. Furthermore, we employ dynamic wavelet injection to adaptively enhance plasticity for new tasks, alongside a regularization strategy to ensure the stability of previous learned knowledge. Theoretically, we provide rigorous mathematical guarantees for the proposed framework, proving the structural necessity of the hybrid wavelet architecture for efficient $L^2$ approximation and demonstrating that the decoupled learning rate mechanism successfully restores network plasticity for high-frequency information. Additionally, we provide a formal derivation of the loss-driven injection trigger mechanism to precisely guide the injection. Extensive empirical evaluations demonstrate that our approach maintains superior trainability and generalization throughout the learning process and achieves state-of-the-art performance across diverse continual learning benchmarks.

## Metadata
- **Published**: 2026-08-13T06:38:04Z
- **Authors**: Zeyang Zhang, Tieliang Gong, Junyan Lu, Weizhan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12874v1)