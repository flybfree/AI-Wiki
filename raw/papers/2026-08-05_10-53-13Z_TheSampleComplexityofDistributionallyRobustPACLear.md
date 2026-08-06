---
title: The Sample Complexity of Distributionally Robust PAC Learning under Cressie--Read Divergences
published: 2026-08-05T10:53:13Z
authors: Elad Aigner-Horev, Daniel Rosenberg, Roi Weiss
url: http://arxiv.org/abs/2608.04686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Sample Complexity of Distributionally Robust PAC Learning under Cressie--Read Divergences

## Abstract
We study distributionally robust PAC learning for the $0$--$1$-loss, where adversarial perturbations of the data distribution are constrained by a Cressie--Read divergence of order $k>1$ and radius $ρ\geq 0$. For hypothesis classes with VC dimension $d$, we establish realizable and agnostic sample-complexity bounds tight up to constant and logarithmic factors, respectively; ordinary empirical risk minimization attains both rates up to logarithmic factors. For target accuracy $\varepsilon\in(0,1)$ and confidence $δ\in(0,1)$, their respective orders are \[ \max\!\left\{\frac{1}{\varepsilon}, \frac{ρ^{\frac 1{k-1}}}{\varepsilon^{k_\star}} \right\}\cdot(d+\log δ^{-1}) \qquad\text{and}\qquad \max\!\left\{\frac{1}{\varepsilon^2}, \frac{ρ^{\frac1{k-1}}}{\varepsilon^{k_\star\vee 2}} \right\}\cdot(d+\log δ^{-1}), \] where $k_\star={k}/{(k-1)}$. For every fixed $ρ>0$, robustness changes the realizable $\varepsilon$-dependence from $\varepsilon^{-1}$ to $\varepsilon^{-k_\star}$ as $\varepsilon\downarrow0$. In the agnostic case, for $1<k<2$, robustness changes the $\varepsilon$-dependence from $\varepsilon^{-2}$ to $\varepsilon^{-k_\star}$, whereas for $k\geq2$ the exponent remains the classical $2$, with nontrivial $ρ$-dependence.   Building on the known scalar reduction of robust $0$--$1$ risk to ordinary classification error, our analysis reveals a scale-sensitive interaction between the statistical estimation of classification error and its amplification by robustness, sharply explaining the transition in the agnostic rate. We extend the previously studied $χ^2$-divergence case to every Cressie--Read order $k>1$, close its upper--lower gaps, and recover standard PAC learning rates as $ρ\to0$, unlike previous bounds that fail to interpolate correctly in this limit.

## Metadata
- **Published**: 2026-08-05T10:53:13Z
- **Authors**: Elad Aigner-Horev, Daniel Rosenberg, Roi Weiss
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04686v1)