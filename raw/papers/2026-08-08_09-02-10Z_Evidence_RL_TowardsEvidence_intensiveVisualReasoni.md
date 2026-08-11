---
title: Evidence-RL: Towards Evidence-intensive Visual Reasoning
published: 2026-08-08T09:02:10Z
authors: Haojie Huang, Xinlei Yu, Chengming Xu, Zhangquan Chen, Cheng Yang, Qingdong He, Yu Yang, Jiangning Zhang, Xiaobin Hu
url: http://arxiv.org/abs/2608.08021v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-RL: Towards Evidence-intensive Visual Reasoning

## Abstract
Vision-Language Models (VLMs) should answer from concrete image evidence rather than language priors, dataset shortcuts, or irrelevant visual context. Existing perception-aware post-training methods encourage image use through global perturbations or attention proxies, but they do not test whether a sampled answer causally depends on the local evidence that supports it. We propose Counterfactual Evidence Disentanglement (CED), a training-time evidence audit for VLM grounding. For each response, CED neutralizes an object-centric Evidence Region and compares the resulting support drop against matched non-evidence Regions. We combine this signal with answer correctness inside GRPO, rewarding correct answers that rely on the evidence path rather than shortcut or nuisance paths. CED uses weak object-level proposals, requires no question-specific evidence annotations, and adds no inference-time overhead. Across nine public benchmarks and four backbones, CED outperforms prior RL-based post-training methods, with targeted analyses verifying its object-centric signal.

## Metadata
- **Published**: 2026-08-08T09:02:10Z
- **Authors**: Haojie Huang, Xinlei Yu, Chengming Xu, Zhangquan Chen, Cheng Yang, Qingdong He, Yu Yang, Jiangning Zhang, Xiaobin Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08021v1)