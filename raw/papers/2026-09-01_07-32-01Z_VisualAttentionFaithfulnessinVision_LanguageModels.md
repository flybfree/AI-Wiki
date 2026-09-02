---
title: Visual Attention Faithfulness in Vision-Language Models is Heterogeneous
published: 2026-09-01T07:32:01Z
authors: Xurui Song, Weishi Wang, Zhongqi Yue, Kuluhan Binici, Tao Bai, Hongxin Shao, Daniel Dahlmeier, Jun Luo
url: http://arxiv.org/abs/2609.00830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visual Attention Faithfulness in Vision-Language Models is Heterogeneous

## Abstract
Whether attention weights faithfully reflect model reasoning has been actively debated in NLP, yet this question remains largely unexplored for the visual modality in Vision-Language Models (VLMs). We address this gap through causal perturbation analysis on current VLMs, evaluating both the comprehensiveness and sufficiency gap of attention-ranked visual tokens. Our analysis reveals that visual attention faithfulness is heterogeneous, manifesting in three distinct processing modes: Faithful-Sufficient, where top-$k$ attention tokens are both necessary and sufficient for prediction; Faithful-Distributed, where they are necessary but broader visual context remains required; and Non-Focal, where no localized attention region is individually necessary while visual information remains an essential trigger for prediction. Furthermore, human-annotated ground-truth regions satisfy comprehensiveness in only $\sim 60$% of cases compared with model attention rankings, revealing systematic divergence between model visual reliance and human intuition. We demonstrate these patterns across both general VQA on VQAv2 and document tasks on VRDU and ChartQA, showing that visual attention faithfulness varies systematically with processing demands and model architectures rather than being uniformly faithful or unfaithful.

## Metadata
- **Published**: 2026-09-01T07:32:01Z
- **Authors**: Xurui Song, Weishi Wang, Zhongqi Yue, Kuluhan Binici, Tao Bai, Hongxin Shao, Daniel Dahlmeier, Jun Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00830v1)