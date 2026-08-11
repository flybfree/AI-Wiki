---
title: Unimodality-Promoting Regularized Learning for Ordinal Regression
published: 2026-08-08T22:55:31Z
authors: Ryoya Yamasaki
url: http://arxiv.org/abs/2608.08359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unimodality-Promoting Regularized Learning for Ordinal Regression

## Abstract
Ordinal regression, also called ordinal classification, is classification of ordinal data, in which the underlying target variable is categorical and considered to have a natural ordinal relation. Previous works have indicated that, in many real-world ordinal data, the conditional probability distribution (CPD) of the target variable given a value of the explanatory variable would be unimodal in a large domain of the explanatory variable and close to be unimodal even in a remaining domain. Therefore, unimodality-promoting regularized learning (UPRL), which promotes a predicted CPD closer to be unimodal with the aim of decreasing a prediction variance without inducing much bias for ordinal data of the unimodality, is promising to improve the prediction performance especially with small-size training data. In this study, we show that previous UPRL methods promote a predicted CPD to not only become closer to be unimodal but also have a larger scale (in other words, be smoother or less-confident). Therefore, we develop a novel method that more strictly reflects the idea of UPRL and evades a scale-related bias, and verify through experimental comparison that the unimodality-promotion indeed contributes to improve the prediction performance. Additionally, while our proposed UPRL method could perform better for smaller-scale data or with larger-size training data compared to a previous UPRL method, our analysis explains this experimental observation in terms of the presence or absence of an unexpected scale-related bias.

## Metadata
- **Published**: 2026-08-08T22:55:31Z
- **Authors**: Ryoya Yamasaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08359v1)