---

title: Accelerated Decentralized Stochastic Gradient Descent for Strongly Convex Optimization
published: "2026-06-05T17:51:11Z"
authors: Ming Sun, Kun Yuan
url: http://arxiv.org/abs/2606.07496v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Accelerated Decentralized Stochastic Gradient Descent for Strongly Convex Optimization



**Source**: [Original Paper](http://arxiv.org/abs/2606.07496v1)
## Abstract
Decentralized stochastic optimization is a fundamental paradigm for large-scale learning over networks, where agents communicate only with their neighbors and no central coordinator is required. For strongly convex problems, communication efficiency is mainly determined by the condition number \(κ=L/μ\) and the network spectral gap \(1-β\). Although deterministic decentralized methods can simultaneously achieve accelerated \(\sqrtκ\) and \(1/\sqrt{1-β}\) dependences, no existing stochastic method attains both improvements at once. In this paper, we propose \emph{Multi-Gossip Accelerated DSGD} (MG-ADSGD), a decentralized stochastic algorithm that combines Nesterov-type primal--dual extrapolation with multi-round fast gossip averaging. The key idea is to couple the gossip depth with the mini-batch size so that additional communication rounds simultaneously improve consensus accuracy and reduce gradient variance. We show that MG-ADSGD achieves the communication complexity \[ \widetilde{\mathcal O}\!\left( \frac{σ^2}{μnε}\log\frac{1}ε + \sqrt{\fracκ{1-β}}\log\frac{1}ε \right), \] where \(ε\) denotes the target accuracy, \(n\) is the number of nodes, and \(σ^2\) is the gradient variance. To the best of our knowledge, this bound yields the best currently available communication complexity for decentralized stochastic strongly convex optimization, up to logarithmic factors that are independent of $ε$.

## Metadata
- **Published**: 2026-06-05T17:51:11Z
- **Authors**: Ming Sun, Kun Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.07496v1)