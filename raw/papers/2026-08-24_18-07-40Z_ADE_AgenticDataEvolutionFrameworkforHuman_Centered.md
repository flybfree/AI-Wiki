---
title: ADE: Agentic Data Evolution Framework for Human-Centered Objectives
published: 2026-08-24T18:07:40Z
authors: Yang Yu, Yilin Jiang, Zexuan Fei, Yiming Luo, Xingkai Song, Kaiyi Huang, Aimin Zhou, Xin Lin, Fei Tan
url: http://arxiv.org/abs/2608.23719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ADE: Agentic Data Evolution Framework for Human-Centered Objectives

## Abstract
Aligning large language models to human-centered objectives is difficult when targets are non-executable and context-dependent, limiting reliable verification and scalable supervision. Although synthetic data expands coverage, weak verification shifts the bottleneck from generation to selection. Noisy signals destabilize iterative refinement and can cause silent regressions. We propose Agentic Data Evolution (ADE), a data-centric framework that organizes synthetic supervision as evolving data snapshots. ADE improves data snapshots through a closed-loop Observation-Variation-Selection (OVS) procedure, where a steady-state admission mechanism acts as a quality ratchet that conservatively gates updates for sustained cross-round improvement. We validate these improvements through complementary intrinsic trend tracking and extrinsic post-training evaluation. On DEV300, ADE raises the intrinsic win rate from 50% to 75.81% and the extrinsic win rate from 55.20% to 68.86%, consistent performance gains across diverse benchmarks. Blind expert evaluation further confirms this, with a 66.11% preference for evolved answers. These gains extend across post-training methods, model scales, and tasks beyond the target weakly verifiable educational objectives. Resources are available at https://github.com/ZeroLoss-Lab/Agentic-Data-Evolution.

## Metadata
- **Published**: 2026-08-24T18:07:40Z
- **Authors**: Yang Yu, Yilin Jiang, Zexuan Fei, Yiming Luo, Xingkai Song, Kaiyi Huang, Aimin Zhou, Xin Lin, Fei Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23719v1)