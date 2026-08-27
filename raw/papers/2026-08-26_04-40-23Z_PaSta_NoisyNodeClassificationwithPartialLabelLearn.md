---
title: PaSta: Noisy Node Classification with Partial Label Learning
published: 2026-08-26T04:40:23Z
authors: Yujing Liu, Yixin Liu, Yu Zheng, Yue Tan, Alan Wee-Chung Liew, Shirui Pan
url: http://arxiv.org/abs/2608.25365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PaSta: Noisy Node Classification with Partial Label Learning

## Abstract
Noisy node classification problem is a fundamental yet challenging task for real-world graph-related web services, where node labels are often corrupted or unreliable due to weak supervision or automatic annotation. However, existing methods typically train models based on one-hot labels, which not only makes models susceptible to overfitting on noisy labels, but also leads to error accumulation after pseudo-label-guided enhancement. In this paper, we propose a novel Partial label-based Self-training framework (PaSta for short) that leverages partial label learning technique to overcome the limitations of existing methods. Specifically, PaSta first trains multiple annotators to comprehensively capture the class distribution of nodes and aggregates their predictions to construct high-quality partial labels. Subsequently, we design a partial label-based classification model with two well-crafted loss functions to guide the model learning at both label and representation spaces. To further enhance the robustness against noisy labels, we introduce a self-training strategy where the labels refined by partial label learning are then used to further optimize the annotators in a closed-loop iterative manner. Extensive experiments on five datasets demonstrate that, compared with existing state-of-the-art methods, PaSta achieves an average improvement of 1.1% in classification performance under various noise settings.

## Metadata
- **Published**: 2026-08-26T04:40:23Z
- **Authors**: Yujing Liu, Yixin Liu, Yu Zheng, Yue Tan, Alan Wee-Chung Liew, Shirui Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25365v1)