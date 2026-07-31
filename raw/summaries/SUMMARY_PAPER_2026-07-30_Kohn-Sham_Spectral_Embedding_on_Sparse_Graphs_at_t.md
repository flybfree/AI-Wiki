---
title: Kohn-Sham Spectral Embedding on Sparse Graphs at the Nishimori Temperature for Image Classification
url: http://arxiv.org/abs/2607.28428v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_16-05-51Z_Kohn_ShamSpectralEmbeddingonSparseGraphsattheNishi.md
generated_at: 2026-07-30 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Kohn-Sham Spectral Embedding (KSSE) which replaces dense CNNs with a sparse graph spectral embedding evaluated at the Nishimori temperature of an associated Random-Bond Ising Model. It solves D independent channel spectral problems in O(N log N + k^2_mode N) time using FFT on circulant blocks and low-order Rayleigh refinement, achieving 88.93% Top‑1 accuracy with about 21.24M parameters while outperforming Swin-L and matching ViT-H/14 under standard inductive setups.

## Key Takeaways
- KSSE maps pre-trained features onto quasi-cyclic low-density parity-check graphs using a regularized Laplacian as Kohn-Sham Hamiltonian, solving D independent channel spectral problems efficiently with FFT on circulant blocks.  
- The graph topology is optimized via star-domain surgery that creates local convexity around codewords while bounding residual frustration to ρ(B_γ) ≤ 1+δ, enabling Rayleigh refinement with k_mode=5 modes.  
- Theoretical results include a generalized Ihara-Bass identity linking belief propagation to the Laplacian and an additive channel separability bound, plus a fixed-point convergence theorem guaranteeing stable training.

## Context
The rise of large vision transformers has driven interest in lightweight yet high‑performing models that fit within limited compute budgets. Sparse graph neural networks offer a promising alternative by reducing parameter count and inference cost without sacrificing accuracy. This work demonstrates that physics‑inspired spectral embeddings can bridge this gap.

## Implications
For industry practitioners, KSSE provides a scalable architecture that delivers near‑state‑of‑the‑art image classification performance with dramatically smaller memory footprints, enabling deployment on edge devices. The theoretical guarantees also offer robustness to training dynamics, encouraging broader adoption of graph‑based vision models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28428v1)
