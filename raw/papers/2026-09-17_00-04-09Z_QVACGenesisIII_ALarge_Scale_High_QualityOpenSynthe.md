---
title: QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training
published: 2026-09-17T00:04:09Z
authors: Davide Vitabile, N. Ranjan, Akshay Nambiar, Kamal K. Gupta, Amril Nazir
url: http://arxiv.org/abs/2609.19513v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QVAC Genesis III: A Large-Scale, High-Quality Open Synthetic STEM Corpus for Efficient Language Model Pre-Training

## Abstract
High-quality pre-training data is a critical bottleneck for educational and STEM-specific language models targeting edge AI and on-device deployment where token budgets are tightly constrained. While major organizations train ever-larger models on private corpora, the open ecosystem lacks STEM-focused synthetic datasets that deliver high per-token learning value efficiently for small models. To address this gap, we introduce QVAC Genesis III, a 191.43B-token, STEM-focused multi-domain synthetic corpus covering 19 domains across several difficulty levels and different educational styles. QVAC Genesis III is built via a dual generation strategy that performs targeted teacher distillation using a weak edge-scale student model as signal: the student's failures are converted into corrective explanations, while its successes are expanded into contrastive option-level reasoning over all answer choices. We further introduce an LLM-as-a-parser evaluation protocol that extracts final answers from free-form outputs and tracks both accuracy and answer validity. To validate the effectiveness of our QVAC Genesis III data, we conduct controlled from-scratch ablations with 1.7B-parameter models, showing that models trained with QVAC Genesis III consistently outperform both models trained with the open-source synthetic corpus Cosmopedia-v2 and the publicly released Cosmo-1B model across ARC, GPQA Diamond, and MMLU STEM benchmarks, achieving up to +28.57% on ARC-E and +21.35% on ARC-C, while reaching a Valid Answer Rate of up to 99.45%.

## Metadata
- **Published**: 2026-09-17T00:04:09Z
- **Authors**: Davide Vitabile, N. Ranjan, Akshay Nambiar, Kamal K. Gupta, Amril Nazir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19513v1)