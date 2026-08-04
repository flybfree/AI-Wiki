---
title: Scoring Rules! Statistical and Strategic Alignment for Text Evaluation Metrics
published: 2026-08-02T18:10:01Z
authors: Shengwei Xu, Yuxuan Lu, Yifan Wu, Jason Hartline, Grant Schoenebeck
url: http://arxiv.org/abs/2608.01423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scoring Rules! Statistical and Strategic Alignment for Text Evaluation Metrics

## Abstract
Reference-based text evaluation metrics, which are widely used to assess natural language generation systems, score a candidate response by comparing it with a reference response. The reliability of an evaluation metric is usually judged by its statistical correlation with human ratings. However, as these metrics are increasingly used as optimization objectives, correlation alone is no longer sufficient: agents may strategically game the evaluation metric. We study this issue through two complementary notions of alignment. A metric is statistically aligned if it correlates with human ratings and strategically aligned if it resists perturbations that do not add task-relevant information. We make two contributions. First, we propose test principles for reference-based metrics consisting of human-rating correlation, degradation sensitivity, and manipulation robustness. These principles evaluate whether a metric agrees with human judgments, penalizes low-effort information loss, and resists strategic score inflation. Second, we develop a unified design framework for mutual-information-based metrics that decomposes existing and new metrics into four choices: information measure, estimation method, text representation, and prediction mechanism. Across peer review, summarization, and question answering, we find that strong human-rating correlation does not imply strategic alignment: LLM-as-a-Judge achieves high correlation but is susceptible to manipulation. In contrast, mutual-information-based metrics substantially improve manipulation robustness. Our framework also uncovers a new metric that achieves the strongest overall robustness in our experiments while remaining competitive on human-rating correlation.

## Metadata
- **Published**: 2026-08-02T18:10:01Z
- **Authors**: Shengwei Xu, Yuxuan Lu, Yifan Wu, Jason Hartline, Grant Schoenebeck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01423v1)