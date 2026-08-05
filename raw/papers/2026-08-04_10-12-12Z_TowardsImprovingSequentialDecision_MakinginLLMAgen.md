---
title: Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory
published: 2026-08-04T10:12:12Z
authors: Jakub Rada, Viliam Lisý
url: http://arxiv.org/abs/2608.03420v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory

## Abstract
Large language models have improved substantially on single-shot reasoning tasks, but their performance in sequential decision-making is less well understood. We study this on fully-observable two-player zero-sum games, which provide ground-truth evaluation: outcomes are determined by the rules, and optimality of individual moves can be computed or approximated, without relying on a judge model. Across model tiers, LLMs play suboptimally in simple games such as tic-tac-toe or Connect Four, and lose to MCTS opponents. Obfuscations that preserve the game tree but rewrite its surface form leave performance largely unchanged, indicating the gap is not fully explained by recall of memorized strategies. Motivated by this performance gap, we introduce an agentic framework enhanced with an experience memory designed for the sequential setting and addressing common challenges of sequential decision-making such as credit assignment. We show that post-game reflection and rule extraction yield measurable improvements on tic-tac-toe without modifying the model weights.

## Metadata
- **Published**: 2026-08-04T10:12:12Z
- **Authors**: Jakub Rada, Viliam Lisý
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03420v1)