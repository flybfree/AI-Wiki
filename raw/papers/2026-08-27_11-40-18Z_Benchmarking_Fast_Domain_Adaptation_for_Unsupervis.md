---
title: Benchmarking_Fast_Domain_Adaptation_for_Unsupervised_Speech_Units
published: 2026-08-27T11:40:18Z
authors: Robin San Roman, Manel Khentout, Tu Anh Nguyen, Paul Michel, Yossi Adi, Emmanuel Dupoux
url: http://arxiv.org/abs/2608.26992v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking_Fast_Domain_Adaptation_for_Unsupervised_Speech_Units

## Abstract
Representation learning has attracted great atten- tion and managed to reach good performances as a pretraining method for downstream tasks or as a first step towards unsu- pervised speech modeling. Yet, little is known about how such methods deal with out-of-domain speech and how could they be adapted in a few shot to new domains. This is important especially for accented speech where one observes a long tail of accents that diverge from the standard ones. We introduce ABX- Accent, a benchmark based on the AESRC dataset that features 10 different accents of English. It includes a small (< 10 hours) unlabelled training set in each of the accents and adaptations of the Zero Resources Challenge ABX evaluation metrics to each of the accents. We illustrate this benchmark with a baseline model that uses adaptive domain normalization to fine tune a pretrained Contrastive Predictive Coding model on the accents. This method is first developed on LibriSpeech using a male/female split. When applied to the new benchmark, the proposed method yields a relative improvement of 23.6% on across-speaker ABX scores on average compared to non adapted models. The data and metrics will be open sourced upon paper acceptance

## Metadata
- **Published**: 2026-08-27T11:40:18Z
- **Authors**: Robin San Roman, Manel Khentout, Tu Anh Nguyen, Paul Michel, Yossi Adi, Emmanuel Dupoux
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26992v1)