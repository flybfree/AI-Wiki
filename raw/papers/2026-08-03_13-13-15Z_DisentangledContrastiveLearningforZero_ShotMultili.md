---
title: Disentangled Contrastive Learning for Zero-Shot Multilingual Dense Retrieval
published: 2026-08-03T13:13:15Z
authors: Chao Huang, Yufeng Chen, Changhao Guan, Guang Yang, Dongze Chen, Kaiyu Huang
url: http://arxiv.org/abs/2608.02189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangled Contrastive Learning for Zero-Shot Multilingual Dense Retrieval

## Abstract
Multilingual dense retrieval aims to handle queries and documents across different languages based on a unified retriever model. The challenge lies in enabling robust retrieval transfer to low-resource languages where annotated retrieval data is often scarce. Although previous studies transfer high-resource supervision to low-resource languages in multilingual semantic representation learning, the shared representation often entangles semantic and linguistic features, which may interfere with optimizing semantic relevance for retrieval. Different from existing methods that focus on learning language-agnostic semantic features under such entanglement, we propose a disentangled contrastive learning~(DCL) method for multilingual dense retrieval by separating multilingual representations into semantic and linguistic subspaces. Specifically, we design disentangled optimization objectives based on hierarchical semantic alignment and language debiasing contrastive learning. By aligning retrieval-relevant semantics across languages at both sentence and token levels while capturing language-specific variations in the linguistic subspace, these objectives reduce language-induced interference in semantic matching. We jointly optimize them with the retrieval objective to facilitate stable zero-shot transfer from English supervision to multilingual dense retrieval. Extensive experiments on mMARCO and MIRACL show that our method consistently outperforms several strong baselines, demonstrating its effectiveness and generalization ability.

## Metadata
- **Published**: 2026-08-03T13:13:15Z
- **Authors**: Chao Huang, Yufeng Chen, Changhao Guan, Guang Yang, Dongze Chen, Kaiyu Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02189v1)