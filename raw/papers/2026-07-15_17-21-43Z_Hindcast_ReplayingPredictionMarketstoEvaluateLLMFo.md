---
title: Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters
published: 2026-07-15T17:21:43Z
authors: Xiao Ye, Jacob Dineen, Evan Zhu, Shijie Lu, Kevin Song, Ben Zhou
url: http://arxiv.org/abs/2607.14051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters

## Abstract
Forecasters are evaluated by backtesting, which replays resolved questions and grades the probability the system would have assigned before the outcome was known. For LLMs, two channels leak the answer into this test. A model that retrieves can surface reports written after the event, turning forecasting into a lookup, and each new model is trained on data closer to the event, so a question that lay in the future for last year's models sits inside this year's training data. Either way, the test grades recall while claiming to grade foresight. We introduce Hindcast, which closes both leaks by grading a model as if it stood at a chosen past date $t_0$, before the outcome existed in either channel. Hindcast replays resolved Polymarket prediction markets against a frozen snapshot of public Reddit, lets the model read only posts written before $t_0$, and scores each forecast against both what happened and the market's own price at $t_0$, itself a human forecast made from the same past information. Because the cutoff is set per market and the snapshot never changes, the evaluation re-runs on new markets as models improve, without going stale. Once the leak is closed, retrieval still helps most models, but only where Reddit discussed the event beforehand. Where the archive carried only speculation, retrieval hurts.

## Metadata
- **Published**: 2026-07-15T17:21:43Z
- **Authors**: Xiao Ye, Jacob Dineen, Evan Zhu, Shijie Lu, Kevin Song, Ben Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14051v1)