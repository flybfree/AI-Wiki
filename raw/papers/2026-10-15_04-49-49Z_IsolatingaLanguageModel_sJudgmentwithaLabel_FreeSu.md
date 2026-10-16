---
title: Isolating a Language Model's Judgment with a Label-Free Subspace
published: 2026-10-15T04:49:49Z
authors: Chaemin Jang, Donggyu Lee, Jeesoo Kim, Dongman Lee, Jihee Kim
url: http://arxiv.org/abs/2610.21256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Isolating a Language Model's Judgment with a Label-Free Subspace

## Abstract
Language models are often asked to make judgments: whether a proposed answer is correct, whether one statement follows logically from another, or whether a response is safe. Yet changing the instructions that specify how the judgment should be expressed can make the final answer less reliable, even for the same input. We ask whether this reflects a change in internal judgment or a failure to express it. Comparing hidden-state vectors for the same input under different instructions, we find that their differences concentrate in a low-dimensional expression subspace. We identify this subspace without benchmark labels and remove its contribution from a linear predictor to obtain an isolated judgment. Across correctness, entailment, and safety, the isolated judgment remains reliable under instructions not used to identify the subspace, even when the model's final answer and the original predictor degrade. When the judgment question is negated, isolation raises the predictor's AUROC from 0.504 to 0.825 for entailment and from 0.480 to 0.891 for safety. We also find that judgment is readable in earlier layers, before the expression subspace begins to disrupt the predictor. Together, these results provide a way to separate judgment from expression and recover internal judgments even when the model's final answers are unreliable.

## Metadata
- **Published**: 2026-10-15T04:49:49Z
- **Authors**: Chaemin Jang, Donggyu Lee, Jeesoo Kim, Dongman Lee, Jihee Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21256v1)