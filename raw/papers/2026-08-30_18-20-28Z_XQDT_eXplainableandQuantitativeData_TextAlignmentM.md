---
title: XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals
published: 2026-08-30T18:20:28Z
authors: Kun Efimov-Zhang, Yifei Song, Claire Gardent
url: http://arxiv.org/abs/2608.29948v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals

## Abstract
Evaluating data-text alignment remains challenging: existing metrics often provide limited explanations for the scores, while prompt-based LLM-as-Judge methods can be expensive and unreliable. We present an end-to-end explainable evaluation metric that fine-tunes a language model to identify omitted, extra, incorrect, and correct data units in a data-text pair. These local judgements are aggregated into precision, recall, and F1 scores, providing both fine-grained diagnostic feedback and an interpretable measure of alignment quality. Across benchmarks, our fine-tuned models outperform LLM-as-Judge methods in error prediction and achieve competitive precision, recall, and F1 scores, while maintaining strong correlation with human judgements. Beyond evaluation, our verifier outputs also provide useful feedback signals for downstream correction and refinement, supporting alignment-oriented improvement of data-to-text and text-to-data. Code and resources are available at https://github.com/guihuzhang/xqdt.

## Metadata
- **Published**: 2026-08-30T18:20:28Z
- **Authors**: Kun Efimov-Zhang, Yifei Song, Claire Gardent
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29948v1)