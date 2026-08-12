---
title: BREAD: Baseline-Referenced Explanations for Anomaly Diagnosis
published: 2026-08-11T07:16:06Z
authors: Jiaqi Qiu, Rob Goedhart, Jannis Kurtz, Inez M. Zwetsloot
url: http://arxiv.org/abs/2608.10587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BREAD: Baseline-Referenced Explanations for Anomaly Diagnosis

## Abstract
Artificial Intelligence (AI)-based prospective anomaly detection methods are increasingly deployed in high-dimensional and nonlinear settings. Among these approaches, AI-based statistical process monitoring (SPM) is widely used, providing a structured framework for prospective monitoring. Once an anomaly is detected, a diagnosis method is needed to identify the features driving the flagged observation away from normal behaviour. Traditional SPM diagnosis methods are typically designed for specific detection models and cannot be directly applied to AI-based methods. Model-agnostic explainable AI (XAI) offers a general framework for feature relevance explanation. However, existing methods suffer from scalability limitations or assign relevance to noise features, reducing diagnosis accuracy. We propose a scalable, baseline-referenced diagnosis method that uses both the anomalous observation and normal baseline information. We provide mathematical guarantees that under a mean-shift anomaly setting, the proposed method achieves higher faithfulness in detecting the features causing the anomaly compared to LIME. Simulation studies and a real-world case study validate the effectiveness of the proposed method and show that it generates more faithful and accurate diagnosis results for AI-based prospective anomaly detection methods.

## Metadata
- **Published**: 2026-08-11T07:16:06Z
- **Authors**: Jiaqi Qiu, Rob Goedhart, Jannis Kurtz, Inez M. Zwetsloot
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10587v1)