---
title: AHEAD: Advancing Multi-Class Label Aggregation with Interpretable Cross-Annotator Modeling
published: 2026-07-20T19:32:01Z
authors: Ju Chen, Sijia Xu, Jun Feng, Zhiqiang Gao, Zhengyi Yang
url: http://arxiv.org/abs/2607.18465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AHEAD: Advancing Multi-Class Label Aggregation with Interpretable Cross-Annotator Modeling

## Abstract
Crowdsourced labeling provides valuable labeled data for domains across natural language processing, computer vision, and video. Label aggregation aims to infer latent true labels from noisy and biased annotations, with the key lying in annotator reliability estimation. Despite promising progress, existing approaches struggle with one real-world bottleneck: most individual annotators label only a small subset of tasks, making accurate annotator estimation highly intractable. In this paper, we focus on the considerably more challenging multi-class label aggregation and propose AHEAD (cross-Annotator learning and High-confidEnce Annotator-guideD label aggregation), a cross-annotator learning framework that advances annotator reliability estimation by leveraging the population-level data. Specifically, AHEAD first learns high-dimensional cross-annotator contexts via a graph neural network, deriving multi-view, complementary annotator embeddings by aggregating individual-level annotator features with contextual information. These embeddings are then decoded into interpretable annotator-specific confusion matrices to fit the observed labels. We formulate a composite objective incorporating high-confidence annotators to alleviate the unsupervised training issues faced by prior models. Experiments on 10 real-world datasets spanning NLP, CV, Video, and Audio show that AHEAD substantially improves label accuracy, increasing average accuracy from 68.75% to 73.23%, with gains of up to 14.9% in the best case. Meanwhile, scalability experiments on the largest dataset further demonstrate the overall superiority of our method.

## Metadata
- **Published**: 2026-07-20T19:32:01Z
- **Authors**: Ju Chen, Sijia Xu, Jun Feng, Zhiqiang Gao, Zhengyi Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18465v1)