---
title: LLM-Guided Initialization for Accelerated Hybrid Quantum-Classical Medical Image Classification
published: 2026-07-29T07:24:48Z
authors: Riza Alaudin Syah, Irwan Alnarus Kautsar, Haza Nuzly Bin Abdull Hamed
url: http://arxiv.org/abs/2607.27262v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-Guided Initialization for Accelerated Hybrid Quantum-Classical Medical Image Classification

## Abstract
Variational quantum algorithms often encounter barren plateaus, where cost gradients decay rapidly with increasing circuit depth, undermining the trainability of parameterized quantum circuits. This paper evaluates AdaInit (Adaptive Initialization), proposed by Zhuang and Cunningham, which uses large language models to propose initial parameters for quantum neural networks. We study a simplified single-query AdaInit variant paired with GPU-accelerated simulation in NVIDIA CUDA-Q and apply it to binary classification on the DMR-IR mammography dataset. AdaInit delivers 14.6 times higher gradient variance at initialization than random initialization (0.0095 vs. 0.0006), producing 160 times faster convergence (1.1s vs. 176 s) while maintaining the same classification accuracy of 61.4 percent. We provide theoretical analysis grounded in the geometry of parameterized circuit landscapes and show empirically that LLM-guided initialization places the optimizer in trainable regions of parameter space. Beyond performance, our results indicate that a single LLM query can yield informative parameters without iterative refinement, suggesting a low-overhead path to improved trainability. The findings validate AdaInit in a medical imaging setting and demonstrate its compatibility with GPU-accelerated quantum backends for practical speedups.

## Metadata
- **Published**: 2026-07-29T07:24:48Z
- **Authors**: Riza Alaudin Syah, Irwan Alnarus Kautsar, Haza Nuzly Bin Abdull Hamed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27262v1)