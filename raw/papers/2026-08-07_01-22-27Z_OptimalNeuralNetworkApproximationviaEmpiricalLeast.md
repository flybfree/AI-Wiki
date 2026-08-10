---
title: Optimal Neural Network Approximation via Empirical Least Squares with Deterministic Samples
published: 2026-08-07T01:22:27Z
authors: Xinliang Liu, Tong Mao, Jinchao Xu
url: http://arxiv.org/abs/2608.06687v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Neural Network Approximation via Empirical Least Squares with Deterministic Samples

## Abstract
We develop a rigorous theory of discrete residual least-squares approximation for elliptic spectral equations $\mathfrak L_βu=f$ using linearized ReLU$^k$ neural networks on the sphere, where $\mathfrak L_β$ is a positive elliptic spectral multiplier of order $β$. Given a parameter set $Θ_n=\{θ_{j}^*\}_{j=1}^n\subset\mathbb S^d$, we approximate $u$ in the linearized network space $L_n^k(Θ_n)$ by the discrete residual on the collocation points $\{η_i^*\}_{i=1}^m$ \begin{equation*} u_{n,m}\in\arg\min_{v_n\in L_n^k(Θ_n)}\frac1m\sum_{i=1}^m\left(f(η_i^*)-\mathfrak L_βv_n(η_i^*)\right)^2. \end{equation*} With $k>\frac{d-1}{2}+β$, for antipodally quasi-uniform network parameter sets and any quasi-uniform collocation points with $m\gtrsim n$, we prove that \begin{equation*} \|u-u_{n,m}\|_{\mathcal H^β(\mathbb S^d)}\eqsim\|f-\mathfrak L_βu_{n,m}\|_{\mathcal L^2(\mathbb S^d)}\lesssim n^{-\frac{r}{d}} \begin{cases} \|f\|_{\mathcal W^{r,p}(\mathbb S^d)},&\frac{d}{p}<r\leq \frac{d}{2},~p>2,\\ \|f\|_{\mathcal H^r(\mathbb S^d)},&r>\frac{d}{2}. \end{cases} \end{equation*} We also establish a high-probability residual estimate, up to a logarithmic factor and an arbitrarily small smoothness loss, for i.i.d.\ uniformly distributed collocation points.   The key analytical ingredient is a Bernstein inequality for linearized ReLU$^k$ network spaces. If $\underline h$ denotes the antipodal separation distance of the network parameters, then \begin{equation*} \|v_n\|_{\mathcal H^r(\mathbb S^d)}\lesssim\underline h^{-(r-s)}\|v_n\|_{\mathcal H^s(\mathbb S^d)},\qquad 0\leq s<r<k+\tfrac12. \end{equation*}

## Metadata
- **Published**: 2026-08-07T01:22:27Z
- **Authors**: Xinliang Liu, Tong Mao, Jinchao Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06687v1)