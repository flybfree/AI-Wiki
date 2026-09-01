---
title: Structured State Reconciliation for Human-AI Task Handover
published: 2026-08-28T22:14:59Z
authors: Kayleigh Bishop, Maria P. Stull, Breanne Crockett, Bradley Hayes
url: http://arxiv.org/abs/2608.28907v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structured State Reconciliation for Human-AI Task Handover

## Abstract
Task handover requires communicating enough current state for a successor to resume work, yet the relevant information is often divided between system records and human observations. System records can be precise and timestamped but only partially observe the task, while human reports capture intent and task knowledge that no log contains but are vulnerable to omission and memory error. We present a provenance-aware pipeline that converts task telemetry and human-authored reports into a shared typed task-state representation, aligns and reconciles their facts, detects conflicts, and generates structured handover reports. We evaluate the approach on 13 paired task states collected in a controlled spatial multitask environment, using task-grounded metrics that estimate the state-reconstruction cost a report would spare a hypothetical recipient and the misinformation burden it would impose. Reconciling both sources preserved greater estimated task-state utility than either the user report or telemetry alone. Relative to a direct end-to-end LLM given the same inputs, structured reconciliation maintained comparable estimated utility while incurring substantially less misinformation, and task-aware rendering retained utility more efficiently (per token) than exhaustive rendering. An exploratory content analysis further shows that human reports contain substantial strategic knowledge that lies outside state-focused metrics. These results support provenance-aware state reconciliation as a design pattern for safer AI-assisted handover.

## Metadata
- **Published**: 2026-08-28T22:14:59Z
- **Authors**: Kayleigh Bishop, Maria P. Stull, Breanne Crockett, Bradley Hayes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28907v1)