---
title: A Multiclass Quantum Aligned Centroid Kernel
published: 2026-07-22T06:03:20Z
authors: Kilian Tscharke, Pascal Debus
url: http://arxiv.org/abs/2607.19782v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multiclass Quantum Aligned Centroid Kernel

## Abstract
Kernel methods are powerful tools in machine learning but commonly used full-Gram kernels face three key limitations: (1) quadratic scaling with training set size; (2) the use of fixed, non-trainable kernels; and (3) the absence of an intrinsic formulation for multiclass classification. We present McQuack, a trainable quantum kernel method for multiclass problems that achieves linear scaling in the number of training samples. This is accomplished by replacing the full training-set Gram matrix with a trainable sample-to-(class-centroid) fidelity matrix. We evaluate the model in simulation and on 124 qubits of two IBM devices, across more than 150 datasets. In simulation, McQuack outperforms existing "pure" quantum baselines, while results from hardware inference -- obtained without training -- achieve performance similar to an RBF kernel. Finally, we study the trainability of the model and observe no evidence of barren plateaus in our experiments with up to 13 qubits, and highlight the importance of parameter initialization for successful optimization.

## Metadata
- **Published**: 2026-07-22T06:03:20Z
- **Authors**: Kilian Tscharke, Pascal Debus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19782v1)