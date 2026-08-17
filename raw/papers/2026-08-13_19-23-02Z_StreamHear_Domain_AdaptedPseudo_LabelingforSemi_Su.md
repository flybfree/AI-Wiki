---
title: StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition
published: 2026-08-13T19:23:02Z
authors: Zefang Liu, Chenyang Zhu, Sangwoo Cho, Xujun Peng, Shi-Xiong Zhang, Sambit Sahu
url: http://arxiv.org/abs/2608.13717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition

## Abstract
Streaming automatic speech recognition (ASR) underperforms on domain-shifted target audio, where labeled in-domain data is costly to prepare while unlabeled audio is abundant. We present StreamHear, a semi-supervised pipeline that adapts a pretrained streaming student by fine-tuning an offline transducer teacher on the labeled training set, generating pseudo-labels on the unlabeled portion, and fine-tuning the student on the mixture. We further introduce a prior-regularized dynamic-programming realignment step that fixes chunk-level word placement using an ASR-hypothesis anchor. Across four datasets spanning financial calls, prepared read speech, and phone-quality dialogue, StreamHear consistently outperforms supervised student fine-tuning and narrows the gap to the offline teacher.

## Metadata
- **Published**: 2026-08-13T19:23:02Z
- **Authors**: Zefang Liu, Chenyang Zhu, Sangwoo Cho, Xujun Peng, Shi-Xiong Zhang, Sambit Sahu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13717v1)