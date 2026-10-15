---
title: Pre-Trained Language Models as Zero-Shot Tools for Social Science Research
published: 2026-10-13T18:43:04Z
authors: Noah Dasanaike
url: http://arxiv.org/abs/2610.19048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pre-Trained Language Models as Zero-Shot Tools for Social Science Research

## Abstract
Record linkage and demographic inference from names are routine demands in social science. Most approaches to these problems require labeled training data that are difficult or costly to acquire. I show that pre-trained language models perform both tasks accurately without requiring task-specific training. For record linkage, I introduce EnsembleLink, an algorithm that uses pre-trained embeddings alongside string-based scorers to retrieve a short list of candidates and then identify the likeliest matches. EnsembleLink matches or exceeds the performance of most prior approaches while generalizing across scripts and formats that those methods are unable to handle. For ethnicity inference from names, I show that large language models (LLMs) achieve up to 83.8% accuracy on U.S. voter files, compared to 78.0% for name-supplemented BISG. Open-weight models offer reproducible implementations that approach these models in accuracy. Moreover, LLMs are able to infer group membership for religious, caste-based, and other ethnic group categories outside of the United States, and reduce bias in downstream estimates of geographic racial gaps. Where pre-training encodes the world knowledge required by each task, task-specific labels add less information.

## Metadata
- **Published**: 2026-10-13T18:43:04Z
- **Authors**: Noah Dasanaike
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19048v1)