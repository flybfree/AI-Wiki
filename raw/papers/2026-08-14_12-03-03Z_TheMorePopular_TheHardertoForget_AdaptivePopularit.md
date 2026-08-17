---
title: The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning
published: 2026-08-14T12:03:03Z
authors: Anna Borisiuk, Andrey Savchenko, Alexander Panchenko, Elena Tutubalina
url: http://arxiv.org/abs/2608.14229v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning

## Abstract
Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts the retain penalty each epoch. Across three model families and two benchmarks, AdaPop leaks ~5x less forgotten content than competing methods under paraphrased queries and ~1.6x less under adversarial reformulations. We support our analysis with internal metrics: under our method, forget-set hidden states move further from the pre-unlearning model's states than under other methods, while retain-set representations remain close.

## Metadata
- **Published**: 2026-08-14T12:03:03Z
- **Authors**: Anna Borisiuk, Andrey Savchenko, Alexander Panchenko, Elena Tutubalina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14229v1)