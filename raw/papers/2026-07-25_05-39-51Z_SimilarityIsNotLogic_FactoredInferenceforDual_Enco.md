---
title: Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models
published: 2026-07-25T05:39:51Z
authors: Sultan Alshehri, Zhantao Yang, Han Zhang, Marios Savvides
url: http://arxiv.org/abs/2607.23052v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Similarity Is Not Logic: Factored Inference for Dual-Encoder Vision-Language Models

## Abstract
Dual-encoder vision-language models (VLMs) expose a similarity interface that enables zero-shot retrieval but fails compositional constraints: queries like "umbrella and no person" retrieve images containing both, even when concept detection is reliable. We trace this to an interface-level Bag-of-Concepts effect, where similarity scores approximate mean pooling of concept evidence regardless of operators. Although operator-dependent signals exist in text embeddings, they are too weak or misaligned to affect rankings. Fine-tuning does not reliably resolve this failure because the dominant bottleneck is how similarity aggregates evidence rather than what encoders represent. We propose factored inference, which separates evidence extraction from constraint execution, and introduce LCSE (Logic-Constrained Score Editing), a training-free method that executes constraints externally using concept scores from frozen encoders. We also introduce FACTOR-Bench, where LCSE achieves 85.5% accuracy versus 73.2% for the best fine-tuned baseline, 90.7% when applied to SigLIP 2, and improves NegBench COCO MCQ accuracy from 27.2% to 65.2% while preserving retrieval performance.

## Metadata
- **Published**: 2026-07-25T05:39:51Z
- **Authors**: Sultan Alshehri, Zhantao Yang, Han Zhang, Marios Savvides
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23052v1)