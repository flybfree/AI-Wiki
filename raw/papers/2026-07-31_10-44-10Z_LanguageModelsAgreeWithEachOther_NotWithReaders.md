---
title: Language Models Agree With Each Other, Not With Readers
published: 2026-07-31T10:44:10Z
authors: Kazuki Nakayashiki, Keisuke Watanabe
url: http://arxiv.org/abs/2607.29274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language Models Agree With Each Other, Not With Readers

## Abstract
Claims that language models homogenise are usually measured against human judgements collected for the study, which makes the human side an artifact of the design: a crowdworker given the model's instruction is running the model's prompt. We measure convergence against a human reference nobody built for the purpose -- 2,523 reader mark sets across 120 web documents, produced by people highlighting for their own reasons on a platform where the overlay of others' marks is off by default.   Agreement is the overlap between two size-matched sentence sets minus the overlap expected when each is resampled within its own depth-and-length bands. The null's calibration is demonstrated, not asserted: every pair involving a random baseline lands within 0.006 of zero. On the median document each party names 14 sentences of 70; two readers share 4.1 and two models 8.7.   Across 18 model arms spanning 11 vendors, 3 countries and both weight regimes, the median of 153 model pairs is +0.093 against a human yardstick of +0.040, and 99 sit entirely above the human interval. Two frontier models from rival labs reach +0.203, twice what GPT-4o agrees with itself on a second call. The effect is not determinism, prompt wording, procedure, vendor or routing, and it is graded: the smallest models agree at the human level. No model agrees with readers detectably more than a reader does, and at equal depth and length no surface feature separates their choices.   The multiples are procedure-dependent and the ordering is not: models are cut to their sharpest set while a reader's is a random draw from what they marked, and blunting the models alike halves the gap without closing it. Tested out of sample on four models released after this analysis, against predictions fixed beforehand, none clears the human interval. A population simulated from several models is not several populations.

## Metadata
- **Published**: 2026-07-31T10:44:10Z
- **Authors**: Kazuki Nakayashiki, Keisuke Watanabe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29274v1)