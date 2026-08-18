---
title: Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage
published: 2026-08-16T18:47:57Z
authors: Eric A. F. Reinhardt, Adam J. Hauser
url: http://arxiv.org/abs/2608.15889v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage

## Abstract
Currency arbitrage (CA) involves trading currencies in cycles to exploit discrepancies in market valuations. Quadratic unconstrained binary optimization (QUBO) involves minimizing a quadratic cost (energy) function of binary variables. Previous works have explored the use of QUBO to solve CA problems. We build on these previous works by introducing realistic constraints such as beginning cycles from a held currency and accounting for per-transaction trading fees. We show that this formulation requires fewer logical variables (qubits) than previous QUBO encodings in the literature. We derive provably sufficient penalty weights for its constraint terms. We also introduce an exact anchor-gauge reweighting of the exchange rates that compresses the QUBO coefficient range from the rate scale to the arbitrage scale, addressing the finite analog precision of annealing hardware. We demonstrate the efficacy of this formulation using classical simulated annealing against an exact Held-Karp baseline on the same CPU and show that it can effectively find profitable cycles and account for trading fees. Finally, we benchmark faithful implementations of five prior QUBO encodings at matched sampler budgets and show that the proposed encoding is the only one to recover the exact fee-adjusted optimum.

## Metadata
- **Published**: 2026-08-16T18:47:57Z
- **Authors**: Eric A. F. Reinhardt, Adam J. Hauser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15889v1)