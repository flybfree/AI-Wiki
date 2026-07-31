---
title: Learning Color Grading, No Photo Sharing: Federated Aesthetic Preference Learning for Personalized Image Enhancement
published: 2026-07-30T04:16:38Z
authors: Chuanzhi Xu, Ziyuan Tao, Jean Julien KNell, Yanrong Chen, Haolan Guo, Xuanhua Yin, Adnan Mahmood, Weidong Cai
url: http://arxiv.org/abs/2607.27659v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Color Grading, No Photo Sharing: Federated Aesthetic Preference Learning for Personalized Image Enhancement

## Abstract
Personalized image enhancement should reflect individual aesthetic taste, yet learning such preferences commonly depends on private photos and ratings that are unsuitable for centralized collection. The task must infer preference from sparse, heterogeneous feedback and translate it into natural-looking color transformations on resource-constrained user devices. We introduce FedPAIE, a federated personalized aesthetic image enhancement framework for user-adaptive color grading without centralizing raw photos or ratings. FedPAIE trains a lightweight dual-cue aesthetic scorer, calibrates it into a personalized scorer on a small local support set, and freezes it to guide regularized adaptation of a lightweight CLUT enhancer from unpaired local photographs. Fidelity constraints and an excess-gap penalty regularize scorer-guided adaptation to limit proxy-score over-optimization while preserving content and natural appearance. Training remains lightweight throughout the pipeline: scorer learning updates at most 0.787M parameters, enhancer adaptation updates 0.265M, and inference retains only a 0.293M-parameter personalized enhancer. Experiments on MIT-Adobe FiveK and Flickr-AES demonstrate effective open-world personalization and a favorable balance between user preference and image fidelity. FedPAIE thus connects decentralized preference learning with efficient personalized image transformation without requiring paired user retouches.

## Metadata
- **Published**: 2026-07-30T04:16:38Z
- **Authors**: Chuanzhi Xu, Ziyuan Tao, Jean Julien KNell, Yanrong Chen, Haolan Guo, Xuanhua Yin, Adnan Mahmood, Weidong Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27659v1)