---
title: Beyond Peak Backlog: Conditional Energy and Temporal Geometry in Capacity-Constrained Delayed Bandit Optimization
published: 2026-08-17T07:49:51Z
authors: Anling Xiang, Yuwen Yang, Yang Shen
url: http://arxiv.org/abs/2608.16216v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Peak Backlog: Conditional Energy and Temporal Geometry in Capacity-Constrained Delayed Bandit Optimization

## Abstract
What is the right delay complexity when a learner can track only $C$ pending feedback items and discarded feedback is permanently lost? Existing one-point bandit convex optimization guarantees in this model pay $\sqrt{Tσ_{\max}}$, where $σ_{\max}$ is the peak backlog, although unlimited tracking admits the sharper $\sqrt{d_{\mathrm{tot}}}$ dependence on total delay. We introduce a scheduler-side conditional-energy interface that separates rate adaptation from the one-point perturbation filtration and handles the dependent importance weights created by randomized admission. Under the same semi-clairvoyant oracle and pathwise hard-capacity contract, this yields an untuned learner whose delay term scales as $O(\sqrt{E_C d_{\mathrm{tot}}})$, with only an explicit restart factor $E_C$; a public constant-factor peak bound removes this factor while $d_{\mathrm{tot}}$ remains unknown. Under strong convexity, the same interface yields the temporal cost $H_A(d)=\sum_t σ_t/(A+t)$. Two delay vectors with identical delay multisets, $d_{\mathrm{tot}}$, $σ_{\max}$, and capacity can nevertheless have polynomially different minimax regret, showing that timing matters under curvature even when aggregate delay summaries agree. Finally, a continuous hard family converts tracking capacity into a zeroth-order query budget and gives a complementary capacity-starvation lower endpoint. The upper bounds require $C\ge \ln T+1$ and do not constitute a complete capacity minimax characterization.

## Metadata
- **Published**: 2026-08-17T07:49:51Z
- **Authors**: Anling Xiang, Yuwen Yang, Yang Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16216v1)