---
title: Dec-BFTRL: Squre-Root Regret for Decentralized Online Upper-Linearizable Optimization under Separation Access with Application to Continuous Submodular Maximization
url: http://arxiv.org/abs/2608.30271v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_05-29-54Z_Dec_BFTRL_Squre_RootRegretforDecentralizedOnlineUp.md
generated_at: 2026-08-31 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Dec-BFTRL, a decentralized algorithm for online optimization with upper‑linearizable payoffs that achieves square‑root regret under efficient separation access. The method is applied to continuous diminishing‑return submodular maximization, where each agent iteratively minimizes its BFTRL potential using local HybridNewton steps and communicates only a cumulative surrogate‑gradient dual state.

## Key Takeaways
- Each agent’s action is compared to the average of all local objectives, enabling a global regret bound that scales as $\widetilde O(\sqrt{T})$ over $T$ rounds.  
- The algorithm requires each agent to perform $T$ neighbor‑mixing steps and only $\widetilde O(T)$ calls to the separation oracle, keeping communication overhead linear in time.  
- Four wrapper instantiations are provided for three continuous DR‑submodular maximization problems, demonstrating practical applicability across diverse settings.

## Context
The work addresses a longstanding challenge in decentralized online learning: achieving sublinear regret while limiting communication and computation per agent. By leveraging BFTRL potentials and approximate gauge projections, the authors demonstrate that square‑root regret is attainable without sacrificing scalability for continuous submodular objectives.

## Implications
For practitioners, Dec-BFTRL offers a framework that balances low regret with manageable resource usage in real‑time optimization tasks such as network design or inventory management. The results suggest that square‑root regret can be realized even when agents only have access to local information and a limited communication channel, opening avenues for efficient large‑scale deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30271v1)
