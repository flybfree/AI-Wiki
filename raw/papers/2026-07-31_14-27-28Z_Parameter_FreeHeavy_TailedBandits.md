---
title: Parameter-Free Heavy-Tailed Bandits
published: 2026-07-31T14:27:28Z
authors: Gianmarco Genalti, Alberto Maria Metelli
url: http://arxiv.org/abs/2607.29460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Parameter-Free Heavy-Tailed Bandits

## Abstract
Heavy-tailed distributions arise naturally in sequential decision-making problems such as financial investment, online advertising, and network management, where rare but extreme outcomes can dominate performance. Heavy-tailed bandits model online decision-making in these settings by assuming only that rewards $X$ satisfy $\mathbb{E}[|X|^{1+ε}]\leq u$, for some tail exponent $ε\in(0,1]$ and moment bound $u<+\infty$. However, most existing regret minimization algorithms require these parameters to be known. This assumption is particularly restrictive in practice: $ε$ and $u$ govern the frequency and magnitude of rare events and are therefore precisely the quantities that are hardest to infer reliably from limited observations.   Motivated by an open problem posed by Genalti and Metelli at COLT 2025, we resolve the assumption-free adaptation problem for heavy-tailed bandits and characterize the price in the regret of not knowing the tail parameters. We first study adaptation to the moment bound $u$ for a fixed tail exponent $ε$. We prove that every algorithm unaware of $u$, or of any upper bound on it, must obey a sharp trade-off between its distribution-dependent and distribution-free regret guarantees. We then introduce a scheduled-exploration algorithm that requires no knowledge of $u$ and matches the resulting adaptation frontier up to logarithmic factors. Finally, we show that the same algorithm can be instanced without knowing $ε$ by calibrating its exploration schedule to the endpoint $ε=1$. It achieves sublinear regret for every fixed $ε>0$, while no algorithm can guarantee sublinear regret uniformly over all $ε\in(0,1]$. Altogether, our results resolve the COLT open problem without additional distributional assumptions and provide a sharp characterization of the statistical cost of adapting to unknown heavy tails.

## Metadata
- **Published**: 2026-07-31T14:27:28Z
- **Authors**: Gianmarco Genalti, Alberto Maria Metelli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29460v1)