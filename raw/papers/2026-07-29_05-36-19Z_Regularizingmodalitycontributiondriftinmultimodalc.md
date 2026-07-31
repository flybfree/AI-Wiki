---
title: Regularizing modality contribution drift in multimodal continual learning
published: 2026-07-29T05:36:19Z
authors: Zhen Zhang, Jielei Chu, Bin Liu, Tianrui Li
url: http://arxiv.org/abs/2607.27260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Regularizing modality contribution drift in multimodal continual learning

## Abstract
Multimodal continual learning (MMCL) aims to learn emerging knowledge from multimodal data while preserving knowledge. To mitigate forgetting, current MMCL methods usually focus on cross-modal representation alignment or semantic similarity, but they overlook whether the relative contributions of individual modalities and their interactions remain stable across incremental tasks. We term this decision-level shift Modality Contribution Drift (MCD) and quantify it with the MCD score, which combines contribution-strength and relative-reliance changes under controlled interventions on modality subsets. Theoretical and empirical analyses further explain why current MMCL methods cannot reliably mitigate this drift. To this end, we propose Continual Modality Contribution Drift Regularization (CMCDR), which preserves the modality contribution structure of previously learned tasks. Since MMCL settings differ in whether old exemplars are available, CMCDR includes both replay-based and replay-free versions. The replay-based version uses modality-subset interventions as diagnostic probes on stored old samples, compares their contribution profiles between the current model and a frozen previous model, and constrains changes in old-sample modality-specific and interaction contributions. The replay-free version uses current-task samples as probes and distills the frozen model's old-task contribution responses, thereby regularizing the observed contribution profile without exemplars. Experiments on multimodal class-incremental learning and continual visual question answering validate the generality and effectiveness of CMCDR.

## Metadata
- **Published**: 2026-07-29T05:36:19Z
- **Authors**: Zhen Zhang, Jielei Chu, Bin Liu, Tianrui Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27260v1)