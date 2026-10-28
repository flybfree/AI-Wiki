---
title: Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models
published: 2026-10-27T10:10:11Z
authors: XinYu Piao, Myunghoon Ryu, Joongheon Kim, Jong-Kook Kim
url: http://arxiv.org/abs/2610.36948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models

## Abstract
A large language model maintains conversational content in an external storage that is outside the model and grows as the dialogue continues. This work assumes an environment where a language model has no external memory and no prior knowledge of the future question or its answer. The motivation is to research whether a dialogue can be stored in the model parameters and later answer a question about it. This work proposes self-keyed in-parameter memorization (SKIM), a closed-form method in which the model generates its own questions about each dialogue turn and writes those questions into its parameters as the keys that later retrieve the turn's content. Generating many varied questions for each turn allows a later user question to match one even when phrased differently, and its answer is recalled from the parameters alone. Evaluated on five language models, SKIM recalls most stored dialogue turns from later user questions, and it answers from the model parameters without any external storage.

## Metadata
- **Published**: 2026-10-27T10:10:11Z
- **Authors**: XinYu Piao, Myunghoon Ryu, Joongheon Kim, Jong-Kook Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36948v1)