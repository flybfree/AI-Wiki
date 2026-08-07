---
title: Align-RAG: Alignment Is All You Need for TSFM In-Context Learning
published: 2026-08-06T03:43:45Z
authors: Mohammad Asadi, Soheil Hor, Bardiya Akhbari, Jack W. O'Sullivan, Tahoura Nedaee, Layne C. Price, Raviteja Anantha, Euan Ashley, Ehsan Adeli
url: http://arxiv.org/abs/2608.05571v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Align-RAG: Alignment Is All You Need for TSFM In-Context Learning

## Abstract
Retrieval-augmented forecasting promises to adapt frozen Time Series Foundation Models (TSFMs) to new domains without fine-tuning, but recent methods typically rely on learned fusion modules, i.e., trained adapters that merge retrieved examples into the backbone's forecast, based on the assumption that frozen backbones cannot dynamically incorporate retrieved context on their own. We show this assumption is unnecessary. We introduce Align-RAG, a training-free method that applies a closed-form per-pair amplitude rescaling and integer-lag phase shift to retrieved past-future windows before they enter a frozen backbone's context. With no learned parameters, Align-RAG outperforms the state-of-the-art trained retrieval adapter on a frozen Chronos-Bolt on all seven datasets of the standard benchmark (avg -3.75% MSE), showing that the gains previously attributed to learned fusion are recoverable without any training. Align-RAG further improves zero-shot MSE on four additional frozen TSFMs with various architectures by 2.5% to 13.7% per backbone with no per-backbone tuning. To probe why alignment helps, we compare the frozen backbone's prediction shift under aligned demonstrations to the closed-form ridge prediction shift on the same pairs. We find that aligned demonstrations induce prediction shifts that track a closed-form ridge predictor on the same pairs, with a future-shuffle control ruling out a futures-averaging account. Together, these results indicate that frozen TSFMs already support dynamic in-context use of retrievals, and that closed-form alignment should be the default baseline for retrieval-augmented forecasting before any fusion module is trained. Code available at: https://github.com/masadi-99/align-rag

## Metadata
- **Published**: 2026-08-06T03:43:45Z
- **Authors**: Mohammad Asadi, Soheil Hor, Bardiya Akhbari, Jack W. O'Sullivan, Tahoura Nedaee, Layne C. Price, Raviteja Anantha, Euan Ashley, Ehsan Adeli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05571v1)