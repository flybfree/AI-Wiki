---
title: Sinkhorn Linearization and the Spectral Proxy: Unifying the Statistical and Algorithmic Theory of Feature-Parameterized Inverse Optimal Transport via a Single Spectral Sandwich
url: http://arxiv.org/abs/2608.13201v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-03-55Z_SinkhornLinearizationandtheSpectralProxy_Unifyingt.md
generated_at: 2026-08-13 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper establishes a unified statistical and algorithmic framework for inverse optimal transport under feature‑parameterized costs. It introduces Sinkhorn linearization and its spectral proxy, which yields a tight bound on the sensitivity of the OT plan and provides four theorems guaranteeing identifiability, sparsistency, well‑posedness, and convergence.

## Key Takeaways
- The core bound sigma_min ≥ (pi_min/(a_max ε))√λ_min(Σ) links the smallest singular value to the minimal probability π_min, the maximum cost a_max, and the regularization ε.  
- Theorem T2 shows that an ℓ1‑penalized estimator recovers the true support with exponential failure probability under irrepresentability and score concentration.  
- The inverse feature‑moment map is strongly monotone, giving a Lipschitz constant L ≤ ε‖ΦᵀSa‖_op/(π_min λ_min(Σ)), ensuring well‑posedness of the optimization.

## Context
Inverse optimal transport (IOT) problems are central to learning from distributionally shifted data and have driven recent advances in statistical estimation. The feature‑parameterized cost structure—Cθ(i,j)=−θᵀφ(i,j)—introduces a new layer of complexity that requires both theoretical guarantees and efficient algorithms, which this work addresses.

## Implications
For practitioners, the derived bounds enable precise control over estimator stability and computational cost in high‑dimensional settings. The unified theory can be directly applied to tasks such as domain adaptation and anomaly detection, where reliable transport maps are essential for performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13201v1)
