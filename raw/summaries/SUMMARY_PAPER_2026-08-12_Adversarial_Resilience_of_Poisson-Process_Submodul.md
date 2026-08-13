---
title: Adversarial Resilience of Poisson-Process Submodular Maximization over Matroids: From Robust Offline Optimization to Full-Bandit Learning
url: http://arxiv.org/abs/2608.12134v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_14-54-15Z_AdversarialResilienceofPoisson_ProcessSubmodularMa.md
generated_at: 2026-08-12 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the robustness of Poisson‑process submodular maximization under a general matroid constraint when an arbitrary controlled value oracle is available. The authors prove that the Spiteful Greedy Swap Poisson Process (SGS‑Poisson) algorithm maintains its promised approximation guarantees even in the presence of adversarial noise, delivering exact limiting regret factors for both monotone and non‑monotone objectives.

## Key Takeaways
- The SGS‑Poisson algorithm retains a 1/e approximation factor for non‑monotone submodular objectives under any oracle perturbation bounded by ξ, with expected value at least (1/e−ε)OPT − O(kξ).  
- For monotone objectives the guarantee is 1−1/e, yielding an expected value of at least (1−1/e−ε)OPT − O(kξ), using only Θ(nk²ε⁻²) oracle calls.  
- These results enable a full‑bandit CMAB reduction that achieves exact limiting approximation regrets and regret scaling of Θ(n^{1/5}k^{4/5}T^{4/5}) for general matroid‑constrained submodular rewards.

## Context
The work addresses a longstanding challenge in online combinatorial optimization: preserving offline algorithmic guarantees when faced with adversarial oracle noise. By showing resilience without altering core mechanisms, the study bridges offline and online learning paradigms within constrained submodular settings.

## Implications
For practitioners, this means that existing Poisson‑process based solvers can be safely deployed in real‑time bandit scenarios where data may be noisy or limited, ensuring predictable performance. The theoretical robustness also encourages broader adoption of these algorithms across industries requiring combinatorial optimization under uncertainty.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12134v1)
