---
title: Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination Detection
published: 2026-09-04T11:44:11Z
authors: Renato Vukovic, Hsien-chin Lin, Carel van Niekerk, Benjamin Ruppik, Michael Heck, Shutong Feng, Nurul Lubis, Milica Gasic
url: http://arxiv.org/abs/2609.05025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination Detection

## Abstract
Hallucination-where a language model generates outputs that are factually incorrect or unsupported by the source-is a major challenge for both prompted and fine-tuned language models. Detecting hallucinations is difficult due to the opaque reasoning processes of LLMs, which often provide little insight into why a model's output may be inaccurate.   In this work, we investigate whether an LLM can use an alternative, low level, symbolic competence such as SQL for unsupervised hallucination detection in some high level task. For this, we make an LLM build an SQL database from reference documents. This SQL database is then used for reasoning over the reference and the sampled response in a hallucination detection pipeline that is grounded in the database, thereby providing a neurosymbolic checkup.   On RAGTruth and DiaHalu hallucination detection datasets, we find that our approach improves on direct prediction and competes with state-of-the-art hallucination detection methods, while not requiring domain-specific fine-tuning. Instead it relies on a low-level general competence already present in LLMs. This warrants further investigation of low-level LLM competences in neurosymbolic approaches.

## Metadata
- **Published**: 2026-09-04T11:44:11Z
- **Authors**: Renato Vukovic, Hsien-chin Lin, Carel van Niekerk, Benjamin Ruppik, Michael Heck, Shutong Feng, Nurul Lubis, Milica Gasic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05025v1)