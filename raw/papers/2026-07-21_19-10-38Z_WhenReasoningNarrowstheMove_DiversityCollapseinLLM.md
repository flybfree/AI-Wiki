---
title: When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play
published: 2026-07-21T19:10:38Z
authors: Junyi Sha, Renfei Tan, David Simchi-Levi
url: http://arxiv.org/abs/2607.19523v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play

## Abstract
Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored. We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly. Across state-level evaluation, arena gameplay, and training trajectories, we find that reasoning-mode generation frequently suppresses action diversity without uniformly improving action accuracy. Furthermore, standard SFT improves accuracy but often induces premature diversity collapse, which exceeds what is minimally required by the accuracy-diversity tradeoff. We then show that action augmentation, which trains on all optimal actions per state rather than a single demonstrated action, would partially mitigates this effect. Our results identify narrow-support imitation as a source of policy collapse in LLM decision-making and suggest that preserving action support during SFT is important for maintaining exploratory behavior.

## Metadata
- **Published**: 2026-07-21T19:10:38Z
- **Authors**: Junyi Sha, Renfei Tan, David Simchi-Levi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19523v1)