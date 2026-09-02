---
title: Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs
published: 2026-09-01T05:15:59Z
authors: Lu Cheng
url: http://arxiv.org/abs/2609.00738v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs

## Abstract
Inference-time search with large language models (LLMs) often concentrates on a small set of structurally or semantically similar trajectories, leaving alternatives underexplored---a failure mode we call \textit{reasoning basin collapse}. We introduce BASIN, a training-free, structure-aware selection method that groups reasoning states into basins and penalizes repeated visits to the same strategy, thereby reallocating search across genuinely distinct reasoning paths under a fixed compute budget. Under matched inference budgets, BASIN improves over Tree of Thoughts (ToT) by up to $+22$pp on Game of 24 and $+6.7$pp on MuSR. A quality-aware variant, QA-BASIN, further improves robustness by preserving high-quality basins when unconditional diversification over-explores. To explain when basin-aware selection helps, we introduce the redundancy gap $Δ$, which measures how differently search concentrates for correct versus incorrect predictions: standard ToT often operates near $Δ\approx 0$, while BASIN consistently shifts $Δ$ positive. More broadly, BASIN suggests structure-aware selection as a simple and general approach to improving inference-time reasoning. Code can be found at https://github.com/GitHubLuCheng/basin.

## Metadata
- **Published**: 2026-09-01T05:15:59Z
- **Authors**: Lu Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00738v1)