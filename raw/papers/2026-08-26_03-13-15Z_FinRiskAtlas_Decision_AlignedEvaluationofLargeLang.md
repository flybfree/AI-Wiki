---
title: FinRiskAtlas: Decision-Aligned Evaluation of Large Language Models for Financial Risk Review
published: 2026-08-26T03:13:15Z
authors: Suyang Zhong, Jingzhe Zhu, Qi Xu, Liyao Sun, Yin Wang, Qingqing Sun, Shuai Chen, Tianyi Zhang
url: http://arxiv.org/abs/2608.25325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinRiskAtlas: Decision-Aligned Evaluation of Large Language Models for Financial Risk Review

## Abstract
Deploying large language models for professional financial review requires more than measuring general financial competence: models must perform the specific review operation required by a workflow and determine whether available evidence is sufficient for a defensible decision. Existing financial benchmarks cover knowledge, reasoning, compliance, and professional tasks, but their evaluation units are often organized around datasets or task formulations rather than the decisions that deployed systems support. We introduce FinRiskAtlas, a Chinese-language benchmark that evaluates financial LLMs along two complementary dimensions: operation execution under fixed evidence states and evidence-state control under evolving review conditions. The static benchmark contains 9,742 instances across 53 task families, including 42 Domain Knowledge families and eleven downstream review operations defined by explicit evaluation contracts. FinRisk-Ask extends this framework through offline replay of 680 pre-action states from 104 de-identified professional trajectories, withholding future evidence during inference and using it only to construct expert-verified evidence targets. Across 33 model configurations, operation-level evaluation yields non-redundant rankings (mean pairwise Spearman correlation 0.42 across downstream operations), and knowledge-based shortlisting can incur up to 18.01 points of regret on individual operations. FinRisk-Ask further shows that entering the Ask branch more frequently does not necessarily improve request targeting or end-to-end evidence acquisition. These results show that broad financial capability scores do not fully capture where models are reliable in professional workflows, motivating evaluation units aligned with the decisions and evidence states that deployed systems must support.

## Metadata
- **Published**: 2026-08-26T03:13:15Z
- **Authors**: Suyang Zhong, Jingzhe Zhu, Qi Xu, Liyao Sun, Yin Wang, Qingqing Sun, Shuai Chen, Tianyi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25325v1)