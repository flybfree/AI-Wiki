---
title: Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework
published: 2026-09-18T07:38:58Z
authors: Delun Kong, Wanyun Ling, Chenxi Liu, Ziyue Li
url: http://arxiv.org/abs/2609.21425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing the Evidence Behind Zero-Shot Time-Series Forecasting: A Source-First Taxonomy and Audit Framework

## Abstract
Zero-shot time-series forecasting (TSF) is often described as forecasting without target-specific parameter updates, but that training-status condition does not specify what evidence the system may use. A frozen language model prompted with serialized values, a time-series model pretrained on broad forecasting corpora, and a retrieval-augmented forecaster may all satisfy the no-update condition while drawing on different transferable evidence. This paper argues that zero-shot TSF should therefore be governed as an evidence-access claim. We propose a source-first taxonomy that separates three primary evidence sources---frozen LLM prior reuse, parametric time-series pretraining, and retrieval-augmented external memory---from the architectures that implement them. After the source is identified, four additional audit questions remain: task interface, forecast object and scoring, prediction-time context, and resource budget. The resulting agenda is to make zero-shot leaderboards auditable by reporting evidence boundaries and interface assumptions alongside scores, so that benchmark progress reflects transferable forecasting capability rather than undisclosed changes in context, memory, or budget.

## Metadata
- **Published**: 2026-09-18T07:38:58Z
- **Authors**: Delun Kong, Wanyun Ling, Chenxi Liu, Ziyue Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21425v1)