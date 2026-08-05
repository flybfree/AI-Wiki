---
title: Enhancing Tabular Learners with Context-Aware Semantic Embeddings
published: 2026-08-04T12:29:37Z
authors: Günther Schindler, Maximilian Schambach, Johannes Höhne
url: http://arxiv.org/abs/2608.03565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Tabular Learners with Context-Aware Semantic Embeddings

## Abstract
While modern tabular learners excel at capturing statistical patterns, they frequently operate in a semantic vacuum, treating textual features as discrete symbols, ignoring the rich semantics inherent in feature names or cell entries. We propose CASE (Context-Aware Semantic Embeddings), a novel framework that bridges the gap between the semantic understanding of Large Language Models (LLMs) and the statistical capabilities of tabular learners. Unlike existing methods that embed rows in isolation, CASE utilizes a contextualization strategy: we pre-fill the KV cache of a custom-trained Gemma 3-based Tabular Language Model with a representative sample of rows to establish a persistent anchor of the dataset's semantics. This ensures that generated row embeddings are dynamically contextualized, resolving semantic ambiguities and anchoring representations in domain-specific context. Our experiments across several benchmarks (CARTE, TextTab, and TabArena) demonstrate that CASE substantially improves the performance of tabular learners on semantically rich datasets, particularly in low-data regimes.

## Metadata
- **Published**: 2026-08-04T12:29:37Z
- **Authors**: Günther Schindler, Maximilian Schambach, Johannes Höhne
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03565v1)