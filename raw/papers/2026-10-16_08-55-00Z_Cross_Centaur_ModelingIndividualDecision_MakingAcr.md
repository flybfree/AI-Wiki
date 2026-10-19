---
title: Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models
published: 2026-10-16T08:55:00Z
authors: Hikaru Asano, Hidezo Suganuma, Ryutaro Mori, Yukino Baba
url: http://arxiv.org/abs/2610.23157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Centaur: Modeling Individual Decision-Making Across Psychological Tasks with Language Models

## Abstract
Large language models (LLMs) are increasingly used as computational models of human behavior. Recent models such as Centaur have advanced this goal by fine-tuning LLMs on trial-by-trial decisions from psychological experiments. However, existing large-scale behavioral datasets do not link the same participants across different tasks, so these models learn population-level regularities but are not trained to model individual-level regularities across tasks. We introduce Cross-Psych-101, a dataset of 591 participants and 261{,}551 valid decisions across 12 Bandit, Tradeoff, Structure, and Social tasks. We train Cross-Centaur to predict a participant's target-task actions from a target-task description and the source-task description paired with the same participant's source-task behavior. Cross-Centaur outperforms off-the-shelf LLMs and Centaur on held-out participants, both within and across tasks. Probing analyses suggest that its hidden states encode participant-level behavioral tendencies that transfer across tasks. These results highlight the potential of cross-task individual-level data for predicting human decision-making with language models. Cross-Pysch-101 is available at https://huggingface.co/datasets/HikaruAsano/cross-psych-101.

## Metadata
- **Published**: 2026-10-16T08:55:00Z
- **Authors**: Hikaru Asano, Hidezo Suganuma, Ryutaro Mori, Yukino Baba
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23157v1)