---
title: CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts
published: 2026-10-18T15:57:03Z
authors: Ilia Badanin
url: http://arxiv.org/abs/2610.25356v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts

## Abstract
We present CHSM8, a 210M-parameter chess transformer that plays moves conditioned on a free-text description of a playing style, e.g. "go for the Sicilian Defense", "solid, safe, risk-free chess" or "You are Magnus Carlsen in his prime". The model is pretrained without search on 1.07B filtered Lichess games, using a factorized move representation and legal-move masking. It reaches 1837 Elo against a strength-limited Stockfish and, in 1,000-game matches, beat every other public model we tested that was likewise trained without preference tuning, rewards or search, including one with 13 times as many parameters. We then fine-tune it to follow text on a synthetic dataset: Gemma-4-31B describes the playing style of 3M game sides, a 1B Gemma-3 model distilled from the 2.4M of those descriptions that contradict nothing on the board labels the rest, and every one of 30M selected game sides gets five descriptions. Supervised fine-tuning attaches a frozen text encoder through gated cross-attention, and direct preference optimization (DPO) uses the same moves under a mismatched description as the rejected sample. After DPO, style adherence rises on every prompt we test (for example, queens traded early 53% -> 67%, pawn moves 29% -> 32% of all moves, queenside castling 97.3% -> 99.7%), and strength without a prompt stays within noise of SFT (1792 vs. 1797 Elo). Design choices at every stage were made by fixed-budget automated search loops on top of standard architectures and training recipes. We document the full pipeline and the decisions behind it, report the ablations that failed, and evaluate the models across many style prompts and kinds of games, with 1,000 games per setting. The work is fully open source and reproducible: weights, datasets with all training labels, prompts, configurations, inference code and playable demos are public and free to build on.

## Metadata
- **Published**: 2026-10-18T15:57:03Z
- **Authors**: Ilia Badanin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25356v1)