---
title: Modeling Discourse Profiles in Climate Misinformation Discourse
published: 2026-10-17T06:15:44Z
authors: Ge Gao, Zhengyang Shan, Bryan A. Plummer, Margrit Betke, Derry Wijaya
url: http://arxiv.org/abs/2610.24489v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modeling Discourse Profiles in Climate Misinformation Discourse

## Abstract
Prior work on climate misinformation detection typically classifies individual comments or claims using text alone. This framing overlooks a key property of online climate discourse: misinformation is often produced, reinforced, and sustained through recurring rhetorical patterns that reappear across comments and threads. Using a large-scale TikTok climate discourse dataset, we construct discourse profiles by clustering climate-related comments into recurring rhetorical patterns. We then incorporate these profiles into fine-grained climate misinformation classifiers using a late-fusion architecture. Under video-disjoint evaluation across three training seeds, discourse-profile-aware models significantly improve macro-F1 over text-only baselines for bag-of-words, TF-IDF, and MPNet representations. RoBERTa-large exhibits a positive mean improvement but substantially greater variability, and the difference is not statistically significant. Beyond classification, our results show discourse profiles shape misinformation reception and propagation. Discourse-profile-conditioned language model agents exhibit misinformation acceptance patterns aligned with profile-level misinformation prevalence in ClimateDisc, and the relationship between misinformation prevalence and engagement persistence differs across dominant discourse profiles.

## Metadata
- **Published**: 2026-10-17T06:15:44Z
- **Authors**: Ge Gao, Zhengyang Shan, Bryan A. Plummer, Margrit Betke, Derry Wijaya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24489v1)