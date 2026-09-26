---
title: ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction
published: 2026-09-24T08:02:48Z
authors: Sudha Priyadarshini, Mohamed Chahine Ghanem
url: http://arxiv.org/abs/2609.29191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction

## Abstract
Sensitive information is defined by domain and intent, not a universal category, yet redaction systems such as privacy filters and named-entity recognizers fix a taxonomy at training time, requiring retraining for each new domain. We introduce ASIRF (Agentic Sensitive Information Redaction Framework), which retrieves domain-specific definitions based on the input's domain from a flexible knowledge base at inference time, needing no retraining to adapt. Two architectures, a three-call multi-agent pipeline and a single-agent variant, are evaluated across ten small open-weight models and eight datasets, including out-of-distribution fictional domains, against the OpenAI Privacy Filter (OPF) as a trained-classifier baseline. With only a few dozen expert-authored definitions per domain and no training data, ASIRF's recall exceeds OPF's in 68 of 80 model-domain combinations (85 percent), by at least one of the two architectures, with shortfalls confined mostly to OPF's training-distribution domains.

## Metadata
- **Published**: 2026-09-24T08:02:48Z
- **Authors**: Sudha Priyadarshini, Mohamed Chahine Ghanem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29191v1)