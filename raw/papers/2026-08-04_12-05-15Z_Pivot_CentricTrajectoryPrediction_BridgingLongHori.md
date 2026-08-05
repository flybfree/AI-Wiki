---
title: Pivot-Centric Trajectory Prediction: Bridging Long Horizons via Dynamical Guidance
published: 2026-08-04T12:05:15Z
authors: Xiucong Zhao, Jindong Tian, Hao Miao
url: http://arxiv.org/abs/2608.03521v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pivot-Centric Trajectory Prediction: Bridging Long Horizons via Dynamical Guidance

## Abstract
Forecasting precise future motion of surrounding agents is essential for reliable autonomous vehicles. However, as the demand for longer prediction horizons increases, existing endpoint-completion or iterative-refine methods increasingly struggle with weak guidance and compounding errors. To tackle the long-horizon prediction challenge, we propose Pivot-Centric Trajectory Prediction (PCTP). By introducing ``pivots'' and focusing on predicting pivot points along extended trajectories, we divide the long-term prediction task into short-term sub-tasks at various scales. Specifically, PCTP decouples the long-term trajectory predicting process into two processes: pivot prediction and pivot-based trajectory refinement. The pivot prediction process aims to utilize global map context and agent-to-agent interactions to identify these ``pivot points'', while the pivot-based trajectory refinement process focuses on local map details and refines the short-term trajectory based on predicted ``pivot points''. Compared with existing methods, PCTP provides more intermediate guidance while reducing compounding errors. Moreover, PCTP is a flexible approach that can be integrated into most state-of-the-art trajectory prediction models. Experimental results show that PCTP improves the prediction accuracy of leading models on both Argoverse I and Argoverse II datasets with minimal impact on model size. Specifically, PCTP combined with QCNet outperforms all published ensemble-free methods on the Argoverse II leaderboard at submission.

## Metadata
- **Published**: 2026-08-04T12:05:15Z
- **Authors**: Xiucong Zhao, Jindong Tian, Hao Miao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03521v1)