---
title: On Improving Faithfulness of Podcasts from Documents
published: 2026-07-24T04:17:56Z
authors: Soumya Dutta, Tejas Indulal Dhamecha, Pannaga Shivaswamy
url: http://arxiv.org/abs/2607.21961v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Improving Faithfulness of Podcasts from Documents

## Abstract
Large language models (LLMs) are increasingly used to generate long-form conversational content such as podcasts from textual sources. While these systems produce fluent and engaging narratives, they often introduce ungrounded information. In this work, we present the first systematic study of faithfulness in document-grounded podcast generation, where grounding must be maintained across conversational turns in long-form, multi-speaker transcripts. We construct a dataset of over 1500 documents spanning five domains and generate podcast transcripts using multiple LLMs. We introduce a turn-level LLM-as-a-judge framework for evaluating whether conversational turns are supported by the source document, and validate its reliability through human studies. Our analysis shows that even state-of-the-art models, including GPT-4o, frequently generate ungrounded content. To mitigate this issue, we propose catch-n-repair, a model-agnostic framework that detects and rewrites unfaithful conversational turns while preserving conversational flow. Experiments demonstrate consistent improvements in faithfulness across both in-domain and out-of-domain settings.

## Metadata
- **Published**: 2026-07-24T04:17:56Z
- **Authors**: Soumya Dutta, Tejas Indulal Dhamecha, Pannaga Shivaswamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21961v1)