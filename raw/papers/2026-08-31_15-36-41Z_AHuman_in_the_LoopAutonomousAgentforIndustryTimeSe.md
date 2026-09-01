---
title: A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting
published: 2026-08-31T15:36:41Z
authors: Xiaoyu Tao, Mingyue Cheng, Ze Guo, Bokai Pan, Qi Liu, Shijin Wang, Enhong Chen
url: http://arxiv.org/abs/2608.30976v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting

## Abstract
Real-world time-series forecasting is rarely a one-shot model invocation: practitioners must formulate tasks, connect data and models, incorporate domain expertise, assess prediction plausibility, and communicate uncertainty. Specialized forecasting models provide strong numerical predictions but usually operate in fixed pipelines, while general-purpose large language model (LLM) agents often lack forecasting-specific checks, constraints, and stopping rules. We present CastClaw, a human-in-the-loop autonomous forecasting system built through forecasting-oriented harness engineering. CastClaw connects data, specialized models, analytical tools, user input, and a versioned execution record in one runtime. Users specify the target, horizon, constraints, and hypotheses in natural language. Starting from a supplied or model-generated forecast, CastClaw checks temporal patterns and user constraints; when evidence is missing, it retrieves context, runs an analysis or another model, or asks the user. It then keeps, revises, or escalates the result under explicit stopping conditions. The output contains the final forecast and an execution report recording inputs, evidence, actions, and revisions. In this five-dataset electricity-price setting, CastClaw reports the lowest point-estimate MSE and MAE among 16 baselines. A Nord Pool case demonstrates the inspectable workflow. CastClaw was also validated offline on provincial electricity-load data from North China covering January--June 2026.

## Metadata
- **Published**: 2026-08-31T15:36:41Z
- **Authors**: Xiaoyu Tao, Mingyue Cheng, Ze Guo, Bokai Pan, Qi Liu, Shijin Wang, Enhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30976v1)