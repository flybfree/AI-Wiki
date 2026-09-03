---
title: A Unified Particle Filter LSTM for Data-Driven Process Simulation
published: 2026-09-02T00:53:37Z
authors: Parvin Malekzadeh, Opher Baron, Dmitry Krass
url: http://arxiv.org/abs/2609.01967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Particle Filter LSTM for Data-Driven Process Simulation

## Abstract
Data-driven process simulation aims to generate realistic case trajectories from historical event logs without requiring an explicitly specified model of the underlying dynamics. Deep sequence models can capture complex temporal dependencies through next-activity probabilities and conditional time distributions. However, event logs provide only a partial view of the underlying process state, often recording activity completions without the corresponding service-start times. Consequently, the same observed process history may be consistent with multiple plausible latent process conditions, whereas standard recurrent models compress each process prefix into a single deterministic recurrent state. We propose a Unified Particle Filter LSTM (Unified PF-LSTM) that maintains and sequentially updates a weighted set of recurrent-state hypotheses. We summarize this particle belief using its weighted mean and learned features based on the moment-generating function. The resulting representation is used to predict a categorical distribution over the next activity and conditional quantiles of the current activity's sojourn time. The framework is trained end-to-end from event-log data and evaluated on three real-world emergency department datasets. The results show that the proposed framework consistently outperforms the considered data-driven baselines in reproducing routing, duration, and system-level behavior across all datasets, with particularly strong gains in settings where complex process dynamics are only partially reflected in the available event logs.

## Metadata
- **Published**: 2026-09-02T00:53:37Z
- **Authors**: Parvin Malekzadeh, Opher Baron, Dmitry Krass
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01967v1)