---
title: Stable and Budget-Feasible Coalition Formation for Clustered Federated Learning: A Hedonic Potential-Game Approach
url: http://arxiv.org/abs/2607.26788v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_11-29-45Z_StableandBudget_FeasibleCoalitionFormationforClust.md
generated_at: 2026-07-29 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a transferable‑surplus model that separates learning benefit, system cost, participant cost, and monetary transfers in clustered federated learning. By converting coalition surplus into hedonic preferences it shows that symmetric pairwise allocations form an exact potential game with Nash‑stable partitions and exponential budget feasibility under submodular retained slack.

## Key Takeaways
- A potential‑game framework guarantees a Nash‑stable partition of participants into coalitions where each pair’s allocation is individually optimal.  
- Feasibility of bounded pair incentives can be checked in polynomial oracle time when the retained coordinator surplus is submodular, preventing unbounded welfare loss.  
- The additive price‑of‑stability guarantee is asymptotically tight, while exact balance yields welfare‑optimal stability only for pairwise‑representable instances.

## Context
Clustered federated learning aims to let diverse data sources collaborate without sharing raw data, but sustainable coalition formation remains an open challenge. This work bridges game theory and algorithmic fairness by formalizing how surplus translates into participant preferences, offering a principled basis for scalable model training.

## Implications
For practitioners, the method provides a reliable way to allocate limited transfer budgets while preserving model quality, reducing reliance on gradient alignment. It also offers theoretical guarantees that can be leveraged in real‑world federated deployments where welfare loss must be bounded and stable over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26788v1)
