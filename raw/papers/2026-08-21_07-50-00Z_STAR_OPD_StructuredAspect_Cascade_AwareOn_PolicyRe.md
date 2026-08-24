---
title: STAR-OPD: Structured Aspect-Cascade-Aware On-Policy Reward Distillation for ABSA Quadruple Extraction
published: 2026-08-21T07:50:00Z
authors: Tong Sun, Mingyang Ma, Jiayang Yu
url: http://arxiv.org/abs/2608.20831v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# STAR-OPD: Structured Aspect-Cascade-Aware On-Policy Reward Distillation for ABSA Quadruple Extraction

## Abstract
Aspect-based sentiment analysis (ABSA) quadruple extraction requires jointly predicting target, aspect, opinion, and sentiment over reviews that often contain multiple fine-grained sentiment tuples. While large chain-of-thought (CoT) models perform well on this task, distilling them into smaller deployable models remains difficult. We identify a task-specific failure mode in distilled ABSA extraction: student errors at the target-aspect interface create structurally invalid states, such as broken target-aspect bindings and hallucinated targets, which then corrupt downstream predictions. Conventional off-policy distillation is poorly suited to this setting because it trains only on teacher-generated trajectories and provides little supervision on the student-induced structural states that dominate inference. To address this mismatch, we propose STAR-OPD (STructured Aspect-cascade-aware On-Policy Reward Distillation), which builds on generic on-policy distillation and instantiates it for ABSA quadruple extraction with cascade-aware, set-structured rewards. STAR-OPD trains on student rollouts and applies set-structured rewards that directly target binding consistency, target grounding, and fine-grained aspect disambiguation. Experiments on E-ABSA20K and SemEval-2014 show that STAR-OPD consistently outperforms off-policy and general on-policy baselines, reduces target hallucination, and substantially improves performance on structurally hard cases. With Qwen3-4B, STAR-OPD substantially narrows the student-teacher gap while improving inference efficiency, highlighting the importance of on-policy structural correction for distilled ABSA extraction.

## Metadata
- **Published**: 2026-08-21T07:50:00Z
- **Authors**: Tong Sun, Mingyang Ma, Jiayang Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20831v1)