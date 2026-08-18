---
title: CoupVisor: Strategy Optimization by Round and Challenge Decision Support
published: 2026-08-16T17:29:04Z
authors: Cris Huynh
url: http://arxiv.org/abs/2608.15868v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoupVisor: Strategy Optimization by Round and Challenge Decision Support

## Abstract
This paper presents CoupVisor, a decision-support system for the hidden-information card game Coup. It addresses two questions: what a player should do on each turn, and when a player should challenge an opponent's claim. The system is built around a single description of game events, which is shared across manual play, replay of recorded games, simulation, belief tracking, advisor recommendations, and learning-based policies. CoupVisor estimates the chance that a claim is truthful by combining how likely each role is with how many cards the claimant still holds, which corrects a case where the very first claim of a game was flagged as suspicious despite no evidence. We compare a rule-following advisor and several learned and heuristic players across many simulated games and different opponent styles. Our main finding is that the choice of reward, whether it rewards short-term gains or ultimately winning the game, decides which learning approach performs best, and that a win-oriented reward produces a policy that outperforms all baselines.

## Metadata
- **Published**: 2026-08-16T17:29:04Z
- **Authors**: Cris Huynh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15868v1)