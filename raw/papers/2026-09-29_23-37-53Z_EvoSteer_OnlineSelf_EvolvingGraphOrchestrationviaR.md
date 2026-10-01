---
title: EvoSteer: Online Self-Evolving Graph Orchestration via Reference-Anchored Credit Assignment
published: 2026-09-29T23:37:53Z
authors: Mingda Zhang, Hanwen Zhang, Qiang Huang, Zijia Wang, Pengfei Guo, Yuchen Zhang, Jionghao Zhu, Xiaoying Tang
url: http://arxiv.org/abs/2609.38661v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoSteer: Online Self-Evolving Graph Orchestration via Reference-Anchored Credit Assignment

## Abstract
In recent years, LLM-based multi-agent systems have been widely applied to orchestrate tool-using agents into executable communication graphs. However, existing self-evolving orchestration still faces key challenges, including post-hoc evolution that revises the team only after the trajectory ends, credit diffusion that gives every action the same terminal advantage under confounded baselines, and skill admission that is uncalibrated and never retired. To address these challenges, we propose EvoSteer, a new paradigm of Online Self-Evolving Graph Orchestration -- the orchestrator builds a running team and repairs its plausible but failing steps from execution features and a learned value estimate. To support this paradigm, we introduce Anchored Trajectory Balance (AnchorTB), a regression-style flow-matching loss that assigns each orchestration action a coefficient by balancing subtrajectories against a frozen reference. Built on the learned flow, we further propose Validated Skill Admission, in which a candidate skill is tried before promotion and promoted only if paired evidence passes a sequential test under a shared nominal testing budget. Moreover, AnchorTB combines measured task-level reference reward statistics with prefix-dependent corrections. Experimental results on twelve datasets show that EvoSteer significantly outperforms baselines across question answering, mathematical reasoning, code generation, and interactive decision making. Our code is available at https://github.com/beita6969/evosteer.

## Metadata
- **Published**: 2026-09-29T23:37:53Z
- **Authors**: Mingda Zhang, Hanwen Zhang, Qiang Huang, Zijia Wang, Pengfei Guo, Yuchen Zhang, Jionghao Zhu, Xiaoying Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38661v1)