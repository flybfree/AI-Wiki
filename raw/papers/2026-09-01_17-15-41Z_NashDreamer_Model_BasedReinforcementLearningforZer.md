---
title: NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games
published: 2026-09-01T17:15:41Z
authors: Tomáš Holeček, Viliam Lisý
url: http://arxiv.org/abs/2609.01549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games

## Abstract
Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning faces severe identifiability barriers, which we argue make centralized model learning a mathematical necessity. Building on this analysis, we propose NashDreamer, a principled MBRL framework for two-player zero-sum IIGs. It introduces a centralized Multi-Agent Recurrent State-Space Model (MARSSM) that decouples environment dynamics from the effect of players' strategies on their individual observations. NashDreamer is designed to use arbitrary policy gradient algorithms and inherits their convergence guarantees towards Nash equilibria under an idealized model. Empirical evaluations across four benchmark games demonstrate that NashDreamer substantially improves sample efficiency over model-free baselines early in the training. Finally, we theoretically analyze the architecture's optimization landscape, identifying the vulnerability of the Dreamer family of algorithms to posterior collapse in stochastic environments. We leave it as an open challenge.

## Metadata
- **Published**: 2026-09-01T17:15:41Z
- **Authors**: Tomáš Holeček, Viliam Lisý
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01549v1)