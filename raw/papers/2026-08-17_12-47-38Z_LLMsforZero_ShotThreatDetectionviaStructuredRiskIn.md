---
title: LLMs for Zero-Shot Threat Detection via Structured Risk Indicators
published: 2026-08-17T12:47:38Z
authors: Abdullah Alghamdi, Siamak Layeghy, Marius Portmann
url: http://arxiv.org/abs/2608.16508v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs for Zero-Shot Threat Detection via Structured Risk Indicators

## Abstract
We propose a two-stage large language model (LLM) framework for zero-shot detection of insider threats and advanced persistent threats (APTs) from heterogeneous security logs. The framework models user activity as chronological timelines and incorporates retrieval-augmented generation (RAG) to provide personalised behavioural context from each user's historical activity. Rather than performing end-to-end classification directly from raw logs, it first generates structured, interpretable sets of threat-specific risk indicators, which are then classified jointly across temporal sequences to capture attack patterns spanning multiple windows.The framework is evaluated on two benchmark datasets, CERT r5.2 for insider threat detection and PicoDomain for APT detection, using four combinations of two open-weight LLMs under both retrieval and non-retrieval settings. All configurations outperform the previous state-of-the-art LLM-based framework (GABM), with the best configuration improving the F1-score by 11.40 percentage points on CERT r5.2 and 31.50 percentage points on PicoDomain. Results further show that retrieval mainly benefits weaker LLMs by generating more discriminative risk indicators, whereas stronger models achieve comparable performance without retrieved context. The most effective assignment of LLMs to the two stages depends on the dataset. These findings show that the quality of the generated risk indicators is the main driver of zero-shot cyber threat detection performance.

## Metadata
- **Published**: 2026-08-17T12:47:38Z
- **Authors**: Abdullah Alghamdi, Siamak Layeghy, Marius Portmann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16508v1)