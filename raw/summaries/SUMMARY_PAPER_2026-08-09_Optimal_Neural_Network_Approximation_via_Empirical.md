---
title: Optimal Neural Network Approximation via Empirical Least Squares with Deterministic Samples
url: http://arxiv.org/abs/2608.06687v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_01-22-27Z_OptimalNeuralNetworkApproximationviaEmpiricalLeast.md
generated_at: 2026-08-09 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper establishes a rigorous theory of discrete residual least‑squares approximation for elliptic spectral equations using linearized ReLU$^k$ neural networks on the sphere. It proves that, under antipodally quasi‑uniform parameter sets and quasi‑uniform collocation points, the approximation error decays as $n^{-r/d}$ with a bound involving the smoothness of the data.

## Key Takeaways
- The error norm $\|u-u_{n,m}\|_{\mathcal H^β(\mathbb S^d)}$ is equivalent to the residual norm $\|f-\mathfrak L_βu_{n,m}\|_{\mathcal L^2(\mathbb S^d)}$, up to constants, for $k>\frac{d-1}{2}+β$ and $m\gtrsim n$.  
- A high‑probability estimate holds for i.i.d. uniformly distributed collocation points, allowing a logarithmic factor and an arbitrarily small smoothness loss.  
- The key analytical tool is a Bernstein inequality that relates the $\mathcal H^r$ norm of network outputs to the parameter separation distance $\underline h$, giving $\|v_n\|_{\mathcal H^r}\lesssim\underline h^{-(r-s)}\|v_n\|_{\mathcal H^s}$.

## Context
Neural networks are increasingly used to approximate solutions of high‑dimensional PDEs, yet their error behavior is often unclear. This work provides precise quantitative guarantees for discrete residual least‑squares methods on the sphere, a setting relevant to many scientific and engineering applications.

## Implications
The results offer confidence that carefully designed network parameters and collocation points lead to stable approximations, which can guide practical implementation in AI‑driven simulation tools. Practitioners may leverage these bounds to reduce overfitting and improve computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06687v1)
