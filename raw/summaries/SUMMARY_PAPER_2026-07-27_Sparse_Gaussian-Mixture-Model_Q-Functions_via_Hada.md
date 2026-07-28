---
title: Sparse Gaussian-Mixture-Model Q-Functions via Hadamard Overparametrization for Online Reinforcement Learning
url: http://arxiv.org/abs/2607.23474v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_05-58-23Z_SparseGaussian_Mixture_ModelQ_FunctionsviaHadamard.md
generated_at: 2026-07-27 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Sparse Gaussian‑Mixture‑Model Q‑Functions (S‑GMM‑QFs) as an online off‑policy policy iteration method for reinforcement learning that leverages Hadamard overparametrization to achieve sparse, interpretable models. The framework reconciles streaming data with the Riemannian geometry of parameter space and uses experience replay to address distributional mismatch. Numerical experiments show S‑GMM‑QFs match or surpass deep RL methods while using far fewer parameters.

## Key Takeaways
- Hadamard overparametrization creates a smooth regularization that naturally sparsifies the model, allowing the algorithm to automatically select only those components whose means and covariances capture meaningful geometric roles in the state‑action space.  
- The optimization proceeds on a Cartesian‑product Riemannian manifold via online gradient descent, which preserves the Riemannian structure and yields efficient updates despite non‑stationary streaming data.  
- Experience replay is employed to handle distributional mismatch between observed transitions and the target Q‑function distribution, ensuring stable learning across episodes.

## Context
The integration of geometric priors into reinforcement learning offers a path toward models that are both compact and interpretable, addressing longstanding challenges of deep RL’s opaque parameter growth. By combining Riemannian optimization with overparametrized Gaussian mixtures, S‑GMM‑QFs provide a principled alternative to black‑box function approximators.

## Implications
For practitioners, the method promises faster convergence per transition and lower memory footprint, making it suitable for real‑time deployment where resources are limited. The interpretability of component parameters could also inform domain‑specific policy design, bridging theory with practical engineering in robotics and autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23474v1)
