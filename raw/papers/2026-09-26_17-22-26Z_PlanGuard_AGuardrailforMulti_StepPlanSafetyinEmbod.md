---
title: PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents
published: 2026-09-26T17:22:26Z
authors: Junchi Chen, Changtao Miao, Yuxiao Xiang, Zhenchao Jin, Haojie Yuan, Qi Chu, Tao Gong, He Liu, Bo Zhang, Jiansheng Cai, Zhe Li, Nenghai Yu
url: http://arxiv.org/abs/2609.32801v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PlanGuard: A Guardrail for Multi-Step Plan Safety in Embodied Agents

## Abstract
Embodied task planners may produce multi-step plans whose subtask dependencies and interactions with the environment create physical risks during execution. Yet existing safeguards overlook such compositional risks, as general-purpose guardrails focus on semantic harm and embodied safety detectors assess subtasks in isolation. To address this gap, we introduce PlanGuard, the first pre-execution detector that evaluates the physical safety of a complete multi-step plan in its current environment. For training and evaluation, we construct a Multi-Step Plan Safety (MSP-Safe) dataset through paired task construction, plan generation using diverse planners, and safety annotation by three judges. Task-oriented SFT on MSP-Safe establishes fundamental plan-safety assessment capabilities, yet a substantial gap remains between compact models suitable for real-time deployment and stronger but costlier large models. Accordingly, we propose Strong-Teacher Adaptive Compensation for On-Policy Distillation (STAC-OPD), which provides compact models with adaptive strong-teacher supervision along their on-policy trajectories. It combines token-level distribution transfer from a fine-tuned strong teacher with probability-routed sequence-level compensation, retaining student-generated targets when the student favors the reference safety decision and using teacher-reconstructed targets otherwise. Across all test subsets, PlanGuard-2B achieves average 87.15% ACC and 87.21% F1, demonstrating effective whole-plan physical-risk detection at compact model scale. Code and dataset will be publicly released.

## Metadata
- **Published**: 2026-09-26T17:22:26Z
- **Authors**: Junchi Chen, Changtao Miao, Yuxiao Xiang, Zhenchao Jin, Haojie Yuan, Qi Chu, Tao Gong, He Liu, Bo Zhang, Jiansheng Cai, Zhe Li, Nenghai Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32801v1)