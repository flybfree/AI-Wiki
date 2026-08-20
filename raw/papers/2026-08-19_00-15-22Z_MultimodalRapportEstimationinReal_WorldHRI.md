---
title: Multimodal Rapport Estimation in Real-World HRI
published: 2026-08-19T00:15:22Z
authors: Akihiro Sakuramoto, Takato Hayashi, Ryo Miyoshi, Yuki Okafuji, Shogo Okada
url: http://arxiv.org/abs/2608.18401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multimodal Rapport Estimation in Real-World HRI

## Abstract
Evaluating interaction quality in real-world HRI is an important challenge. If interaction quality can be estimated reliably, the results can be used to improve dialogue strategies and ultimately enable robots to adapt their behavior autonomously. However, existing automatic evaluation methods have been developed primarily in controlled laboratory settings, and it remains unclear whether they can be directly applied to real-world environments, where users are free to disengage and multi-party participation may arise naturally. In this study, we investigate the automatic estimation of third-party-rated rapport scores using 62 sessions of multimodal recordings collected in a Japanese drugstore. We compare zero-shot LLMs, pretrained text, audio, and visual models, and their prediction-level fusion. The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information. In particular, Gemini 2.5 Flash performs strongly as a single model, and a fusion model combining Gemini (text) with HuBERT and V-JEPA performs best overall. Further analyses showed that estimation performance varied across interaction-duration and group-size conditions. These findings suggest that rapport estimation in real-world HRI requires evaluation and model design that account for contextual variability beyond that assumed in laboratory settings.

## Metadata
- **Published**: 2026-08-19T00:15:22Z
- **Authors**: Akihiro Sakuramoto, Takato Hayashi, Ryo Miyoshi, Yuki Okafuji, Shogo Okada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18401v1)