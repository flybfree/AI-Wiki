---
title: BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure
published: 2026-09-10T03:10:58Z
authors: Shenghan Zheng, Zonglin Di, Yimin Liu, Kyoung Whan Choe, Jiankai Sun, Heguang Lin, Penghao Jiang, Yifeng He, Xiao Cheng, Jicheng Wang, Wenbo Chen, Alex Yates, Yinzhe Zhao, Bingran You, Yuan Gao, Ayush Munot, Shubham Gaur, Zhe Ye, Hao Wang, Xiangyi Li, Dawn Song, Christophe Hauser
url: http://arxiv.org/abs/2609.11028v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure

## Abstract
LM-agent benchmarks increasingly function as interactive evaluation infrastructure. Agents observe state, call tools, modify workspaces,   submit artifacts, and receive rewards from outcome procedures. This interactivity makes evaluations vulnerable to reward hacking: an agent   improves its measured score by exploiting the reward-relevant trajectory instead of solving the intended task. Existing defenses rely largely   on task-specific patches, prompt instructions, or post-hoc detectors. They do not provide reusable evidence that a concrete run remained   within its intended evaluation boundary. This paper presents BenchShield, a model-backed instrumentation layer for reward integrity in   LLM-agent evaluation. BenchShield grounds detection in a finite lifecycle model of an evaluation's reward-relevant events. Within the   benchmark infrastructure, two complementary analyses operate over this model. A static, phase-aware taint analysis exposes reward-hacking   paths before a run. Its runtime counterpart uses infrastructure-side evidence to attribute concrete agent use and emit evidence-backed claims.   We construct BenchShield Trajectories, a human-labeled corpus of 456 adjudicated trajectories from more than 31,000 public agent runs across   three benchmarks. Compared with an agentic hackability scanner baseline on the same tasks and model, BenchShield improves full-chain recall   from 23-94% to 77-100%, same-vector coverage from 16-56% to 43-78%, and reduces per-task cost by up to 65%. Its runtime analysis achieves 96%   accuracy in detecting reward hacking from infrastructure-side evidence.

## Metadata
- **Published**: 2026-09-10T03:10:58Z
- **Authors**: Shenghan Zheng, Zonglin Di, Yimin Liu, Kyoung Whan Choe, Jiankai Sun, Heguang Lin, Penghao Jiang, Yifeng He, Xiao Cheng, Jicheng Wang, Wenbo Chen, Alex Yates, Yinzhe Zhao, Bingran You, Yuan Gao, Ayush Munot, Shubham Gaur, Zhe Ye, Hao Wang, Xiangyi Li, Dawn Song, Christophe Hauser
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11028v1)