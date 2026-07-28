---
title: Simple Language Normalization Wins: Cross-Lingual Speaker Verification for the TidyVoice 2026 Challenge
published: 2026-07-24T21:23:20Z
authors: Nina Hosseini-Kivanani
url: http://arxiv.org/abs/2607.22923v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simple Language Normalization Wins: Cross-Lingual Speaker Verification for the TidyVoice 2026 Challenge

## Abstract
Cross-lingual mismatch remains a key source of overall degradation in modern speaker verification. The TidyVoice2026 Challenge targets this setting with text-independent verification, comprising 3,666 training and 808 development speakers in 40 languages and 2,200 evaluation speakers in 38 unseen languages, without language labels at test time. Starting from the official SimAM-ResNet34 baseline pretrained on VoxBlink2 and VoxCeleb2 and fine-tuned on TidyVoice, we revisit Nuisance Attribute Projection (NAP) as a simple language-normalization step in the embedding space. We estimate a compact language subspace from cross-language same-speaker differences and project embeddings onto its orthogonal complement before cosine scoring with Adaptive Symmetric score normalization. This reduces development EER from 2.97\% with cosine and 2.70\% with AS-Norm to 2.18\% and yields a Codabench evaluation score of 8.40, showing that simple back-end language normalization can rival more complex systems.

## Metadata
- **Published**: 2026-07-24T21:23:20Z
- **Authors**: Nina Hosseini-Kivanani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22923v1)