---
title: Structuring Semantic Embeddings for Principle Evaluation: A Prototype-Guided Contrastive Learning Approach
published: 2026-08-15T13:19:25Z
authors: Che Shen, Junwei Su, Lingpeng Kong, Chuan Wu
url: http://arxiv.org/abs/2608.15224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structuring Semantic Embeddings for Principle Evaluation: A Prototype-Guided Contrastive Learning Approach

## Abstract
Reliable post-hoc evaluation asks whether already generated text satisfies a target criterion after generation. In this paper we study a focused frozen-embedding setting using principle-evaluation proxy tasks: toxicity detection, fine-grained emotion categorization, and ordinal review rating. General-purpose text embeddings are widely deployed for such tasks, but broad semantic similarity can place semantically similar yet task-distinct examples in overlapping regions of the representation space. We introduce Prototype-Guided Contrastive Learning (PGCL), a prototype-guided geometric regularization module built on top of frozen text embeddings. The module combines a semantic stream, a prototype-anchor attention stream, supervised contrastive learning, offset-based prototype-margin regularization, and stream regularization to produce a compact task-adapted representation without updating the base encoder. Controlled experiments show that PGCL improves over raw frozen embeddings on all three datasets and gives the clearest direct-baseline margin on AmazonReviews, while remaining competitive with strong direct frozen metric-learning baselines on GoEmotions and ToxicComment. We also add supervised residual-adapter, encoder-LoRA, full fine-tuning, objective ablation, sensitivity, and fully logged few-shot LLM protocol diagnostics to define the boundary of the claim. The theoretical analysis is revised as a sufficient-condition account for prototype-margin behavior under explicit assumptions in the prototype-mapping space, rather than as an unconditional training or final-embedding separation guarantee.

## Metadata
- **Published**: 2026-08-15T13:19:25Z
- **Authors**: Che Shen, Junwei Su, Lingpeng Kong, Chuan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15224v1)