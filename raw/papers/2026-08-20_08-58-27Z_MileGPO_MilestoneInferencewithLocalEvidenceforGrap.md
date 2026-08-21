---
title: MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents
published: 2026-08-20T08:58:27Z
authors: Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu
url: http://arxiv.org/abs/2608.19803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents

## Abstract
Credit assignment is challenging in long-horizon agentic reinforcement learning, where supervision often comes only from final rewards. Existing methods refine trajectory-level signals into step-level credits through step grouping or graph-based advantage estimation, but can overlook meaningful intermediate milestones. We propose MileGPO (Milestone Inference with Local Evidence for Graph-Based Policy Optimization), which derives process-level credit from grouped on-policy rollouts through three designs. Milestone Discovery identifies candidate milestones on successful rollouts and recurring traps on failed ones. Reliability-Calibrated Shaping (RCS) weights these candidates by outcome-based confidence, strengthening reliable milestones and traps while down-weighting uncertain ones. Progress-Contrastive Calibration (PCC) further tests whether a candidate reflects local progress and whether its incoming ansition outperforms observed alternatives from the same state.MileGPO requires neither auxiliary models nor additional environment interaction. Experiments on ALFWorld and WebShop show state-of-the-art performance and a small in-distribution to out-of-distribution gap on ALFWorld. Ablations and credit diagnostics indicate that reliability weighting, local progress, and same-state branch evidence complement milestone discovery and resolve ambiguous intermediate credit.

## Metadata
- **Published**: 2026-08-20T08:58:27Z
- **Authors**: Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19803v1)