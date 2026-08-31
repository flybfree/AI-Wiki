---
title: Beyond Search-Imitation: Prior-Directed Exploration for Searchless Chess
published: 2026-08-27T22:42:08Z
authors: Szymon Miłosz, Piotr Duch, Szymon Grabowski
url: http://arxiv.org/abs/2608.27757v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Search-Imitation: Prior-Directed Exploration for Searchless Chess

## Abstract
Searchless chess networks reach human master strength from a single forward pass by imitating a stronger teacher: the strongest, Leela Chess Zero's (Lc0) released Chessformer, distills the visit counts of an AlphaZero-style Monte Carlo Tree Search (MCTS). Imitating a search is a poor proxy for playing without one, so we fine-tune for single-pass strength with self-play reinforcement learning (RL). Its exploration is usually supplied by an entropy bonus, the reverse Kullback-Leibler (KL) divergence to uniform. We replace it with a forward, mass-covering KL toward the network's own MCTS prior (prior-directed exploration), so exploration covers the moves the prior judges promising, and pair it with an entropy-adaptive sampling temperature, set by the value head's outcome uncertainty, that sharpens once a position is decided. In about two thousand steps it raises puzzle accuracy from 93.9% to 94.9% on a 100,000-puzzle suite and mate-in-four accuracy from 77% to 81% while holding searchless strength at or slightly above the base. Measuring tactical accuracy and playing strength together across a matched-compute sweep, we find the two dissociate: accuracy gains fall in a one-point band while ratings straddle the base, and a control fine-tuned on puzzles alone posts the study's largest tactical gains while shedding roughly 260 Elo; a better puzzle-solver is not thereby a stronger player. Distribution-level measurements show what anchoring buys: without a regularizer self-play collapses onto a single line of play, and the puzzles newly solved are the near misses whose winning move the prior kept alive. The forward-KL prior tops the rating ladder, statistically tied with a reverse-KL anchor that concentrates twice as hard and drops the hardest solutions the mass-covering prior keeps in support.

## Metadata
- **Published**: 2026-08-27T22:42:08Z
- **Authors**: Szymon Miłosz, Piotr Duch, Szymon Grabowski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27757v1)