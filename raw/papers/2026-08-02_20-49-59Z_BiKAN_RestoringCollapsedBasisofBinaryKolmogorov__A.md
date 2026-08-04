---
title: BiKAN: Restoring Collapsed Basis of Binary Kolmogorov--Arnold Networks
published: 2026-08-02T20:49:59Z
authors: Kazi Ahmed Asif Fuad, Lizhong Chen
url: http://arxiv.org/abs/2608.01490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BiKAN: Restoring Collapsed Basis of Binary Kolmogorov--Arnold Networks

## Abstract
Binarizing a polynomial Kolmogorov--Arnold Network (KAN) not only changes parameter precision, but also alters the function space available to each layer. When activations are restricted to ${-1,+1}$, all even powers reduce to $1$ and all odd powers reduce to $x$, causing the elementwise polynomial basis to collapse to constant and first-order responses. We refer to this structural failure as Spatial Orthogonality Collapse. Our proposed BiKAN addresses this critical issue by augmenting each binary KAN layer with selected degree-2 Walsh characters. Fixed circular channel rolls generate pairwise parities, and learned binary projections mix them using the same XNOR--popcount operations as the remaining W1A1 paths. This restores explicit pairwise coordinates without learned routing or multiplier-based feature generation. Experiments on CIFAR-10 confirms that removing parity reduces accuracy by $1.23$ points over five paired seeds ($p=0.003$), the gain increases as width decreases, and accuracy improves monotonically as more parity planes are added. At an equal $\sim$11.9M-parameter budget, parity outperforms conventional widening by $3.09$ points ($p<10^{-4}$). At W1A1, BiKAN reaches $99.48\%$, $84.38\%$, and $55.81\%$ on MNIST, CIFAR-10, and CIFAR-100, respectively. Post-route Zynq-7020 FPGA results show that the repair remains hardware-efficient; the convolutional design cuts DSP usage from 164 to 72 and estimated compute-core latency from 401 to 54.8 ms, while the power-of-two-aware dense design achieves zero-DSP inference with a 0.03-point accuracy loss. The BiKAN implementation is available at https://github.com/OSU-STARLAB/BiKAN.

## Metadata
- **Published**: 2026-08-02T20:49:59Z
- **Authors**: Kazi Ahmed Asif Fuad, Lizhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01490v1)