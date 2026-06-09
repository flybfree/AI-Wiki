---
title: Regret Minimization with Adaptive Opponents in Repeated Games
published: 2026-06-04T17:59:08Z
authors: Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, Kaiqing Zhang
url: http://arxiv.org/abs/2606.06486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Regret Minimization with Adaptive Opponents in Repeated Games

## Abstract
In this paper, we study regret minimization in repeated games with \emph{adaptive} opponents who can respond based on histories of play. The standard metric of \emph{external regret} in online learning is known to fail to capture such adaptivity. To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the \emph{realized} and the \emph{best-in-hindsight} accumulated utility when all players can \emph{respond} to the history of play. Compared to existing regret notions in this setting, ours is native to repeated game playing, enabling stronger comparators and opponents with fewer constraints, while maintaining the possibility of finding better equilibria when all players minimize it. We first identify necessary conditions for obtaining {\tt RP-Regret} sublinear in time, on the variation of the player's comparator strategies in the regret definition and on the memories of both the comparator and opponents' strategies. We then study additional conditions and provable algorithms to minimize {\tt RP-Regret}, which is by definition \emph{non-convex} in the strategy space. To address this challenge, we propose three algorithms: (i) one based on an optimization oracle, as assumed in some prior work in online non-convex learning; (ii) one that minimizes a convex and \emph{linearized} surrogate of {\tt RP-Regret} at each iteration; (iii) one that directly minimizes {\tt RP-Regret} when opponents change strategies slowly. Furthermore, when all players can run algorithms to minimize the {\tt RP-Regret} (or its linearized variant), certain subgame perfect equilibria of the repeated game can be learned. We also provide experiments showing that minimizing our regret notions can lead to more cooperative solutions with higher utility in games such as Stag-Hunt.

## Metadata
- **Published**: 2026-06-04T17:59:08Z
- **Authors**: Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, Kaiqing Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.06486v1)