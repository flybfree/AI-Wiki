---
title: Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?
published: 2026-10-21T12:29:30Z
authors: Esmail Gumaan
url: http://arxiv.org/abs/2610.30205v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?

## Abstract
When an LLM agent's move fails, the harness writes the move and the failure message into the transcript and asks again. In tool calling, this record makes small models more likely to repeat the failed action. We test whether the same holds in games (Sokoban, Connect Four, Othello), where a move can fail by being illegal or by being legal but losing, both verified exactly. On fixed probe items built by perturbing a correct move, the record backfires: pooled over 8 instruction-tuned models (135M-1.7B) it makes the failed move more likely (corrective gain G = -1.38 nats per token), through the move's surface form, for illegal moves but not for losing ones, and not for every model. An exploratory analysis shows what sets the sign: after the record, the failed move's log-probability barely depends on how likely it was before (slope 0.18). Moves the model would not have played become more likely, and greedy decoding starts to produce them; moves it was about to play become less likely, but greedy decoding still repeats 38% of them. A description of the failure that omits the move string keeps the model's preference instead. Along the OLMo 2 1B post-training ladder the inversion is present in the base model and largely removed at the DPO stage. RAGEN's default models invert in RAGEN's own Sokoban format before any RL. A "do not repeat" instruction does nothing, a clean retry is the worst harness, and a decoder ban stops exact repeats but not illegal play. All measurements ran in float32 on a free Colab GPU, which first reproduced the original paper's number.

## Metadata
- **Published**: 2026-10-21T12:29:30Z
- **Authors**: Esmail Gumaan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30205v1)