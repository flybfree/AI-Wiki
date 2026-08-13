---
title: LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification
published: 2026-08-12T07:46:29Z
authors: Michael Schlee, Fabian Lukassen, Christoph Weisser
url: http://arxiv.org/abs/2608.11753v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification

## Abstract
Financial text is produced and interpreted within a market environment, yet financial text classifiers almost always receive text alone. We study whether financial time series are useful as an additional input on the task of classifying sentences from Federal Reserve communication as hawkish, dovish, or neutral. Our system, \lfts{}, extends the \lf{} architecture with this modality: a small voting network combines three independently trained components, a fine-tuned RoBERTa encoder, a prompted large language model (LLM), and a fused ensemble of time-series transformers over the market series of the months preceding publication. Because only about a thousand annotated sentences are available for training, the RoBERTa encoder is first pre-trained on sentences annotated automatically by the LLM and only then fine-tuned on the human labels. Trained on Federal Open Market Committee (FOMC) communication up to 2015 and evaluated on 2015--2022, the fused system achieves 70.2\% weighted F1 -- against 64.1\% for the zero-shot LLM -- and overtakes it with as few as 240 human-labelled sentences. We take this as initial evidence for market time series as an input modality in financial text classification.

## Metadata
- **Published**: 2026-08-12T07:46:29Z
- **Authors**: Michael Schlee, Fabian Lukassen, Christoph Weisser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11753v1)