---
title: Optimal Learning Under Tsybakov Noise
published: 2026-08-09T02:20:51Z
authors: Steve Hanneke, Hongao Wang, Mingyue Xu
url: http://arxiv.org/abs/2608.08416v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Learning Under Tsybakov Noise

## Abstract
Probably Approximately Correct (PAC) learning [Val84] is a fundamental learning model that has been extensively investigated. In this model, $\mathcal{H} \subseteq \{0,1\}^{\mathcal{X}}$ is a concept class, and $h^*\in\mathcal{H}$ is the target concept to be learned. Having access to i.i.d. labeled examples from a distribution $\mathcal{D}$ over $\mathcal{X}\times\{0,1\}$, which admits $h^*$ as the best concept in $\mathcal{H}$, the goal is to design a learning algorithm that outputs a hypothesis having low error competitive to $h^{*}$ with high probability.   This model was initially studied under the realizable setting, which assumes that $h^*$ has no error. A natural relaxation is to allow label noise, that is, the true label can be flipped with probability $η\in(0,1/2)$. In reality, certain labels might be extremely noisy, especially for those points near the decision boundary. Hence, it is natural to allow very noisy points, though only rarely. This is quantified by a noise model introduced by [MT99] and [Tsy04], now known as Tsybakov noise. For learning general concept classes, [MN06] gave the general upper and lower bounds for error guarantees under Tsybakov noise. However, their upper and lower bounds differ by a logarithmic factor. Resolving this gap has remained a well-known open question for the past twenty years.   In this work, we resolve this open question by improving the upper bound to match the best known lower bound, thus establishing the optimal error guarantee for learning under Tsybakov noise. Our learning algorithm operates by adaptively partitioning the instance space into regions, roughly corresponding to different noise levels, and returning a hypothesis in the concept class satisfying a specific error constraint for each region. Our technique shares a conceptual foundation with several recent advances in non-realizable learning, such as [HLZ24] and [Han25].

## Metadata
- **Published**: 2026-08-09T02:20:51Z
- **Authors**: Steve Hanneke, Hongao Wang, Mingyue Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08416v1)