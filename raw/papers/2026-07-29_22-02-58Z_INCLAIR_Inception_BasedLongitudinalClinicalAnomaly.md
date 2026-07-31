---
title: INCLAIR: Inception-Based Longitudinal Clinical Anomaly Detection with Informed Reasoning
published: 2026-07-29T22:02:58Z
authors: Maxx Richard Rahman, Wolfgang Maass
url: http://arxiv.org/abs/2607.27487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# INCLAIR: Inception-Based Longitudinal Clinical Anomaly Detection with Informed Reasoning

## Abstract
Detecting anomalies in longitudinal clinical profiles is clinically important but difficult: abnormal evidence is often sparse, patient histories have unequal length, and expert explanations are costly. We propose INCLAIR, a framework that scores each observation against multiple historical contexts, aggregates evidence at the profile level, and generates grounded natural-language explanations under limited expert supervision. Under stated within-profile exchangeability assumptions, the complete mean subsequence score takes an order-$l$ U-statistic form, yielding a variance decomposition and an incomplete-subset approximation that controls combinatorial inference cost independently of profile length. The same analysis shows that mean aggregation attenuates localized anomalies by a factor set by the anomaly support and profile length, motivating validation-selected top-$k$ pooling. Across three clinical datasets, INCLAIR consistently outperforms state-of-the-art baselines. We further validate practical relevance through a case study on longitudinal steroid profiles, comparing INCLAIR's predictions and explanations against domain-expert assessments supported by DNA analysis. The results show that INCLAIR enables clinically actionable anomaly detection under limited expert supervision.

## Metadata
- **Published**: 2026-07-29T22:02:58Z
- **Authors**: Maxx Richard Rahman, Wolfgang Maass
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27487v1)