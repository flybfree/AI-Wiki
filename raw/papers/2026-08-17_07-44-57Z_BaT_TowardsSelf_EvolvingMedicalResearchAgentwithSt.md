---
title: BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics
published: 2026-08-17T07:44:57Z
authors: Junqi Liu, Yufan He, Yexiao He, Pengfei Guo, Dong Yang, Andriy Myronenko, Can Zhao, Hanrong Ye, Tianhao Qi, Yuyin Zhou, Daguang Xu, Yucheng Tang
url: http://arxiv.org/abs/2608.16211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics

## Abstract
Long-horizon agents are beginning to automate complete workflows that produce code, reports, and research artifacts. Medical imaging workflows are multi-stage and data-sensitive, while expert trajectories remain scarce and difficult to share. Structured benchmarks can localize failures through stage-level rubrics, but standard post-training discards these diagnostics before the next training round. We present Benchmark-as-Teacher (BaT), a recursive self-improvement system for agent post-training. BaT contains two linked components: the asynchronous Stage Bank data pipeline and BiCuRL (Bilevel Curriculum Reinforcement Learning), its self-improving post-training method. Stage Bank synthesizes content-isolated training states outside the policy-update loop. BiCuRL uses a fixed held-out evaluation to select the next stage curriculum, verifies rollouts with task rubrics, updates the policy with GRPO, and returns the candidate checkpoint to evaluation. On AutoMedBench-Lite, BaT-4B and BaT-9B more than double the Overall scores of their Qwen Instruct baselines. BaT-9B Agent reaches 79.6 Overall, exceeding Claude Opus 4.6 with Claude Code at 77.5.

## Metadata
- **Published**: 2026-08-17T07:44:57Z
- **Authors**: Junqi Liu, Yufan He, Yexiao He, Pengfei Guo, Dong Yang, Andriy Myronenko, Can Zhao, Hanrong Ye, Tianhao Qi, Yuyin Zhou, Daguang Xu, Yucheng Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16211v1)