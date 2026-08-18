---
title: What to Forget in Unlearning? Forget Set Curation for Language Models
published: 2026-08-14T19:51:53Z
authors: Animesh Jha, Arpandeep Khatua, Youssef Allouah, Sanmi Koyejo
url: http://arxiv.org/abs/2608.14855v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What to Forget in Unlearning? Forget Set Curation for Language Models

## Abstract
Machine unlearning aims to remove targeted data or behaviors from a trained model without retraining from scratch. Yet most evaluations assume that the examples to forget are already known. In realistic language-model deployments, a requester may ask a model to stop reproducing a song or book without knowing which spans, documents, quotations, or near-duplicates in a trillion-token corpus support that behavior. We study this missing upstream problem, forget set curation: mapping a suppression request to the data passed to an unlearning algorithm. We introduce CleanSlate, a benchmark for verbatim output suppression over songs and books, with model-specific extraction profiles, content-grounded QA, and capability-retention evaluations. CleanSlate exposes two failure modes. Natural lexical and exact-substring curators often yield forget sets that lead to weak suppression. An evaluation-aware curator suppresses requested continuations almost completely, but causes collateral regression on non-requested content and model-dependent capability loss. These results show that practical unlearning is not only an optimization problem once a forget set is given: the data chosen for forgetting determines both what can be unlearnt and what else is damaged.

## Metadata
- **Published**: 2026-08-14T19:51:53Z
- **Authors**: Animesh Jha, Arpandeep Khatua, Youssef Allouah, Sanmi Koyejo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14855v1)