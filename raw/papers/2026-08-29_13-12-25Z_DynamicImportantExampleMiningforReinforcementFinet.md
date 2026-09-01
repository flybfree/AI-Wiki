---
title: Dynamic Important Example Mining for Reinforcement Finetuning
published: 2026-08-29T13:12:25Z
authors: Haoru Tan, Sitong Wu, Yanfeng Chen, Shizhen Zhao, Yang-Tian Sun, Tianjia Liu, Chirui Chang, Shaofeng Zhang, Samm Sun, Xiuzhe Wu, Ruobing Xie, Xiaojuan Qi
url: http://arxiv.org/abs/2608.29252v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Important Example Mining for Reinforcement Finetuning

## Abstract
Reinforcement fine-tuning (RFT) is increasingly used to strengthen the reasoning abilities of large models, yet its effectiveness is bound by how training data are selected and used. Most data-centric RFT methods rely on static or heuristic sample selection, implicitly assuming a sample's value is fixed over training. This overlooks the non-stationary dynamics of policy learning and can lead to suboptimal updates. We propose Dynamic Important Example Mining (DIEM), a principled and fully automated framework that makes data utilization adaptive throughout RFT. DIEM integrates two components into each optimization step: (i) a gradient-alignment importance estimator that efficiently approximates each sample's marginal contribution to policy improvement; and (ii) a constrained batch reweighting scheme that maximizes aggregate utility while preserving the update's gradient magnitude to stabilize optimization. Across several reasoning benchmarks, DIEM consistently outperforms strong static and dynamic baselines. The code will be released via https://github.com/hrtan/DIEM.

## Metadata
- **Published**: 2026-08-29T13:12:25Z
- **Authors**: Haoru Tan, Sitong Wu, Yanfeng Chen, Shizhen Zhao, Yang-Tian Sun, Tianjia Liu, Chirui Chang, Shaofeng Zhang, Samm Sun, Xiuzhe Wu, Ruobing Xie, Xiaojuan Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29252v1)