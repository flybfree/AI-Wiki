---
title: ZIPBrain: Can EEG Foundation Models Be Faster, Locally Deployable, but Accurate?
published: 2026-08-07T09:45:02Z
authors: Lingwei Li, Yirong Kan, Peng Chen, Xu Cao, Zheng Chen, Yasuhiko Nakashima
url: http://arxiv.org/abs/2608.07033v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ZIPBrain: Can EEG Foundation Models Be Faster, Locally Deployable, but Accurate?

## Abstract
This work investigates whether Electroencephalograph (EEG) foundation models (EFMs) can be made faster and locally deployable without sacrificing accuracy. EEG foundation models are a major trend, offering strong general-purpose representations. However, their computational burden grows quadratically with input length, hindering deployment on resource-constrained scenario, particularly for real-time clinical monitoring. EEG's low SNR further suggests many of these tokens are redundant and compressible with little accuracy cost. We propose ZIPBrain, a novel redundancy-aware EEG token pooling module that leverages this low-SNR characteristic to reduce token count. Given a token sequence, ZIPBrain partitions tokens into redundant and unique groups, then merges each redundant token with its most similar counterpart in the unique group. Furthermore, ZIPBrain serves as a training-free, plug-and-play module that seamlessly integrates into standard Transformer encoders with negligible computational overhead. Extensive experiments across multiple EEG foundation models show ZIPBrain's strong versatility, achieving 1.3%-10.5% average improvement over baselines, while reducing wall-clock inference time by 32.7% (up to 41.8% with CUDA Graph) compared to the original EEG foundation models.

## Metadata
- **Published**: 2026-08-07T09:45:02Z
- **Authors**: Lingwei Li, Yirong Kan, Peng Chen, Xu Cao, Zheng Chen, Yasuhiko Nakashima
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07033v1)