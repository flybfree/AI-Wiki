---
title: ReasonCast: Towards Explainable Time Series Forecasting with Reasoning
published: 2026-08-03T08:21:07Z
authors: Seunghan Lee, Jun Seo, Jaehoon Lee, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
url: http://arxiv.org/abs/2608.01875v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReasonCast: Towards Explainable Time Series Forecasting with Reasoning

## Abstract
Most time series (TS) models are specialized for a single task, either understanding (i.e., returning text answers about a TS) or generation (i.e., returning a numeric forecast). Only recently have unified models begun to handle the two within a single architecture. Even these models, however, produce the two outputs as task-separated paths and cannot predict a series and explain why that prediction arises within a single coherent response. In this paper, we argue for a task-fused model that jointly produces 1) prediction (generation) and 2) selfexplanation (understanding), thereby integrating 1) numerical TS forecasting and 2) interpretable text reasoning within a single response. To enable the systematic study of this capability, we present both a benchmark and a recipe that jointly address the two tasks. The benchmark, ReasonTS-Bench, identifies five fundamental patterns underlying TS and enables the joint evaluation of both tasks. ReasonCast, our recipe for finetuning any LLM to perform both tasks jointly, yields a model that generates a reasoning chain and a forecast together in a single autoregressive pass. Extensive experiments show that ReasonCast outperforms both LLMs and TS models on prediction accuracy while producing verifiable, causal reasoning. Code is available at: https://github.com/seunghan96/reasoncast.

## Metadata
- **Published**: 2026-08-03T08:21:07Z
- **Authors**: Seunghan Lee, Jun Seo, Jaehoon Lee, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01875v1)