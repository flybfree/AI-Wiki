---
title: Socio-Foundation: A Model for Generalizable Individual Behavior Simulation via Hierarchical Capability Distillation
published: 2026-10-06T18:31:42Z
authors: Liang Wang, Wenxuan Xie, Xinyi Mou, Yixin Luo, Zhongyu Wei
url: http://arxiv.org/abs/2610.08967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Socio-Foundation: A Model for Generalizable Individual Behavior Simulation via Hierarchical Capability Distillation

## Abstract
Simulating individual behavior requires large language models (LLMs) to preserve persona traits while adapting to dynamic social contexts. However, general-purpose LLMs often flatten distinct personas, while task-specific tuning suffers from fragmentation and generalization. To overcome these challenges, we organize individual simulation into the \textbf{FONTS Taxonomy}, comprising five complementary capability dimensions: \emph{persona fidelity} (\textbf{F}), \emph{outcome realization} (\textbf{O}), \emph{behavioral naturalness} (\textbf{N}), \emph{trajectory coherence} (\textbf{T}), and \emph{social grounding} (\textbf{S}). Grounded in this taxonomy, we curate a standardized training corpus library of approximately 10 million instances across 14 representative datasets and present \textbf{Socio-Foundation}. Socio-Foundation decouples specialization from integration via a three-stage pipeline: learning task experts via DAPO, consolidating them into capability experts via off-policy distillation, and unifying them via multi-teacher on-policy distillation (MOPD). We also establish \textbf{IndiEval}, consolidating 29 metrics across the FONTS dimensions. Experiments show that Socio-Foundation outperforms its \textit{Qwen3-8B} base by 11.0 points and approaches frontier models such as \textit{GLM-5.2}, with ablations and out-of-distribution evaluations further demonstrating the effectiveness and generalization of our model.

## Metadata
- **Published**: 2026-10-06T18:31:42Z
- **Authors**: Liang Wang, Wenxuan Xie, Xinyi Mou, Yixin Luo, Zhongyu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08967v1)