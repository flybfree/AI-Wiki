---
title: Predicting Multilingual Classification and Translation Performance of LLMs with Cross-Lingual Alignment $\unicode{x2013}$ Is English Enough?
published: 2026-08-04T10:44:40Z
authors: Adnan Al Ali, Kathy Hämmerl, Jindřich Libovický, Alexander Fraser
url: http://arxiv.org/abs/2608.03446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Predicting Multilingual Classification and Translation Performance of LLMs with Cross-Lingual Alignment $\unicode{x2013}$ Is English Enough?

## Abstract
Multilingual large language models (LLMs) have been shown to perform better on non-English classification tasks when the representations of the given language are more aligned to English within the model. Several cross-lingual alignment (CLA) scores have been proposed for use with LLMs, along with multiple approaches for extracting embeddings from the models. We provide a comparative analysis of 27 CLA score variants, examining how they differ and how well each predicts downstream performance across three tasks. Crucially, while LLMs are widely used for generative tasks such as machine translation, prior work has focused almost exclusively on classification. We therefore investigate whether CLA scores are similarly predictive of translation performance. To enable computing correlations across target languages, we propose a PMI-based translation metric, which is less dependent on the target language and correlates strongly with chrF. We find that CLA with English predicts translation quality comparably to or better than source-target CLA, providing new evidence that LLMs use English as an internal pivot language.

## Metadata
- **Published**: 2026-08-04T10:44:40Z
- **Authors**: Adnan Al Ali, Kathy Hämmerl, Jindřich Libovický, Alexander Fraser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03446v1)