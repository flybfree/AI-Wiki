---
title: PatientAct: Theory-Grounded Mental Health Client Simulation
published: 2026-08-13T03:01:15Z
authors: Sahand Sabour, TszYam NG, Yaqian Chen, Guanqun Bi, Jialu Zhao, Minlie Huang
url: http://arxiv.org/abs/2608.12750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PatientAct: Theory-Grounded Mental Health Client Simulation

## Abstract
LLM-based simulated clients are increasingly used to train novice counselors, evaluate LLM therapists, and generate synthetic data. However, current simulators produce overly cooperative clients that disclose too readily, accept therapeutic reframes without resistance, and resolve core issues within a single session. We trace these issues to profiles that lack causal depth and behavioral mechanisms that treat all content as equally accessible. We present PatientAct, a framework for client simulation grounded in established clinical theories. Our profiles integrate the 5Ps clinical case formulation, providing causal depth without tying the design to any single therapeutic modality. During simulation, profiles include a dynamic memory layer in which items carry trust thresholds (e.g., symptoms are available early, whereas formative memories require a sustained therapeutic alliance). At each turn, the client's emotional reaction and behavior are modeled before generating a response. If the therapist approaches gated content, PatientAct expresses resistance in terms of quantity, content, and style rather than defaulting to cooperation or a single resistance pattern. We evaluate our framework on 40 clinical situations and demonstrate that it generates diverse profiles with high clinical plausibility. Moreover, PatientAct significantly outperforms the baselines, yielding substantial gains in resistance quality and behavioral realism. Our code and data will be publicly available via github.com/Sahandfer/PatientHub.

## Metadata
- **Published**: 2026-08-13T03:01:15Z
- **Authors**: Sahand Sabour, TszYam NG, Yaqian Chen, Guanqun Bi, Jialu Zhao, Minlie Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12750v1)