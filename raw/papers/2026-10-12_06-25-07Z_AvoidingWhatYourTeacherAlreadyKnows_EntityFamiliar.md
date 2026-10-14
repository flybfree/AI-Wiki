---
title: Avoiding What Your Teacher Already Knows: Entity Familiarity for Deep-Search Distillation
published: 2026-10-12T06:25:07Z
authors: Yifei Liu, Zhixiang Liang, Wentao Tan, Yicheng Wang, Jiaqi Wang, Nan Duan, Qiong Cao
url: http://arxiv.org/abs/2610.16251v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Avoiding What Your Teacher Already Knows: Entity Familiarity for Deep-Search Distillation

## Abstract
Deep-search agents are commonly trained by distilling tool-use trajectories from stronger teacher models. However, structurally complex questions may remain relatively easy for teachers familiar with key entities in the underlying entity graph, resulting in lower search demand and weaker supervision. We refer to this teacher-specific variation in question difficulty as teacher-relative difficulty and investigate entity familiarity as an early predictor. We first introduce Evidence-Verified Entity Familiarity (EVF), which estimates familiarity by verifying a teacher-generated factual brief against online evidence. Across multiple teachers, EVF is significantly correlated with teacher-relative difficulty with AUCs of 0.60--0.70. However, its high cost makes it impractical for constructing entity graphs at scale. To address this limitation, we propose Self-Reported Entity Familiarity (SEF), a lightweight gating signal that directly asks a teacher whether it is familiar with an entity before admitting that entity into the graph. Across multiple teachers, trajectories from SEF-gated synthesis exhibit greater observed search demand and yield higher downstream student accuracy than those from ungated synthesis. Because familiarity is teacher specific, we further study cross-teacher reuse. We screen graphs collected for other teachers using Kimi-K3's SEF judgments and use the retained graphs to produce 5,411 additional trajectories. Combined with 2,200 trajectories from newly constructed, SEF-gated graphs, these data improve Qwen3.8-27B's accuracy from 44.10% to 66.41% on a BrowseComp subset, and achieving state-of-the-art performance among models of comparable size on BrowseComp, SEAL-0, HLE-text, and xbench. Overall, SEF provides a low-cost way to synthesize more informative supervision for deep-search distillation.

## Metadata
- **Published**: 2026-10-12T06:25:07Z
- **Authors**: Yifei Liu, Zhixiang Liang, Wentao Tan, Yicheng Wang, Jiaqi Wang, Nan Duan, Qiong Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16251v1)