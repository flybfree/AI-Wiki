---
title: Concentrated Liquidity Provision: a Reinforcement Learning Perspective
published: 2026-08-19T19:08:39Z
authors: Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro Sánchez-Betancourt, Carmine Ventre
url: http://arxiv.org/abs/2608.19389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Concentrated Liquidity Provision: a Reinforcement Learning Perspective

## Abstract
Automated market makers (AMMs) are a cornerstone of decentralised finance (DeFi). Constant product markets with concentrated liquidity, such as UniswapV3, are now a well-established design. In these markets, liquidity providers (LPs) face a sequential decision problem: they must decide when to rebalance their positions and which price ranges to allocate capital to as market conditions evolve. We formulate dynamic liquidity provision as a stochastic impulse control problem and use reinforcement learning (RL) to solve it, focusing on providing interpretable solutions. We show that learned policies exhibit rich state-dependent behaviour, allocating liquidity according to mispricing, rebalancing costs, uncertainty, inventory exposure, and heterogeneous risk preferences. These behaviours help compress the left tail of the Profit and Loss (PnL) distribution and avoid catastrophic outcomes under high uncertainty. Finally, we benchmark the RL agents against baseline and sophisticated agents from the AMM microstructure literature and analyse their performance.

## Metadata
- **Published**: 2026-08-19T19:08:39Z
- **Authors**: Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro Sánchez-Betancourt, Carmine Ventre
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19389v1)