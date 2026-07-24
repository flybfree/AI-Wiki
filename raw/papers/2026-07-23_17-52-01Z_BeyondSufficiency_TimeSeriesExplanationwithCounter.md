---
title: Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity
published: 2026-07-23T17:52:01Z
authors: Hongnan Ma, Yiwei Shi, Mengyue Yang, Weiru Liu
url: http://arxiv.org/abs/2607.21573v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity

## Abstract
Faithful explanations of time-series classifiers should identify subsequences that are not only sufficient to preserve a black-box model's prediction, but also necessary for maintaining it. However, existing sufficiency-oriented methods can assign high importance to spurious subsequences that support the prediction without being essential to the model's decision. We introduce \textbf{TimePNS}, a necessity-aware framework for time-series explanation. Inspired by Pearl's counterfactual notion of necessity, TimePNS assesses whether a temporal factor is necessary by intervening on it and measuring whether the original prediction is disrupted. The framework adopts a two-stage design. Stage I learns an identifiable causal generative process together with a sufficiency-oriented explanation mask. Stage II performs counterfactual interventions on temporal factors to derive necessity signals, which supervise a temporal gate that refines the initial explanation by suppressing non-essential components and emphasizing counterfactually necessary ones. Experiments on synthetic and real-world time-series benchmarks show that TimePNS more accurately identifies decision-critical subsequences and consistently improves sufficiency-necessity trade-offs over strong baselines.

## Metadata
- **Published**: 2026-07-23T17:52:01Z
- **Authors**: Hongnan Ma, Yiwei Shi, Mengyue Yang, Weiru Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21573v1)