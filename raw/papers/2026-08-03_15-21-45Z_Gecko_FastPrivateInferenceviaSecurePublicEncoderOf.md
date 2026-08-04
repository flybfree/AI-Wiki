---
title: Gecko: Fast Private Inference via Secure Public Encoder Offloading
published: 2026-08-03T15:21:45Z
authors: Cheng'an Wei, Kai Chen, Yue Zhao, Congyi Li, Shenchen Zhu
url: http://arxiv.org/abs/2608.02378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gecko: Fast Private Inference via Secure Public Encoder Offloading

## Abstract
Private inference protects both user inputs and server models during neural network inference, but existing solutions remain too slow for practical deployment. This motivates recent efforts to run a public encoder, such as a pretrained backbone, outside the protection boundary and evaluate only a small private predictor cryptographically. While appealing for efficiency, this design is not inherently secure: naively offloading a public encoder may create a feature-space shortcut: an extraction adversary may learn the remaining private predictor's feature-to-output mapping more easily than the original model's input-to-output behavior.   We present Gecko, designed to limit this additional risk while retaining a compact encrypted predictor. We leverage a frozen backbone that contributes hierarchical features, fixed Fastfood projections that compress them, and private feature gating that prepares them for prediction. We formalize ideal independence and information-preservation conditions as design guidance, then separately evaluate component-reuse extraction attacks. Across image and audio tasks, Gecko achieves 0.4-2.2 second inference with at most 10.8 MB communication and accuracy comparable to transfer-learning baselines. Under the evaluated attacks, reusing the offloaded public encoder provides no significant advantage to model-extraction adversaries. Source code and a demo are available at https://github.com/CassiniHuy/gecko-infer.

## Metadata
- **Published**: 2026-08-03T15:21:45Z
- **Authors**: Cheng'an Wei, Kai Chen, Yue Zhao, Congyi Li, Shenchen Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02378v1)