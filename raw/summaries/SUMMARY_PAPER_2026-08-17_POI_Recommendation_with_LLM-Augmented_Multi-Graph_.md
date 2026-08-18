---
title: POI Recommendation with LLM-Augmented Multi-Graph Learning and Contrastive Alignment
url: http://arxiv.org/abs/2608.16407v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_11-01-12Z_POIRecommendationwithLLM_AugmentedMulti_GraphLearn.md
generated_at: 2026-08-17 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LLM-MGCL, a multi-graph neural network that augments LightGCN with semantic and geographic item graphs to improve POI recommendation. Experiments on Yelp Multimodal Recommendation Dataset show Recall@20 up 52% and NDCG@20 up 64.8% over LightGCN while matching SGL performance.

## Key Takeaways
- The semantic graph built from LLM-generated photo summaries and keywords provides rich item knowledge that fills gaps for cold-start items.
- Geographic graph using Haversine distances adds spatial context, enabling better alignment of nearby points.
- Cross-view contrastive alignment is the main contributor to gains, with best results when all three graphs are combined.

## Context
Graph neural networks dominate POI recommendation but face cold-start challenges. Incorporating external knowledge via LLM embeddings offers a promising way to enrich item representations beyond interaction data.

## Implications
Practitioners can leverage LLM-derived item semantics and location data to build more robust recommendation systems that handle sparse interactions. This approach may set new standards for multimodal graph learning in real-world services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16407v1)
