---
title: DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes
published: 2026-07-27T14:55:04Z
authors: Jiahao Xie, Zhongbin Guo, Qianle Wang, Ruiqi Lu, Dongling Xiao, Wanxuan Sun, Cheng Yang
url: http://arxiv.org/abs/2607.24516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes

## Abstract
While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed. We formulate data construction as a systematic mixture-optimization problem and turn it into a reproducible engineering discipline by decoupling the mixture into two orthogonal sub-problems: inter-class ratios across capabilities and intra-class ratios within a category. For inter-class allocation, we use a single-variable iterative search; for intra-class composition, we apply a multidimensional, dataset-level assessment scoring Quality and Difficulty, and formulate selection as a constrained convex optimization with a diversity objective. The DecoupleMix framework delivers two critical capabilities: guiding what data to collect next and rendering dataset validation a controlled, attributable experiment. Experiments show our approach consistently surpasses heuristic baselines. Moreover, optimal ratios discovered on small-scale proxies transfer seamlessly to larger scales without retuning. Using 80B additional multimodal continue-pretraining tokens, our VLM is competitive with strong open-source models trained with substantially larger multimodal budgets.

## Metadata
- **Published**: 2026-07-27T14:55:04Z
- **Authors**: Jiahao Xie, Zhongbin Guo, Qianle Wang, Ruiqi Lu, Dongling Xiao, Wanxuan Sun, Cheng Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24516v1)