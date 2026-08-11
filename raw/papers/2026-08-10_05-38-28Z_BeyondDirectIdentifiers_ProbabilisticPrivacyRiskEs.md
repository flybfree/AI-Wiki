---
title: Beyond Direct Identifiers: Probabilistic Privacy Risk Estimation for Privacy-Conscious LLM Query Delegation
published: 2026-08-10T05:38:28Z
authors: Li Siyan, Zhou Yu, Julia Hirschberg
url: http://arxiv.org/abs/2608.09140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Direct Identifiers: Probabilistic Privacy Risk Estimation for Privacy-Conscious LLM Query Delegation

## Abstract
Recent work on protecting privacy during user-LLM interactions often focuses on direct, explicit identifiers: the personally-identifiable information (PII) captured by standard detectors. One such approach is Privacy-Conscious Delegation (PCD), where a local LLM acts as an intermediary. However, privacy risk does not stem solely from explicit identifiers but also PII-free self-disclosures, leaving users identifiable through combinations of quasi-identifying traits. We investigate a probabilistic variant of PCD, where we augment its objectives with an LLM-driven probabilistic estimation of k-anonymity. To facilitate this, we first create the PUPA-SD dataset, which contains naturalistic user queries with self-disclosure. Our preliminary results indicate that optimizing PAPILLON on PUPA-SD improves quality on unseen conversations across a variety of local models and produces the best privacy-utility balance for Llama-3.2-3B, while smaller models struggle to jointly optimize quality and privacy. We propose k-anonymity as a useful auxiliary metric for tackling PCD.

## Metadata
- **Published**: 2026-08-10T05:38:28Z
- **Authors**: Li Siyan, Zhou Yu, Julia Hirschberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09140v1)