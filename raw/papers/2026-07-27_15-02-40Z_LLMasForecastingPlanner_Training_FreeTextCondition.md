---
title: LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models
published: 2026-07-27T15:02:40Z
authors: Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen, Dai Do, Hung Le
url: http://arxiv.org/abs/2607.24892v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM as Forecasting Planner: Training-Free Text Conditioning for Time-Series Foundation Models

## Abstract
Text-conditioned time-series forecasting predicts a series from both its numerical history and natural-language context, allowing forecasts to account for events and constraints that the past alone cannot reveal. This requires both reliable numerical forecasting and the ability to interpret contextual information. Time-series foundation models (TSFMs) provide strong numerical forecasts, while large language models (LLMs) can reason over text, but combining their strengths remains challenging because asking an LLM to generate or revise forecast values directly can distort the temporal structure captured by the TSFM. We instead formulate forecasting as a planning problem over TSFM-generated trajectories. The frozen TSFM acts as a simulator that proposes numerical continuations, while the LLM acts as a policy and value function that guides candidate selection and evaluates completed trajectories against the context. We instantiate this as \rc{} (\textbf{L}LM \textbf{A}s \textbf{F}orecasting \textbf{P}lanner), a training-free framework that bridges the modality gap without retraining either model, using Monte Carlo tree search (MCTS) over the forecast horizon with a \emph{Ranker} LLM as policy and a \emph{Judge} LLM as value function. Experiments on Context-is-Key and Time-MMD across two TSFM backbones (Chronos and TimesFM) and four LLMs show that \rc{} delivers consistent improvements across model choices, supporting sequential search as an effective training-free approach to text-conditioned forecasting.

## Metadata
- **Published**: 2026-07-27T15:02:40Z
- **Authors**: Huu Hiep Nguyen, Dung Nguyen, Minh Hoang Nguyen, Dai Do, Hung Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24892v1)