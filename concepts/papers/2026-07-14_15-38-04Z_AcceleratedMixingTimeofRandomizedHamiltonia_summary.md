---
title: "Summary: Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo"
date: "2026-07-14"
type: "paper-summary"
source_url: "http://arxiv.org/abs/2607.12902v1"
tags: ["summary", "paper-summary", "arxiv"]
authors: "Siddharth Mitra, Vishwak Srinivasan, Xiuyuan Wang, Andre Wibisono"
---
# Summary: Accelerated Mixing Time of Randomized Hamiltonian Monte Carlo

**Source**: [Original Paper](http://arxiv.org/abs/2607.12902v1)

## Summary

We show the Randomized Hamiltonian Monte Carlo (RHMC) algorithm has accelerated mixing time guarantees for sampling from log-concave probability distributions. RHMC proceeds by repeatedly simulating the continuous-time Hamiltonian dynamics for some random integration times, and resetting the velocity to be an independent Gaussian random variable between each simulation. We show that when the target distribution is log-concave and satisfies an $α$-Talagrand inequality (for example, if the target distribution is $α$-strongly log-concave), if we use a random integration time from either the triangular or the exponential distribution with mean $Θ(α^{-1/2})$, then RHMC converges exponentially fast in KL divergence, and the total integration time to reach error $\varepsilon$ in KL divergence scales as $O(α^{-1/2} \log(\varepsilon^{-1}))$. We also show that when the target distribution is log-concave, if we use a sequence of random integration times from the triangular distribution with exponentially increasing means, then the total integration time to reach error $\varepsilon$ in KL divergence scales as $O(\varepsilon^{-1/2})$. Our analysis relies on a bound on the average KL divergence along Hamiltonian dynamics, which is inspired by an analogous result on accelerated optimization methods based on Hamiltonian dynamics.

## Related Concepts

- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
- [[concepts/data-curation/data-curation-hub.md|Data Curation Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
