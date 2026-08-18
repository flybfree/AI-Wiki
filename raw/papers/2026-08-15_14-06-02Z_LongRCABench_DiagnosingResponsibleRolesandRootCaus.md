---
title: LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures
published: 2026-08-15T14:06:02Z
authors: Yunfei Zhang, Boyu Feng, Changhua Pei, Zexin Wang, Zhihuang Peng, Xinlong Liu, Hengyue Jiang, Difeng Ma, Jiayi Zhang, Yongzhou Yao, Yanan Zhao, Fei Sun, Yintong Huo, Zhaoyang Liu, Jingjing Li, Gaogang Xie, Dan Pei
url: http://arxiv.org/abs/2608.15242v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures

## Abstract
When a long-horizon agent execution fails, outcome-level evaluation reveals the unsuccessful result but not where the decisive error entered the trajectory. Developers must then inspect the full execution to identify the responsible role and localize the earliest decisive root-cause step. Existing failure-attribution benchmarks largely focus on shorter traces, leaving diagnosis across hundreds of recorded steps underexplored. We introduce LongRCA Bench, comprising 1,140 failed trajectories across five domains without injected errors. It provides independently scored human labels for the responsible role and earliest decisive root-cause step. The median trajectory contains 145 steps, and the strongest baseline reaches only 13.2% exact root-step accuracy. We further present Root-Cause Trajectory Attribution (RCTA), a training-free method that retrieves candidate error steps from segment summaries and traces them to available earlier handoff instructions. Using the same backbone, benchmark instances, and scoring protocol, RCTA reaches 51.1% responsible-role accuracy and 24.1% exact root-step accuracy. These results highlight the need to evaluate responsible-role attribution and exact root-step localization as separate targets in long-trajectory failure diagnosis.

## Metadata
- **Published**: 2026-08-15T14:06:02Z
- **Authors**: Yunfei Zhang, Boyu Feng, Changhua Pei, Zexin Wang, Zhihuang Peng, Xinlong Liu, Hengyue Jiang, Difeng Ma, Jiayi Zhang, Yongzhou Yao, Yanan Zhao, Fei Sun, Yintong Huo, Zhaoyang Liu, Jingjing Li, Gaogang Xie, Dan Pei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15242v1)