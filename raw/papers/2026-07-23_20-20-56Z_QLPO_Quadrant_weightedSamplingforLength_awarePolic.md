---
title: QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization
published: 2026-07-23T20:20:56Z
authors: Siwei Chen, Siqi Chen, Xupeng Miao, Bin Cui
url: http://arxiv.org/abs/2607.21793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization

## Abstract
Recent large reasoning models often develop long chain-of-thought responses during reinforcement learning (RL), resulting in high inference latency and deployment cost. Existing methods for response length control typically rely on explicit length penalties or additional control modules, which require careful tuning and may compromise reasoning quality. We propose Quadrant-weighted Sampling for Length-aware Policy Optimization (QLPO), a simple resampling-based variant of GRPO that introduces implicit length control without modifying the reward function. QLPO first over-generates candidate responses and then resamples the training group by preserving the empirical correct/incorrect ratio while favoring short correct responses and long incorrect responses. This reshapes the training distribution and implicitly encourages shorter model outputs. Across models ranging from 1.5B to 32B parameters, including both base models and strong reasoning models, QLPO consistently improves the accuracy-length trade-off. It reduces response length by 30% to 70% while preserving reasoning performance. These results suggest that structured resampling provides an effective and robust approach to efficient reasoning.

## Metadata
- **Published**: 2026-07-23T20:20:56Z
- **Authors**: Siwei Chen, Siqi Chen, Xupeng Miao, Bin Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21793v1)