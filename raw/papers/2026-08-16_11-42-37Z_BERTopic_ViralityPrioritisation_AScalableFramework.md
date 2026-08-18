---
title: BERTopic-Virality Prioritisation: A Scalable Framework for Thematic and Comparative Analysis of COVID-19 and Monkeypox Misinformation on Twitter
published: 2026-08-16T11:42:37Z
authors: Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao
url: http://arxiv.org/abs/2608.15691v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BERTopic-Virality Prioritisation: A Scalable Framework for Thematic and Comparative Analysis of COVID-19 and Monkeypox Misinformation on Twitter

## Abstract
Health misinformation circulating during pandemics can gain traction rapidly, creating harmful narratives that compete with public health guidance. Most topic-modelling pipelines treat engagement as an external outcome, limiting their ability to prioritise semantically coherent topics that are also rapidly diffusing. We introduce BERTopic-VP, a virality-prioritised topic-modelling framework that combines contextual embedding-based clustering (BERTopic) with a post hoc Virality Prioritisation (VP) layer. The pipeline is complemented by a two-stage hybrid misinformation detection module that fuses a supervised content-based classifier with an external verification signal derived from public-health knowledge bases. Applied to three benchmark datasets, COVID-19_FNIR, Monkeypox, and Constraint, the framework achieves strong classification performance, with F1 up to 0.950 and ROC-AUC up to 0.989, while identifying high-impact clusters under top 1%, 5%, and 10% VP thresholds. For datasets without native engagement metadata, prioritisation is based on a logistic propensity-to-spread score, used as an ordinal proxy for diffusion potential rather than a direct measure of engagement. The results show that integrating semantic structure, virality-aware ranking, and affective-linguistic profiling enables scalable and interpretable comparative analysis of misinformation across pandemics. The proposed framework supports monitoring-oriented early warning by surfacing low-volume but high-risk narratives for analyst review.

## Metadata
- **Published**: 2026-08-16T11:42:37Z
- **Authors**: Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15691v1)