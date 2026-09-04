---
title: EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments
published: 2026-09-03T13:40:07Z
authors: Zih-Sian Yang, Yi-Hao Chen, Yu-Te Kuan, Cheng-Jui Wu, Chuang-Chieh Lin, Po-An Chen
url: http://arxiv.org/abs/2609.03846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments

## Abstract
We study the allocation of indivisible goods among agents with identical additive valuations, focusing on envy-freeness up to one good (EF1) and Nash social welfare (NSW). Since every maximum-NSW allocation is EF1 under additive valuations, the associated threshold problem inherits the known strong NP-hardness of NSW maximization under identical additive valuations and is strongly NP-complete. We therefore focus on welfare guarantees satisfied by arbitrary EF1 allocations. Although every such allocation is known to achieve an $e^{-1/e}$-approximation to the unrestricted optimal NSW, we identify conditions yielding stronger guarantees. Under uniform valuations, every EF1 allocation is NSW-optimal. Under an $\varepsilon$-small-item condition, every EF1 allocation achieves an explicit approximation ratio $ρ_n(\varepsilon)$ satisfying $ρ_n(\varepsilon) = 1-O(\varepsilon^2)$ as $\varepsilon\to 0$ for fixed $n$.   We further consider the stronger sequential requirement that EF1 be maintained after every item assignment. For this setting, we propose \emph{PriorityNet}, a deep reinforcement learning framework trained using Proximal Policy Optimization and equipped with prospective EF1 action masking. The mask restricts every decision to assignments that preserve EF1, thereby guaranteeing prefix-wise EF1 by construction without post-processing repair. Across 3,000 test instances in each of the offline and random-order online regimes ($n\in[2,20]$ and $m\in[5,100]$), PriorityNet attains mean normalized $\operatorname{NSW}$ values of $0.9911$ and $0.9701$, respectively. Relative to offline Longest Processing Time (LPT) and online least-valued-bundle baselines, it achieves instance-wise win-minus-loss rates of $+27.10\%$ and $+17.87\%$, while matching the offline baseline's mean normalized welfare to four decimal places and modestly improving the online mean from $0.9694$ to $0.9701$.

## Metadata
- **Published**: 2026-09-03T13:40:07Z
- **Authors**: Zih-Sian Yang, Yi-Hao Chen, Yu-Te Kuan, Cheng-Jui Wu, Chuang-Chieh Lin, Po-An Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03846v1)