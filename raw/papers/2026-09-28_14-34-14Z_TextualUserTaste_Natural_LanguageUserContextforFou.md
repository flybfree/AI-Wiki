---
title: Textual User Taste: Natural-Language User Context for Foundation-Model Recommender System at Scale
published: 2026-09-28T14:34:14Z
authors: Ghazal Fazelnia, Paul Gigioli, Eliza Klyce, Sharon Zheng, Katie Zelvin, Ye Myat Thein, Anurag Deshpande, Seda Davtyan, Kate Remeika, Maya Hristakeva, Erik Franco, Karen Banzon, Peng Ge, Jacqueline Wood, Nandini Singh, David Murgatroyd, Mounia Lalmas, Yves Raimond, Andreas Damianou
url: http://arxiv.org/abs/2609.35285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Textual User Taste: Natural-Language User Context for Foundation-Model Recommender System at Scale

## Abstract
Foundation model recommender systems require user context that can be consumed by large language models, reasoned over, and refined through natural-language interaction. Traditional behavioral embedding vectors remain highly effective for retrieval and ranking, but they are opaque to users and not natively expressed for language model workflows. We present Textual User Taste, a system that generates structured natural-language taste profiles from listening behavior, interaction signals, content metadata, and optional user feedback, and deploys them to millions of Spotify users. We describe the end-to-end production lifecycle required to generate, evaluate, optimize, and maintain these representations at industrial scale, including prompt development and compression, user steering, and integration with downstream personalization systems. Because no unique ground-truth taste profile exists, we introduce a multi-faceted evaluation framework to evaluate taste profiles as a production representation: they carry user-specific predictive signal independently, and when integrated with behavioral embeddings, improve MRR by 0.6% for future-track prediction and NDCG@7 by 2.2% for search ranking. Our evaluation also reveals that taste profiles support positive natural-language steering, while exposing important limitations, including challenges with negation and short-term temporal adaptation. These findings position taste profiles not as replacements for behavioral embeddings, but as an interpretable and steerable interface between evolving user context and foundation-model recommender systems.

## Metadata
- **Published**: 2026-09-28T14:34:14Z
- **Authors**: Ghazal Fazelnia, Paul Gigioli, Eliza Klyce, Sharon Zheng, Katie Zelvin, Ye Myat Thein, Anurag Deshpande, Seda Davtyan, Kate Remeika, Maya Hristakeva, Erik Franco, Karen Banzon, Peng Ge, Jacqueline Wood, Nandini Singh, David Murgatroyd, Mounia Lalmas, Yves Raimond, Andreas Damianou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35285v1)