---
title: SparseKAN: Compressing Kolmogorov--Arnold Networks Across Basis Functions, Neurons, and Bits
published: 2026-08-01T20:42:41Z
authors: Kazi Ahmed Asif Fuad, Lizhong Chen
url: http://arxiv.org/abs/2608.00859v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SparseKAN: Compressing Kolmogorov--Arnold Networks Across Basis Functions, Neurons, and Bits

## Abstract
Kolmogorov--Arnold Networks (KANs) replace scalar edge weights with learnable univariate functions parameterized by multiple basis coefficients. This introduces a source of redundancy that conventional neural-network compression does not directly expose. We present \textbf{SparseKAN}, a unified approach that compresses KANs along three complementary axes: basis functions, neurons/channels, and numerical precision. SparseKAN equips the base branch, nonlinear basis branch, and individual basis terms with hierarchical learnable gates trained under a differentiable active-cost objective. The learned importance structure is subsequently hardened under explicit basis and width budgets, recovered in full or low precision, and physically compacted into smaller dense tensors rather than retained as sparse masks. Experiments on MNIST, CIFAR-10, and CIFAR-100 across spline, polynomial, RBF, wavelet, and convolutional KAN variants show that the structural axes compose predictably in cost. We also find strong basis-dependent differences in term importance: coefficient-based selection outperforms matched low-order truncation by up to 15.25 accuracy points in the evaluated Gram-polynomial settings. Eight-bit quantization is broadly robust, whereas 4-bit convolutional KANs require quantization-aware adaptation. Physical compaction removes up to 73.0\% of parameters without accuracy loss on MNIST and reduces large-batch CUDA latency to as little as $0.51\times$ dense execution. On a ZCU104 FPGA, the resulting sparse low-bit models achieve up to $23.63\times$ lower inference latency, demonstrating that SparseKAN converts functional redundancy into measurable software and hardware efficiency. The SparseKAN implementation is available at https://github.com/OSU-STARLAB/SparseKAN.

## Metadata
- **Published**: 2026-08-01T20:42:41Z
- **Authors**: Kazi Ahmed Asif Fuad, Lizhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00859v1)