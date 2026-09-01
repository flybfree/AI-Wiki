---
title: Stratified Consistency Distillation for Natural Language Formalization
published: 2026-08-31T05:08:08Z
authors: Zhichao Hou, Ferhat Erata, Joe Lilien, MohamadAli Torkamani
url: http://arxiv.org/abs/2608.30258v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stratified Consistency Distillation for Natural Language Formalization

## Abstract
Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers. While this approach shows promise, a fundamental challenge remains: improving the accuracy of translations from natural language to logical formulas. Current methods predominantly rely on prompt engineering, which is difficult to scale across different domains and input formats. Drawing inspiration from the success of fine-tuning in other model adaptation and alignment applications, we propose a fine-tuning-based Stratified Consistency Distillation approach: (1) We generate K logical translations per input using a frontier LLM and cluster them by semantic equivalence (2) Based on the entropy level, we apply majority voting (low entropy), LLM-as-a-Judge (medium entropy), or unification/abstention (high entropy), and (3) fine-tune a smaller model using the selected pseudo-labels. Our experiments show significant and consistent improvements in both Pass@K and our novel Equivalent Logical Similarity metrics, demonstrating the potential of advancing logical translation through consistency distillation.

## Metadata
- **Published**: 2026-08-31T05:08:08Z
- **Authors**: Zhichao Hou, Ferhat Erata, Joe Lilien, MohamadAli Torkamani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30258v1)