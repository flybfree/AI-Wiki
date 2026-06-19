---

title: 'DNQ: Deep Nash Q-Network for Partially Observable n-Player Games'
published: "2026-06-04T17:58:01Z"
authors: Qintong Xie, Edward Koh, Xavier Cadet, Peter Chin
url: http://arxiv.org/abs/2606.06480v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# DNQ: Deep Nash Q-Network for Partially Observable n-Player Games



**Source**: [Original Paper](http://arxiv.org/abs/2606.06480v1)
## Abstract
Many real-world competitive systems require multiple decision-makers to act simultaneously under shared constraints, limited information, and repeated interaction, as in auctions, resource allocation, and security competition. We study multi-turn simultaneous bidding as a controlled testbed for such problems and propose DNQ, a solver-in-the-loop equilibrium supervision framework for training bidding agents. DNQ alternates between trajectory collection, critic-based payoff estimation, equilibrium computation, and policy imitation. At each visited state, a shared critic predicts either pairwise payoff matrices or an exact N-player payoff tensor, an external solver computes equilibrium strategies, and the agents are trained by minimizing the KL divergence between their masked policies and the solver-derived equilibrium targets. We focus on a scalable pairwise formulation that greatly reduces equilibrium-solving cost and training time compared with the exact formulation, while the shared critic amortizes payoff learning across agents and states. Experiments compare the pairwise and exact variants using critic loss, policy entropy, bidding resource usage, and training cost, showing that the pairwise method scales to larger numbers of agents, whereas the exact method becomes computationally impractical as the joint game grows. These results illustrate the trade-off between strategic fidelity and scalability in repeated competitive environments.

## Metadata
- **Published**: 2026-06-04T17:58:01Z
- **Authors**: Qintong Xie, Edward Koh, Xavier Cadet, Peter Chin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.06480v1)