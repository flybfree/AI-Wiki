---
title: Location-Aware Language Models via Secondary Embeddings
published: 2026-08-31T22:48:37Z
authors: Gokul Srinivasagan, Munir Georges
url: http://arxiv.org/abs/2609.00454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Location-Aware Language Models via Secondary Embeddings

## Abstract
Pretrained transformer-based language models achieve strong performance across a wide range of NLP tasks but remain limited in encoding geo-locational semantics, leading to suboptimal representations of place names and spatial entities. In this work, we propose a lightweight, model-agnostic approach for injecting geo-spatial awareness into pretrained embeddings without modifying the tokenizer or requiring costly retraining. Our method augments input representations with structured geographic signals by combining location names with their corresponding latitude and longitude, and employs a location-focused masking to better align textual representations with real-world spatial relationships. This design allows the model to incorporate geo-spatial context while preserving existing semantic and syntactic knowledge. Experimental results demonstrate substantial improvements in geo-spatial alignment while maintaining comparable performance on standard NLP benchmarks such as GLUE. The method is computationally efficient, requiring only minutes of additional training, and generalizes across multiple model architectures and scales.

## Metadata
- **Published**: 2026-08-31T22:48:37Z
- **Authors**: Gokul Srinivasagan, Munir Georges
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00454v1)