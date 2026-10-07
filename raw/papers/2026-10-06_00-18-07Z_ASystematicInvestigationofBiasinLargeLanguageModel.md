---
title: A Systematic Investigation of Bias in Large Language Models for Advertising Relevance
published: 2026-10-06T00:18:07Z
authors: Weiwei Wang, Yinchuan Xu, Jialu Gao, Youkow Homma, Jian Jiao
url: http://arxiv.org/abs/2610.07544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Systematic Investigation of Bias in Large Language Models for Advertising Relevance

## Abstract
Large language models (LLMs) are increasingly used to judge how well an advertisement matches a query, but the fairness of these judgments has received limited attention. We conduct a systematic study of fairness in relevance judgments made by LLMs for queries and advertisements. Our counterfactual framework examines the effects of advertiser identity and possible popularity, input language, and demographic wording. We study GPT-4o as a categorical relevance judge and a Qwen-7B model trained specifically for relevance prediction. The advertiser and language experiments use query and advertisement pairs sampled from real advertising logs. Controlled synthetic queries are used to study demographic associations in employment, housing, and credit. For both models, changing the advertiser identity or input language can alter the relevance assessment. Selected demographic comparisons also show patterns consistent with common stereotypes, particularly those involving gender and occupation. We further study mitigation during model inference and training. The results indicate that its effectiveness depends on whether advertiser information is relevant to the query and how advertiser labels are distributed in the training data. These findings can help advertising practitioners identify fairness risks and develop suitable mitigation methods for LLM relevance systems.

## Metadata
- **Published**: 2026-10-06T00:18:07Z
- **Authors**: Weiwei Wang, Yinchuan Xu, Jialu Gao, Youkow Homma, Jian Jiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07544v1)