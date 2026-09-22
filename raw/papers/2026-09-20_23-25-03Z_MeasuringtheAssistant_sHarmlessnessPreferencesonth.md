---
title: Measuring the Assistant's Harmlessness Preferences on the User Turn
published: 2026-09-20T23:25:03Z
authors: Jord Nguyen
url: http://arxiv.org/abs/2609.23935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring the Assistant's Harmlessness Preferences on the User Turn

## Abstract
Post-training turns a general next-token predictor into a chat model with a persistent assistant persona. If that persona is a character the model plays only on its own turns, its preferences should govern what the assistant says, not what the model predicts other speakers will say. We test this boundary and find that it does not hold: a safety-relevant preference of the assistant---for harmless over harmful tasks---shapes the model's predictions even on the user's turn, where the assistant is not the one speaking. We find that this preference is small or near-zero in pretrained base models, that it emerges through post-training, replicated across open-weight model families, grows with scale, and can be moved by narrow finetuning that never touches user turns. We claim that this is evidence that post-training does not merely install a shallow assistant persona, but instead generalises beyond just the local assistant turn, into the model's representation of the user.

## Metadata
- **Published**: 2026-09-20T23:25:03Z
- **Authors**: Jord Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23935v1)