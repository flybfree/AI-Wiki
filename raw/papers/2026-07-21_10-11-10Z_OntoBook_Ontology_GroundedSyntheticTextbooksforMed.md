---
title: OntoBook: Ontology-Grounded Synthetic Textbooks for Medical Encoder Pretraining
published: 2026-07-21T10:11:10Z
authors: Rian Touchent, Éric de la Clergerie
url: http://arxiv.org/abs/2607.18927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OntoBook: Ontology-Grounded Synthetic Textbooks for Medical Encoder Pretraining

## Abstract
We present OntoBook, a method that converts medical ontology structure into pretraining signal for encoder language models. Our approach has three stages: random walks through ontology graphs capture hierarchical and causal relations between medical codes, a large language model reformulates these walks into fluent textbook-style prose, and the resulting text is used to train ModernCamemBERT, a 149M-parameter French encoder, with two objectives on the same data: masked language modeling and relation prediction between code pairs. On three French medical coding benchmarks (FRACCO, Cantemist-FR, Distemist-FR), OntoBook achieves significant improvements over MLM-only pretraining, with +2.5 micro-F1 on FRACCO and +8.0 micro-F1 on Distemist. We find that alignment between objectives is necessary: misaligned training, where each task uses different data, causes a 30-point degradation. We release 1.3 million LLM-reformulated medical textbooks across three French ontologies (CIM-10, CCAM, ATC) and pretrained model checkpoints.

## Metadata
- **Published**: 2026-07-21T10:11:10Z
- **Authors**: Rian Touchent, Éric de la Clergerie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18927v1)