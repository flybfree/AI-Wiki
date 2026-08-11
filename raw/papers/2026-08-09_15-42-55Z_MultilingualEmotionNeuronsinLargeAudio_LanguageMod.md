---
title: Multilingual Emotion Neurons in Large Audio-Language Models
published: 2026-08-09T15:42:55Z
authors: Xiutian Zhao, Philipp Koehn, Björn Schuller, Berrak Sisman
url: http://arxiv.org/abs/2608.08772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multilingual Emotion Neurons in Large Audio-Language Models

## Abstract
Emotion is central to human communication, and its expression varies across languages. Large audio-language models (LALMs) achieve strong performance on multilingual speech tasks, yet it remains unclear whether they encode emotion through language-specific correlations or language-agnostic representations. We present the first neuron-level interpretability study of this question. We define Multilingual Emotion Neurons (MLENs) as functional units exhibiting stable emotional selectivity and aligned causal effects across languages, and introduce Consistency-Regularized Fusion (CR-Fusion) to identify them. Across four modern LALMs and 12 typologically diverse languages, emotion-sensitive neurons identified independently per language show minimal overlap, and additional monolingual identification data saturates quickly without isolating more transferable units, motivating identification from pooled cross-lingual evidence. Causal interventions demonstrate that MLENs identified by CR-Fusion provide more precise and transferable affective control than monolingual neuron sets in both zero-shot and low-resource settings. Leave-one-out ablations further reveal asymmetric transfer: individual identification languages, including low-resource ones, contribute non-redundant evidence, while several low-resource languages benefit most from the resulting cross-lingual transfer. Together, our findings provide the first causal, neuron-level account of how LALMs encode emotion across languages, and establish multilingual neuron identification as an effective mechanism for understanding cross-lingual affective behavior.

## Metadata
- **Published**: 2026-08-09T15:42:55Z
- **Authors**: Xiutian Zhao, Philipp Koehn, Björn Schuller, Berrak Sisman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08772v1)