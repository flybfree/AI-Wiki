---
title: Fast Rates for Swap-Agnostic Learning of Proper Losses
published: 2026-07-30T21:41:40Z
authors: Princewill Okoroafor
url: http://arxiv.org/abs/2607.28856v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast Rates for Swap-Agnostic Learning of Proper Losses

## Abstract
Swap-agnostic learning strengthens classical agnostic learning by allowing the comparator to select a different hypothesis on each level set of the learner's predictions. This benchmark captures prediction-dependent postprocessing, but appears to require solving a separate agnostic-learning problem for every possible prediction value. We show that, for proper losses, these prediction-level comparisons can instead be controlled jointly. Our main result is an offline swap-agnostic learner for any fixed proper loss. For a finite hypothesis class $H$ and any fixed smooth proper loss, the excess risk from $m$ i.i.d. samples is $\widetilde{O}((\log |H|/m)^{2/3})$, with a corresponding online swap-regret bound of $\widetilde{O}(T^{1/3}(\log |H|)^{2/3})$. We also give algorithms whose predictions are simultaneously swap-agnostic for entire families of losses. For all proper losses bounded in $[-1,1]$, we obtain online and offline rates of $\widetilde{O}(\sqrt{T\log |H|})$ and $\widetilde{O}(\sqrt{\log |H|/m})$, respectively. For convex, $1$-Lipschitz proper losses, these rates improve to $\widetilde{O}(T^{1/3}(\log |H|)^{2/3})$ online and $\widetilde{O}((\log |H|/m)^{2/3})$ offline. These bounds are tight up to logarithmic factors and improve upon the $\widetilde{O}(T^{2/3}(\log |H|)^{1/3})$ rate implied by the swap-omniprediction guarantee of Luo et al. (2025). Our main technical contribution is a reduction from swap-agnostic learning to a second-order form of multicalibration, obtained via Blackwell approachability with a Bernstein-style variance correction.

## Metadata
- **Published**: 2026-07-30T21:41:40Z
- **Authors**: Princewill Okoroafor
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28856v1)