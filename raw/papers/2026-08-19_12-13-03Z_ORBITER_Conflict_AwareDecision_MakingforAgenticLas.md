---
title: ORBITER: Conflict-Aware Decision-Making for Agentic Last-Mile Delivery
published: 2026-08-19T12:13:03Z
authors: Mingzhao Li, Chenxi Liu, Yan Zhao, Hao Miao
url: http://arxiv.org/abs/2608.18846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ORBITER: Conflict-Aware Decision-Making for Agentic Last-Mile Delivery

## Abstract
Last-mile delivery aims to handle dynamically arriving orders with couriers while modeling complex spatial and temporal correlations. Recent learning-based methods model spatiotemporal dependencies among orders to predict courier service sequences, but leave next-order decision making unexplained. Describing the current delivery state in language allows LLMs to reason explicitly about the spatial, temporal, and behavioral cues behind an individual decision. As direct predictors, however, LLMs remain sensitive to task presentation and often produce unreliable decisions. To address these challenges, we introduce ORBITER, an agentic Order Arbiter for next-order decision-making in last-mile delivery. ORBITER models courier service through decision points, each containing the courier's spatiotemporal state and visible orders and exposing local trade-offs for modeling and verification. Fixed proposers rank the candidates, and a structured report identifies where their rankings disagree. The LLM uses task-specific tools to gather evidence on the leading alternatives, while an independent critic checks the resulting decision against that evidence. We conduct extensive evaluations on data in four cities, where ORBITER outperforms existing state-of-the-art baselines by up to 9.2% on average showing its effectiveness.

## Metadata
- **Published**: 2026-08-19T12:13:03Z
- **Authors**: Mingzhao Li, Chenxi Liu, Yan Zhao, Hao Miao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18846v1)