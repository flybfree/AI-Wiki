---
title: Neighborhood-Aware Dual Biomedical Entity Linking
published: 2026-08-04T18:55:14Z
authors: Yicheng Tao, Jie Liu
url: http://arxiv.org/abs/2608.04144v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neighborhood-Aware Dual Biomedical Entity Linking

## Abstract
Biomedical entity linking grounds mentions in clinical and scientific text to entities in a curated knowledge base (KB) with ontological structure, which supports downstream applications such as literature-scale information extraction and patient-record normalization. The task has several challenges at once: the KB contains large numbers of entities, mentions are often ambiguous, and gold labels follow annotation conventions specific to each corpus. To address these challenges, we propose PILOT, a three-stage framework made up of neighborhood-aware retrieval, dual reranking, and score fusion. The retriever injects ontological structure from both the query and KB side, by reformulating mentions and pooling entity embeddings. The retrieved pool is then scored from two complementary views, one over surface forms and one over context, and fused together. PILOT achieves the state of the art on average across five widely-used benchmarks and remains efficient at inference.

## Metadata
- **Published**: 2026-08-04T18:55:14Z
- **Authors**: Yicheng Tao, Jie Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04144v1)