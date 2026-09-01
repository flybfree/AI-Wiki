---
title: Item-Mean Surrogates: Why Richer Persona Data Fail to Improve LLMs as Human Surrogates
published: 2026-08-29T22:17:23Z
authors: Daehwan Ahn, Chengfeng Mao, Dokyun Lee
url: http://arxiv.org/abs/2608.29455v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Item-Mean Surrogates: Why Richer Persona Data Fail to Improve LLMs as Human Surrogates

## Abstract
LLMs are increasingly used as human surrogates, often on the premise that richer persona data could make them substitutes or exploratory tools for specific individuals. We test this premise across four datasets covering more than 400,000 participants and more than 6,000 survey items and experimental outcomes. LLMs perform well at the aggregate level: their average responses closely align with average human responses to the same items. But this success largely reflects predicting each item's average human response. Once each item's human mean is removed, LLM predictions explain only 3.05% of the remaining respondent-specific variation, far below the 53.6% human test-retest benchmark. Richer personas, model variants, and fine-tuning do not close this gap. In variance analyses, once item means are removed, the reliable remaining signal is person-by-item. It captures how a respondent departs from the mean on a particular item and is about 8.9x larger than the stable person effect. Persona data encode the respondent, but not this item-specific deviation. LLM responses also compress human response distributions, using less spread, fewer response categories, and distorted distributional shapes. We call this pattern item-mean surrogacy. Current LLM surrogates can approximate item averages, but not the distributions or respondent-specific deviations needed to replace individual humans. We propose four empirical tests for LLM-based human-surrogate claims.

## Metadata
- **Published**: 2026-08-29T22:17:23Z
- **Authors**: Daehwan Ahn, Chengfeng Mao, Dokyun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29455v1)