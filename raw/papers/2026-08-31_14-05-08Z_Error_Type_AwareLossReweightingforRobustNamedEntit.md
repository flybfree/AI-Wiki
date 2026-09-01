---
title: Error-Type-Aware Loss Reweighting for Robust Named Entity Recognition with Noisy LLM Labels
published: 2026-08-31T14:05:08Z
authors: Elena Merdjanovska, Jonas Golde, Alan Akbik
url: http://arxiv.org/abs/2608.30827v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Error-Type-Aware Loss Reweighting for Robust Named Entity Recognition with Noisy LLM Labels

## Abstract
Large language models are increasingly used to annotate datasets for training smaller, task-specialized models such as named entity recognition. While this method yields effective models, it assumes that the synthetic dataset is correctly annotated. In this work, we find that (i) current fine-tuning processes simply ignore LLM-introduced annotation noise, resulting in degraded performance and (ii) existing noise-robust losses are not transferable to sequence labeling because annotation noise in named entity recognition is heterogeneous: for example, missing mentions and type errors affect the training signal in different ways. Treating all noisy tokens equally in noise-robust losses and applying a single reweighing criterion for all may therefore remove useful supervision or reinforce incorrect labels. To address this limitation, we propose error-type-aware loss reweighting for NER, which introduces separate reweighing rules for different types of potentially erroneous tokens. Our approach is simple and efficient, does not require additional training resources, and improves F1 by 0.8 - 2.0 percentage points on dataset-level average for noise levels between 15% and 40%, with a maximum improvement of 4.6 percentage points with 24.1% noise on Wikigold.

## Metadata
- **Published**: 2026-08-31T14:05:08Z
- **Authors**: Elena Merdjanovska, Jonas Golde, Alan Akbik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30827v1)