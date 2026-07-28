---
title: CALMRec: Causally Aligned Language Memory for Long-Horizon Recommendation
published: 2026-07-26T13:28:51Z
authors: Gengyu Zhan
url: http://arxiv.org/abs/2607.23647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CALMRec: Causally Aligned Language Memory for Long-Horizon Recommendation

## Abstract
Large language models (LLMs) can summarize heterogeneous user evidence in natural language, but current LLM recommenders often collapse enduring preferences, transient intent, and exposure-induced behavior into one profile. This makes recommendation vulnerable to feedback loops: repeated exposure is mistaken for preference, immediate clicks dominate delayed satisfaction, and fluent explanations need not reflect the ranking decision. We propose our method, a model-agnostic framework for long-horizon recommendation. Our method uses a frozen multimodal language model to convert item content and feedback into evidence-grounded semantic atoms, then maintains separate short-term, long-term, and exposure memories. Propensity-weighted updates reduce policy-induced exposure bias, while a conservative offline critic reranks candidates for delayed satisfaction under a behavior-support constraint. Explanations use only influential evidence atoms and are checked by counterfactual deletion. We provide an identification result and evaluate the framework in e-commerce-like, news-like, and short-video-like environments. Across ten seeds, our method improves discounted long-term value over the strongest alternative by 6.1%, 7.6%, and 6.7%, respectively. Twenty-seed paired ablations show significant value drops after removing propensity correction (0.739 +/- 0.191) or conservative support regularization (0.523 +/- 0.234). A frozen instruction language model also more than doubles semantic-atom NDCG over TF-IDF on a held-out paraphrase benchmark.

## Metadata
- **Published**: 2026-07-26T13:28:51Z
- **Authors**: Gengyu Zhan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23647v1)