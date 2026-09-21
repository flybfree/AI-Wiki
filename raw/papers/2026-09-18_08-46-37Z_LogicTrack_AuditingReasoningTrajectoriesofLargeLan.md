---
title: LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers
published: 2026-09-18T08:46:37Z
authors: Jingyu Hu, Shu Yang, Weiru Liu, Di Wang
url: http://arxiv.org/abs/2609.21492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers

## Abstract
Chain-of-Thought (CoT) reasoning has been shown to improve the performance of large language models (LLMs), yet existing optimization methods largely rely on outcome-based feedback, leaving the logical validity of intermediate reasoning steps largely unverified. To address the gap whereby LLMs arrive at correct final answers through logically flawed intermediate reasoning chains, we propose LogicTrack, a neuro-symbolic framework that audits reasoning trajectories by auto-formalizing each reasoning step into symbolic representations and verifying it with automated theorem provers. LogicTrack introduces Solver-Based Backtracking Reward (SBR), a step-wise scoring mechanism that quantifies logical soundness and guides backtracking tree search at inference time. We further extend LogicTrack to construct supervised fine-tuning (SFT) data with backtracking traces from its trajectories, enabling fine-tuned models to internalize step-wise auditing as an intrinsic capability. Extensive experiments across 8 reasoning benchmarks and 7 LLMs demonstrate that LogicTrack effectively improves both the verifiability of reasoning chains and final answer pass rate, thereby enhancing overall CoT quality and trustworthiness in high-stakes domains.

## Metadata
- **Published**: 2026-09-18T08:46:37Z
- **Authors**: Jingyu Hu, Shu Yang, Weiru Liu, Di Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21492v1)