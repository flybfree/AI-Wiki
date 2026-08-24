---
title: CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting
published: 2026-08-21T06:29:52Z
authors: Zixi Zhu, Jiayuan Su, Jian Zhang, Yu Lin, Hongwei Wang
url: http://arxiv.org/abs/2608.20771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting

## Abstract
Search Agents face a severe reliability crisis during reinforcement learning (RL) fine-tuning. Heuristic Top-K retrieval often causes critical evidence loss or noise inclusion, while over-confidence induced by progressive RL leads to hallucinated answers and redundant searches.   To build highly reliable agents, we introduce Conformal Prediction (CP) and propose Conformalized Agentic Search (CAS). This framework establishes reliability guarantees on both the retrieval and training sides: on the retrieval side, an Adaptive Prediction Set (APS), a specific CP realization, translates statistical coverage into dynamic document truncation to construct prediction sets that are adaptive in size; on the training side, Adaptive Conformal Inference (ACI), a dynamic CP algorithm, dynamically constructs prediction sets with controllable coverage to quantify answer confidence, which is then used to penalize low-confidence trajectories within the Group Relative Policy Optimization (GRPO) objective, ensuring the model learns only from reliable ones.   Experiments across single-hop and multi-hop QA datasets demonstrate that our framework significantly improves reasoning accuracy while drastically reducing redundant tool invocations, establishing a highly reliable and efficient agent paradigm. Our code is available at https://github.com/S1llyBird/CAS.

## Metadata
- **Published**: 2026-08-21T06:29:52Z
- **Authors**: Zixi Zhu, Jiayuan Su, Jian Zhang, Yu Lin, Hongwei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20771v1)