---
title: RAG-HAR+: Towards Cost-Efficient LLM-Based Human Activity Recognition for Edge Deployment
published: 2026-07-29T08:57:03Z
authors: Hansi Karunarathna, Nirhoshan Sivaroopan, Chamara Madarasingha, Anura Jayasumana, Kanchana Thilakarathna
url: http://arxiv.org/abs/2607.26631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAG-HAR+: Towards Cost-Efficient LLM-Based Human Activity Recognition for Edge Deployment

## Abstract
Human Activity Recognition (HAR) from wearable sensors supports applications in healthcare, rehabilitation, fitness tracking, and smart environments. Yet, existing deep learning approaches require dataset-specific training, large labeled corpora, and repeated adaptation to new sensor settings or activity taxonomies. Retrieval-Augmented Generation for Human Activity Recognition (RAG-HAR) addresses this by framing HAR as a training-free, retrieval-augmented task, in which statistical descriptions of sensor windows are used to retrieve similar labeled examples that guide LLM-based classification. We introduce RAG-HAR+, a retrieval-first and cost-optimized extension that strengthens retrieval while reducing dependence on LLM-based inference. RAG-HAR+ uses an offline Retrieval Designer Agent to design dataset-specific feature groups from a diverse pool of motion descriptors, enabling sensor windows to be compared using features better aligned with dataset-specific activity patterns. During inference, RAG-HAR+ uses majority voting over retrieved neighbors for samples with strong retrieval evidence and defers only uncertain cases to an LLM-based Ambiguity Resolver Agent. Across six HAR benchmarks, RAG-HAR+ maintains competitive or improved performance while reducing LLM usage, token consumption, and inference time. We further extend the RAG-HAR mobile prototype to demonstrate the practical feasibility of retrieval-first, LLM-assisted HAR in mobile sensing scenarios.

## Metadata
- **Published**: 2026-07-29T08:57:03Z
- **Authors**: Hansi Karunarathna, Nirhoshan Sivaroopan, Chamara Madarasingha, Anura Jayasumana, Kanchana Thilakarathna
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26631v1)