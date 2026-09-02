---
title: Context Window Failures in Relational Foundation Models
published: 2026-08-31T22:59:57Z
authors: Denis Oliveira Correa, Francisco Galuppo Azevedo
url: http://arxiv.org/abs/2609.00460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context Window Failures in Relational Foundation Models

## Abstract
Recent Relational Deep Learning architectures have been proposed as foundation models for multi-table relational data, yet they impose constrained neighborhood budgets that force row truncation when an entity has many related records. We introduce Animus, a synthetic financial dataset in which predicting customer income requires aggregating up to tens of thousands of transactions. On the raw representation, three recently proposed models (RT, Griffin, RelGT) achieve $R^2 \le 0.18$; a single, routine, temporal pre-aggregation step recovers $R^2$ up to $0.65$. This questions whether current relational foundation models are ready for high-cardinality real-world data.

## Metadata
- **Published**: 2026-08-31T22:59:57Z
- **Authors**: Denis Oliveira Correa, Francisco Galuppo Azevedo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00460v1)