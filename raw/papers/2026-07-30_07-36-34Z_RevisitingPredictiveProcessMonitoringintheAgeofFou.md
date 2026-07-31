---
title: Revisiting Predictive Process Monitoring in the Age of Foundation Models: A Comparative Study of Sequence, Tabular, and LLM Approaches
published: 2026-07-30T07:36:34Z
authors: Lennart Fertig, Lukas Kirchdorfer, Tobias Sesterhenn
url: http://arxiv.org/abs/2607.27797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Revisiting Predictive Process Monitoring in the Age of Foundation Models: A Comparative Study of Sequence, Tabular, and LLM Approaches

## Abstract
Predictive process monitoring (PPM) leverages event logs to forecast the future of running process instances, for instance, predicting the next activity, the remaining time until case completion, or the time to the next event. While PPM research in recent years has been dominated by deep sequence models trained from scratch, such as Long Short-Term Memory (LSTM) models, foundation-model approaches---particularly large language models (LLMs)---are increasingly explored for PPM. At the same time, tabular foundation models with in-context learning capabilities offer a promising alternative but have not yet been systematically benchmarked for PPM. Thus, it remains unclear whether classical sequence-based models remain competitive in this evolving landscape. This paper compares the three modeling paradigms both conceptually and empirically through a controlled benchmark across multiple datasets and prediction tasks. The results show that sequence models consistently perform best for next activity prediction, whereas tabular foundation models are competitive on temporal tasks, with LLMs usually lagging behind despite higher cost.

## Metadata
- **Published**: 2026-07-30T07:36:34Z
- **Authors**: Lennart Fertig, Lukas Kirchdorfer, Tobias Sesterhenn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27797v1)