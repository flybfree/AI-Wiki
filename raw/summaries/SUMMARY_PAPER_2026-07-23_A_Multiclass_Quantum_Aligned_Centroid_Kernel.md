---
title: A Multiclass Quantum Aligned Centroid Kernel
url: http://arxiv.org/abs/2607.19782v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_06-03-20Z_AMulticlassQuantumAlignedCentroidKernel.md
generated_at: 2026-07-23 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces McQuack, a trainable quantum kernel designed for multiclass classification that scales linearly with the number of training samples. By replacing the full Gram matrix with a trainable sample‑to‑class‑centroid fidelity matrix, the method achieves linear complexity and outperforms existing quantum baselines in simulation while matching RBF performance on hardware inference.

## Key Takeaways
- The model replaces the quadratic training‑set Gram matrix with a trainable fidelity matrix that links each sample to class centroids, enabling linear scaling.  
- In simulation, McQuack surpasses pure quantum kernels, and hardware inference without training yields results comparable to an RBF kernel.  
- Experiments up to 13 qubits show no barren plateaus, highlighting the role of proper parameter initialization for successful optimization.

## Context
Quantum kernel methods promise scalable machine learning by leveraging quantum circuits, yet full‑Gram kernels are computationally prohibitive and lack multiclass support. This work addresses those limitations with a trainable formulation that integrates classical centroids into quantum representations, aligning with broader efforts to make quantum algorithms practical for real‑world data.

## Implications
For practitioners, McQuack offers a viable path to deploying quantum classifiers on near‑term devices without sacrificing performance or training complexity. The findings suggest that hybrid approaches combining classical centroids with trainable quantum kernels could become standard in AI pipelines seeking efficient quantum advantage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19782v1)
