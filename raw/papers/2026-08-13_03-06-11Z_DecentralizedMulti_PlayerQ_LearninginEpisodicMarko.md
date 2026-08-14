---
title: Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry
published: 2026-08-13T03:06:11Z
authors: Larissa Xu, King Bi, William Chang
url: http://arxiv.org/abs/2608.12753v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry

## Abstract
We study decentralized multi-player reinforcement learning in episodic tabular Markov decision processes (MDPs) under three forms of information asymmetry: (A) unobserved actions with common rewards, (B) observed actions with independent rewards, and (C) unobserved actions with independent rewards. Players cannot communicate during learning but may agree on a protocol a priori. For Problems A and B we propose \texttt{mQ-learning} and \texttt{mQ-learning-intervals}, achieving $\tilde{O}(\sqrt{H^4 S A_{\text{joint}}\, T})$ regret, where $H$ is the horizon, $S$ the state count, $T = KH$ the total steps, and $A_{\text{joint}} = \prod_{i=1}^M |\mathcal{A}_i|$ the joint action space across $M$ players. For Problem C we give \texttt{mEXC} and \texttt{mEXC-Bellman}, two-phase explore-then-commit algorithms with regret $\tilde{O}(H (S A_{\text{joint}})^{1/3} T^{2/3})$. Against the centralized joint-action benchmark, decentralized learning under information asymmetry matches the single-agent Q-learning rate of \cite{jin2018q} up to logarithmic factors. Because $A_{\text{joint}}$ grows exponentially in $M$, the bounds are most meaningful for small $M$ or small per-player action sets.

## Metadata
- **Published**: 2026-08-13T03:06:11Z
- **Authors**: Larissa Xu, King Bi, William Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12753v1)