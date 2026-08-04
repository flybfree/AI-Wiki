---
title: BiKAN: Restoring Collapsed Basis of Binary Kolmogorov--Arnold Networks
url: http://arxiv.org/abs/2608.01490v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_20-49-59Z_BiKAN_RestoringCollapsedBasisofBinaryKolmogorov__A.md
generated_at: 2026-08-03 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces BiKAN, a method to prevent the collapse of binary Kolmogorov‑Arnold Networks by adding degree‑2 Walsh characters that preserve pairwise coordinates. Experiments on CIFAR‑10 show that removing parity drops accuracy by 1.23 points (p = 0.003) and that more parity planes improve performance, especially at lower width. At a comparable parameter budget BiKAN beats conventional widening by 3.09 points with high confidence.

## Key Takeaways  
- Binary KAN layers suffer from Spatial Orthogonality Collapse because even powers become constant and odd powers reduce to the input variable, eliminating higher‑order features.  
- BiKAN restores explicit pairwise coordinates using fixed circular channel rolls that generate parities, combined with learned binary projections via XNOR‑popcount operations.  
- Adding parity planes yields a monotonic increase in accuracy; at equal budget parity outperforms widening by 3.09 points (p < 10⁻⁴).

## Context  
Binary KANs aim to reduce model size and compute cost, but their structural limitations hinder performance on complex tasks. This work demonstrates that simple algebraic augmentations can overcome the collapse, offering a lightweight alternative to traditional widening strategies.

## Implications  
For practitioners seeking efficient neural networks, BiKAN provides a hardware‑friendly solution that maintains high accuracy while minimizing DSP usage and compute latency. The approach supports deployment on low‑power FPGAs such as Zynq‑7020, where parity‑based designs achieve near‑zero DSP inference with minimal accuracy loss.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01490v1)
