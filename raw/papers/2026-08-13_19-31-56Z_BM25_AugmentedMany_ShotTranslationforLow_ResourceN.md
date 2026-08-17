---
title: BM25-Augmented Many-Shot Translation for Low-Resource North-Eastern Indian Languages
published: 2026-08-13T19:31:56Z
authors: Aashish Dhawan, Christopher Driggers-Ellis, Dzmitry Kasinets, Christan Grant, Daisy Zhe Wang
url: http://arxiv.org/abs/2608.13722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BM25-Augmented Many-Shot Translation for Low-Resource North-Eastern Indian Languages

## Abstract
This paper describes the University of Florida Gators submission to the WMT26 Low-Resource Indic Language Translation shared task. We adapt the retrieval-augmented many-shot translation pipeline from our AmericasNLP 2026 system to translate between English and eleven North-Eastern Indian languages in both directions. At inference time, BM25 retrieves the most similar parallel examples from a language-specific training bank, and Gemini 2.5 Flash translates the input conditioned on these examples. No model fine-tuning is involved. Training banks combine official WMT26 data with publicly available corpora such as Samanantar and prior WMT shared task releases. A grid search over retrieval count r and development exemplar count d across all 22 language-direction pairs selects the best configuration for each submission.

## Metadata
- **Published**: 2026-08-13T19:31:56Z
- **Authors**: Aashish Dhawan, Christopher Driggers-Ellis, Dzmitry Kasinets, Christan Grant, Daisy Zhe Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13722v1)