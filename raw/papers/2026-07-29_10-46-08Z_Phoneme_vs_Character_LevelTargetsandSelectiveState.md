---
title: Phoneme- vs. Character-Level Targets and Selective State-Space Models for Intracortical Brain-to-Text
published: 2026-07-29T10:46:08Z
authors: Lucas Zamora Vera, Jose A. Gonzalez-Lopez
url: http://arxiv.org/abs/2607.26751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Phoneme- vs. Character-Level Targets and Selective State-Space Models for Intracortical Brain-to-Text

## Abstract
State-of-the-art intracortical brain-to-text systems pair a neural-sequence phone decoder with an external language model. Two design axes remain underexplored: whether selective state-space models (Mamba) improve on recurrent decoders, and how the output target (phonetic vs.\ character) interacts with that choice. On the public Brain-to-Text '25 benchmark, we study a controlled 2x2 grid (GRU vs.\ hybrid Mamba decoder; phonetic vs.\ character targets) trained with a CTC objective under one reproducible protocol. The recurrent baseline remains strongest: the best phonetic GRU reaches 12.62\% PER and 21.19\% WER, while the best textual GRU after LM rescoring reaches 13.39\% CER and 26.28\% WER. The Mamba hybrid is competitive but does not surpass it. Ablations isolate architectural contributions, and error analysis shows representation-dependent failures: articulatory-like phoneme confusions vs.\ lexical and word-boundary errors.

## Metadata
- **Published**: 2026-07-29T10:46:08Z
- **Authors**: Lucas Zamora Vera, Jose A. Gonzalez-Lopez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26751v1)