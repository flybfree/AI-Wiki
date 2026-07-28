---
title: FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models
published: 2026-07-27T15:03:22Z
authors: Kaiyang Ye, Yuan Ge, Junxiang Zhang, Bei Li, Ziming Zhu, Haishu Zhao, Xiaoqian Liu, Chenglong Wang, Jingbo Zhu, Zhengtao Yu, Tong Xiao
url: http://arxiv.org/abs/2607.24522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models

## Abstract
While on-policy distillation (OPD) effectively addresses sparse rewards and exposure bias in large language model post-training, its extension to flow models remains underexplored. To this end, we propose Flow Continuous Trajectory Supervision (FlowCTS), which matches subsequent student and reference trajectories initialized from the same student-visited state. Using the integral relation between trajectories and velocity fields, we derive a temporally weighted velocity-matching upper bound and discretize it into practical objectives parameterized by the number of supervision steps. Under a multi-reference setup, single-state FlowCTS-OPD outperforms vanilla KL-based OPD with faster convergence. FlowCTS-OPD improves GenEval from 0.90 to 0.93, OCR from 0.90 to 0.92, and PickScore from 22.75 to 23.06, while outperforming a mixed-reward RL baseline across all target metrics. Further analysis reveals a clear temporal supervision mismatch in vanilla KL-based OPD arising from its auxiliary SDE transition kernels. Beyond on-policy setting,FlowCTS also consistently outperforms vanilla SFT , particularly on OCR, while increasing supervision steps exhibit a trade-off between richer trajectory information and greater optimization difficulty.

## Metadata
- **Published**: 2026-07-27T15:03:22Z
- **Authors**: Kaiyang Ye, Yuan Ge, Junxiang Zhang, Bei Li, Ziming Zhu, Haishu Zhao, Xiaoqian Liu, Chenglong Wang, Jingbo Zhu, Zhengtao Yu, Tong Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24522v1)