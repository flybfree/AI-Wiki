---
title: Reproducing Transparent and Scrutable Recommendations: Exploring Open-Weight Models via Natural-Language User Profiles
published: 2026-09-17T07:36:34Z
authors: Noah Mamié, Laurin van den Bergh
url: http://arxiv.org/abs/2609.19831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reproducing Transparent and Scrutable Recommendations: Exploring Open-Weight Models via Natural-Language User Profiles

## Abstract
In this reproducibility study, we investigate the transparency and scrutability of recommender systems enhanced by incorporating generated natural-language user profiles that represent user preferences. The original paper explores the synthesis of user profiles from raw user-generated review text across domains such as movies and accommodations (Amazon Movies & TV, TripAdvisor). Crucially, these natural-language user profiles enable direct user interaction and intervention, allowing users to customize recommendations by correcting misattributed preferences or addressing cold-start settings. We successfully reproduce the core findings of the original study. Additionally, we extend the evaluation by conducting systematic context ablation experiments, multi-seed stability across five distinct random seeds to establish statistical reliability, and a mechanistic interpretability analysis using the nnsight framework to probe internal model representations under counterfactual profile perturbations. Our findings verify the original paper's claim that User Profile Recommendation (UPR) achieves competitive performance under its test-set reranking protocol and makes recommendations more transparent. Perturbing the natural-language profiles does change predictions, but it shifts predicted ratings uniformly across genres with no detectable genre-selective effect, leaving rankings unchanged even under direct activation steering. We trace this back to the rating-regression objective rather than the profile interface, with ranking-objective models clearly exceeding in this task.

## Metadata
- **Published**: 2026-09-17T07:36:34Z
- **Authors**: Noah Mamié, Laurin van den Bergh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19831v1)