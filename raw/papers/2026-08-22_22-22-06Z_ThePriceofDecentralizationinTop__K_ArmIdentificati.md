---
title: The Price of Decentralization in Top-$K$ Arm Identification
published: 2026-08-22T22:22:06Z
authors: Larissa Xu, Jasmine Nguyen, William Chang
url: http://arxiv.org/abs/2608.22120v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Price of Decentralization in Top-$K$ Arm Identification

## Abstract
Cooperative teams often need to agree on the best few options rather than simply accumulate reward, and they must do so while each member sees only a fragment of the team's collective experience. We study this as top-$K$ joint-arm identification in multi-agent multi-armed bandits: at every round $M$ agents simultaneously choose individual actions that compose a joint arm, and the team must ultimately return the $K$ joint arms of highest mean reward. The difficulty is that an agent may not observe the actions of others, their rewards, or either. We treat three observability regimes---(A) shared rewards with hidden actions, (B) observed actions with private rewards, and (C) full asymmetry---and design communication-free elimination algorithms (UCB-Intervals) that reconstruct implicit coordination from whatever signal each regime leaves intact: a shared arm ordering in (A), observable deviations in (B), and enlarged confidence radii under (C). We give matching analyses in both the fixed-budget and fixed-confidence objectives, then fold all three regimes into a single meta-guarantee indexed by a multiplicity $c$ and a consensus factor $ρ$. Our central result is quantitative rather than merely algorithmic: change-of-measure lower bounds show that shared-reward identification is optimal up to one universal logarithmic factor, and that the entire statistical price of removing communication is a multiplicative $ρ^2$ in sample complexity---a fixed $4\times$ penalty under full asymmetry. The resulting stopping time scales as $O\!\left(\sum_{\mathbf{a}} \frac{\log(A^M/δ)}{Δ_{\mathbf{a}}^2}\right)$ and the fixed-budget error as $\exp(-Θ(T/H_1))$, with the dependence on the joint-action count $A^M$ shown to be unavoidable.

## Metadata
- **Published**: 2026-08-22T22:22:06Z
- **Authors**: Larissa Xu, Jasmine Nguyen, William Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22120v1)