---
title: Dynamically Allocating Evaluation Effort for Model Ranking
published: 2026-08-04T10:33:04Z
authors: Vilém Zouhar, Julia Kreutzer, Alon Lavie, Tom Kocmi, Matt Post, Ondřej Bojar, Mrinmaya Sachan
url: http://arxiv.org/abs/2608.03437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamically Allocating Evaluation Effort for Model Ranking

## Abstract
While human evaluation is the gold standard in many NLP tasks, it suffers from prohibitive costs and poor scalability. When identifying top-performing models, typical evaluation protocols waste effort by exhaustively evaluating all models on the entire benchmark, a safe but inefficient approach. In this work, we formalize multi-model human evaluation as a best-arm identification problem in a multi-armed bandit setup with correlated arms, where pulling an arm corresponds to human-evaluating a model. By sampling adaptively based on the intermediate model rankings obtained on the samples so far, we can focus the annotation budget on the most competitive models. We prove the optimality of the proposed algorithms and show that it improves discrimination between top-performing models. This makes evaluations faster, cheaper and more aligned with large-scale competition evaluation goals.

## Metadata
- **Published**: 2026-08-04T10:33:04Z
- **Authors**: Vilém Zouhar, Julia Kreutzer, Alon Lavie, Tom Kocmi, Matt Post, Ondřej Bojar, Mrinmaya Sachan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03437v1)