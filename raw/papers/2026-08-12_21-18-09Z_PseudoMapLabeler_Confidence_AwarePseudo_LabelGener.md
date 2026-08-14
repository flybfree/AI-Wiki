---
title: PseudoMapLabeler: Confidence-Aware Pseudo-Label Generation for Semi-Supervised Online Mapping
published: 2026-08-12T21:18:09Z
authors: Chikao Tsuchiya, Dhaval Bhanderi, David Ilstrup, Hsinmin Cheng, Christopher Ostafew
url: http://arxiv.org/abs/2608.12600v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PseudoMapLabeler: Confidence-Aware Pseudo-Label Generation for Semi-Supervised Online Mapping

## Abstract
A critical challenge in deploying online HD map construction systems to real-world scenarios is the scarcity of labeled training data, which limits model generalization in diverse environments. To address this limitation, we propose a teacher-student semi-supervised learning (SSL) framework that generates high-quality pseudo-labels from unlabeled data through confidence-aware map refinement. Our approach first trains a teacher model on limited labeled data, then leverages Beta-distribution-based confidence maps to assess the reliability of predicted map elements across temporal observations. Unlike conventional filtering methods that discard entire elements, we introduce a spatial clipping technique that selectively preserves high-confidence regions while removing unreliable segments. The refined map elements serve as map priors that improve the teacher model's prediction accuracy on unlabeled data in a second pass. These enhanced predictions become pseudo-labels for training a student model from scratch, followed by fine-tuning on the original labeled data. Experimental results on the nuScenes dataset demonstrate that our teacher-student framework with refined pseudo-labels improves performance by +6.1 mAP under a low-label regime compared to training on labeled data alone, offering a practical solution to the labeled data scarcity problem in online HD map construction.

## Metadata
- **Published**: 2026-08-12T21:18:09Z
- **Authors**: Chikao Tsuchiya, Dhaval Bhanderi, David Ilstrup, Hsinmin Cheng, Christopher Ostafew
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12600v1)