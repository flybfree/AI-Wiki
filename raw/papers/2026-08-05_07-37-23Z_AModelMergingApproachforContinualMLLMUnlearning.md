---
title: A Model Merging Approach for Continual MLLM Unlearning
published: 2026-08-05T07:37:23Z
authors: Yuhang Wang, Linlin Zhang, Haoxuan Ji, Xianmin Ye, Zhenxing Niu, Haichang Gao
url: http://arxiv.org/abs/2608.04548v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Model Merging Approach for Continual MLLM Unlearning

## Abstract
Multimodal large language model (MLLM) unlearning methods have been proposed to remove private, sensitive, or proprietary information from well-trained models. However, most existing MLLM unlearning methods are designed for one-shot requests and fail to adequately address continual scenarios, as repeatedly applying one-shot operations leads to cumulative utility degradation, unlearning rebound, and retention drift. We introduce Merging for Continual Unlearning (MCU), an approach that dynamically merges multiple one-shot unlearning adapters into a unified adapter upon receiving each new unlearning request.Through a leave-one-out merging analysis, we reveal that these unlearning adapters exhibit strong cross-task dependencies. Such dependencies have two contrasting effects: they can facilitate cross-task unlearning transferability, but they can also introduce severe interference that degrades unlearning effectiveness and compromises retained knowledge. To address this challenge, MCU projects the adapters into a shared representation space, preserves their dominant directions, suppresses over-concentrated coordinates, and reconfigures cross-task dependencies to mitigate interference while enhancing transferability. Experiments on ICU-Bench and MLLMU-Bench demonstrate that MCU achieves superior unlearning effectiveness while preserving both retained knowledge and general multimodal utility.

## Metadata
- **Published**: 2026-08-05T07:37:23Z
- **Authors**: Yuhang Wang, Linlin Zhang, Haoxuan Ji, Xianmin Ye, Zhenxing Niu, Haichang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04548v1)