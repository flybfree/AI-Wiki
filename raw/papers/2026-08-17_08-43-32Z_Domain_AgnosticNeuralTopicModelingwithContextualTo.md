---
title: Domain-Agnostic Neural Topic Modeling with Contextual Token-Level Semantic Graph Representation
published: 2026-08-17T08:43:32Z
authors: Seung-Won Seo, Won Ik Cho, Yongmin Yoo
url: http://arxiv.org/abs/2608.16269v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Domain-Agnostic Neural Topic Modeling with Contextual Token-Level Semantic Graph Representation

## Abstract
Recent advances in neural topic models with pre-trained language models (PLMs) have achieved strong performance by leveraging general-domain pre-training, yet their topic interpretability often degrades on specialized corpora. This limitation primarily stems from the geometry of the embedding space, where domain-specific terms unseen during pre-training collapse into an indistinguishable region, and neither domain-specific re-training, word-level graph enrichment, nor parameter-efficient fine-tuning can restructure this space without inheriting the capacity ceiling of the underlying encoder. Our key insight is that a learnable graph layer operating on token-level PLM embeddings can acquire corpus-specific semantic structure that the frozen encoder lacks, because token-level graphs preserve document-local context that word-level representations discard and joint optimization with the topic objective reshapes embedding geometry directly from target-domain evidence. We instantiate this insight as DARTopic, a domain-agnostic framework that constructs token-level semantic graphs from frozen PLM embeddings and jointly trains a GNN encoder with topic inference. Across three benchmarks spanning general, biomedical, and legal domains, DARTopic consistently outperforms strong baselines in topic coherence and document clus- tering without any encoder fine-tuning, while demonstrating robustness to PLM choice and favorable runtime efficiency over fine-tuning based alternatives.

## Metadata
- **Published**: 2026-08-17T08:43:32Z
- **Authors**: Seung-Won Seo, Won Ik Cho, Yongmin Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16269v1)