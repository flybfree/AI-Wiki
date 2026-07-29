---
title: Variance-Reduced Conditional Gradient Methods under Markovian Sampling for Nonconvex Composite Optimization
published: 2026-07-28T14:37:47Z
authors: Zhaojun Peng
url: http://arxiv.org/abs/2607.25785v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Variance-Reduced Conditional Gradient Methods under Markovian Sampling for Nonconvex Composite Optimization

## Abstract
We study stochastic composite nonconvex optimization over a compact convex set when gradient samples arrive along a single trajectory of a fixed ergodic Markov chain. Existing single-trajectory variance-reduction theory covers smooth unconstrained objectives; we address the projection-free composite setting using the generalized Frank-Wolfe gap. We propose MC-ALFCG, which combines a momentum conditional-gradient method with coupled capped multilevel Monte Carlo estimation and per-iteration clipping. The deepest nested average uses consecutive states from the same trajectory, yielding conditional bias $O(τ_{\mathrm{mix}}/T)$ uniformly over the starting state, while coupling controls the gradient-difference second moment through the iterate displacement. Clipping enforces the pathwise bounds needed by the adaptive analysis. We reduce the Markovian recursion to its independent-sampling counterpart under $σ^2\mapsto 2ΛG_σ^2$ and $L^2\mapsto 2ΛL^2$, where $Λ=O(τ_{\mathrm{mix}}\log T)$. For positive centered noise, the tuned method achieves expected sample complexity $\widetilde{O}((τ_{\mathrm{mix}}^2G_σ+τ_{\mathrm{mix}}^{5/2}G_σ^2)\varepsilon^{-3}+τ_{\mathrm{mix}}^5\varepsilon^{-2})$. The exactly noiseless specialization achieves $\widetilde{O}(\varepsilon^{-2})$ with mixing-time-free constants, while a mixing-time-oblivious variant achieves $\widetilde{O}(τ_{\mathrm{mix}}^6\varepsilon^{-3}+τ_{\mathrm{mix}}^3\varepsilon^{-2})$. All guarantees are in expectation under a fixed transition kernel. Controlled numerical studies examine dependence sensitivity, a nonconvex composite instance, and clipping behavior.

## Metadata
- **Published**: 2026-07-28T14:37:47Z
- **Authors**: Zhaojun Peng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25785v1)