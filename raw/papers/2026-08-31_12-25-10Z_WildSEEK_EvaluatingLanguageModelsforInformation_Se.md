---
title: WildSEEK: Evaluating Language Models for Information-Seeking
published: 2026-08-31T12:25:10Z
authors: Tanise Ceron, Joachim Baumann, Elisa Bassignana, Berat Cabuk, Dirk Hovy, Debora Nozza
url: http://arxiv.org/abs/2608.30683v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WildSEEK: Evaluating Language Models for Information-Seeking

## Abstract
Language models are increasingly mediating information access to end users, urging a systematic evaluation of their responses for a fair and reliable information ecosystem. Existing evaluations, however, are often topic-specific or synthetic, limiting their ability to capture the complexity of "in the wild" information-seeking queries and the risks present in model responses. To address this gap, we introduce WildSEEK, a manually annotated dataset of 3k information-seeking queries from real user interactions, and an evaluation framework for LLM-generated responses. WildSEEK includes annotations for risk-sensitive domains (e.g. health and financial information), and distinguishes factoid queries from analytical queries which seek responses beyond facts. We train classifiers on WildSEEK to analyze more than 1.8M realistic user queries. We find that over a third of information-seeking queries are high-risk and more often analytical. Our findings show that LLM responses fail more often in four criteria: sycophantic behavior, overreliance, a default US-centric perspective, and poor handling of vulnerable populations -- with failure rates being mostly higher for analytical queries. By providing methods to monitor the reliability, safety, and fairness of LLM behavior, our dataset and evaluation framework offer an empirical foundation for the broader question of how these systems should behave as they take on a growing role in information access.

## Metadata
- **Published**: 2026-08-31T12:25:10Z
- **Authors**: Tanise Ceron, Joachim Baumann, Elisa Bassignana, Berat Cabuk, Dirk Hovy, Debora Nozza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30683v1)