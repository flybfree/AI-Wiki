---
title: Generative vs. Encoder Models for Multilingual NER: A Comprehensive Empirical Study on Naamapadam
url: http://arxiv.org/abs/2608.29959v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_18-41-04Z_Generativevs_EncoderModelsforMultilingualNER_AComp.md
generated_at: 2026-08-31 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper conducts a comprehensive empirical study comparing generative and encoder-based neural architectures for Named Entity Recognition across eleven Indian languages using the Naamapadam benchmark. Encoder models such as mBERT and XLM‑R achieve significantly higher F1 scores than any generative approach, with gaps ranging from 7.5 to 40 percentage points against the best few-shot model.

## Key Takeaways
- Encoder-based architectures dominate performance in ten of eleven languages, delivering F1 values around 0.68 for Hindi while generative models fall far behind at roughly 0.43 on average.  
- The strongest few‑shot generative result reaches only 28 % of the encoder baseline, highlighting a stark limitation of zero‑to‑five shot inference in low‑resource settings.  
- Language performance clusters into three groups: encoder‑dominant languages, partially covered languages, and failure zones where encoders still outperform but gaps are narrower.

## Context
The study addresses a longstanding gap in multilingual NLP where most research focuses on English while Indic languages remain under‑served. By benchmarking diverse model families, it provides empirical evidence that encoder models currently hold the advantage for sequence labeling tasks across many low‑resource languages.

## Implications
For practitioners, this work suggests prioritizing encoder fine‑tuning over generative inference when deploying NER in Indian languages to achieve reliable results with minimal data. It also underscores the need for more robust few‑shot strategies or alternative architectures to close the performance gap in partial‑coverage scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29959v1)
