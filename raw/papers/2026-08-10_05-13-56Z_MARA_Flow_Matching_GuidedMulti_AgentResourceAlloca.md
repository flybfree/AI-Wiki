---
title: MARA: Flow-Matching-Guided Multi-Agent Resource Allocation for Computational Resource Efficient Learning
published: 2026-08-10T05:13:56Z
authors: Hanye Zhao, Muning Wen, Yong Yu, Weinan Zhang
url: http://arxiv.org/abs/2608.09130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MARA: Flow-Matching-Guided Multi-Agent Resource Allocation for Computational Resource Efficient Learning

## Abstract
Allocating limited computation among concurrent learning tasks is difficult when each task must reach a target loss before a deadline but its required training effort is unknown. Existing approaches combine online loss prediction with adaptive resource allocation, yet commonly treat computation as continuously divisible throughput. We instead study a practical setting in which tasks arrive over time and computation is provided by discrete nodes. This setting introduces both uncertain demand and constrained sequential decisions. We propose MARA, which predicts future loss trajectories with conditional flow matching and coordinates compute nodes through a cooperative multi-agent autoregressive policy. A potential-based progress reward supplies intermediate training feedback while preserving the undiscounted task-completion objective. Across in-distribution, reinforcement-learning, and vision workloads, flow matching reduces remaining-resource prediction error relative to weighted least squares. At the scheduler's training load, MARA completes 63.46% of tasks on average, 8.54 percentage points above strong baseline Learning with Adaptive Resource Allocation (LARA), and remains ahead under unseen heavier workloads.

## Metadata
- **Published**: 2026-08-10T05:13:56Z
- **Authors**: Hanye Zhao, Muning Wen, Yong Yu, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09130v1)