---
title: Secrets Everywhere: Auditing Memorization in Mobility Prediction Models
published: 2026-08-03T10:47:56Z
authors: Anne Josiane Kouam, Hristo Boyadzhiev, Konrad Rieck
url: http://arxiv.org/abs/2608.02052v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Secrets Everywhere: Auditing Memorization in Mobility Prediction Models

## Abstract
Human mobility prediction models, which forecast the next location in a user's trajectory, are increasingly deployed in urban analytics, navigation, and personalized services. Yet, little is known about their potential to memorize and expose sensitive user trajectories from training data. While memorization has been extensively studied in language models, mobility prediction poses unique challenges: training sequences encode human behavior at various spatial and temporal scales, creating privacy risks at different granularities.   In this paper, we conduct the first systematic audit of memorization in mobility prediction models. While prior work has shown that privacy leaks can arise from such models, we systematically assess and quantify memorization risks at scale. We identify key challenges, including the lack of a randomness space, the multi-scale structure of trajectories, and user-specific behavioral diversity. To address these challenges, we introduce a framework to quantify mobility memorization at different levels of granularity: individual locations, anchor pairs, and subtrajectory segments. We also develop user-grounded reference sets to assess how likely a model is to prefer training data over realistic alternatives. Our evaluation across multiple models and datasets reveals pervasive memorization patterns that correlate with user regularity and increase the risk of data extraction at inference time. Our findings call for mandatory privacy auditing in mobility prediction models.

## Metadata
- **Published**: 2026-08-03T10:47:56Z
- **Authors**: Anne Josiane Kouam, Hristo Boyadzhiev, Konrad Rieck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02052v1)