---
title: Textual User Taste: Natural-Language User Context for Foundation-Model Recommender System at Scale
url: http://arxiv.org/abs/2609.35285v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_14-34-14Z_TextualUserTaste_Natural_LanguageUserContextforFou.md
generated_at: 2026-09-29 01:52
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Textual User Taste, a system deployed at Spotify scale that converts user listening behavior and interaction signals into structured natural-language taste profiles for foundation-model recommender systems. The authors demonstrate that these textual representations serve as an interpretable interface that complements traditional behavioral embeddings, yielding measurable improvements in future-track prediction and search ranking metrics when integrated into downstream personalization workflows.

## Key Takeaways
- The system generates structured natural-language profiles from diverse signals including listening behavior, interaction data, content metadata, and optional feedback, deploying them to millions of users while managing an end-to-end production lifecycle that encompasses prompt development, compression, optimization, and maintenance at industrial scale.
- Evaluation reveals that taste profiles carry independent predictive signal and, when combined with behavioral embeddings, improve Mean Reciprocal Rank by 0.6% for future-track prediction and NDCG@7 by 2.2% for search ranking, establishing their value as a complementary representation rather than a replacement for opaque embedding vectors.
- The profiles enable positive natural-language steering of recommendations but expose specific limitations regarding the model's handling of negation and short-term temporal adaptation, highlighting challenges in maintaining dynamic user context over time within foundation-model workflows.

## Context
As recommender systems increasingly integrate large language models, there is a growing need to bridge the gap between high-dimensional behavioral embeddings and the natural-language interfaces that LLMs natively process. This work addresses the interpretability

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35285v1)
