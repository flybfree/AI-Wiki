---
title: Ground-Truth Neighborhood Regularization for Reinforcement Learning Post-Training of Time Series Foundation Models
published: 2026-08-08T08:41:33Z
authors: Jianqi Zhang, Xingyu Zhang, Zeen Song, Changwen Zheng, Fanjiang Xu, Wenwen Qiang
url: http://arxiv.org/abs/2608.08010v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ground-Truth Neighborhood Regularization for Reinforcement Learning Post-Training of Time Series Foundation Models

## Abstract
Time series forecasting (TSF) plays an important role in a wide range of real-world applications. Recently, time series foundation models (TSFMs), pretrained on large-scale datasets, have demonstrated strong generalization capabilities and emerged as an important paradigm for TSF. Reinforcement learning (RL) post-training has consequently attracted growing attention as a means of further improving their performance on downstream tasks. However, we find that, in certain forecast regions, RL post-training may gradually shift the output distributions of TSFMs away from the ground truth, thereby limiting their performance. We refer to this phenomenon as \textbf{suboptimal collapse}. Our analysis suggests that difficulty in initially sampling high-quality trajectories near the ground truth is an important contributing factor to suboptimal collapse. To address this issue, we propose Ground-Truth Neighborhood Regularization (GTN-R) for RL post-training of TSFMs. GTN-R uses the ground truth as a reference for locating high-quality regions and guides the model's probability mass toward the ground-truth neighborhood. This increases the probability of sampling high-quality trajectories, mitigates suboptimal collapse, and improves performance. Moreover, GTN-R can be flexibly integrated into various RL methods for TSFMs. Extensive experiments show its effectiveness.

## Metadata
- **Published**: 2026-08-08T08:41:33Z
- **Authors**: Jianqi Zhang, Xingyu Zhang, Zeen Song, Changwen Zheng, Fanjiang Xu, Wenwen Qiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08010v1)