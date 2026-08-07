---
title: BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition
published: 2026-08-06T13:30:13Z
authors: Bojing Hou, Ruohao Li, Yitong Zhu, Hongjun Liu, Luwen Yu, Yuyang Wang
url: http://arxiv.org/abs/2608.06023v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition

## Abstract
To address the limitations of video-based emotion recognition under ambiguous or socially masked behavioral cues, as well as the poor deployability of physiological signals, this paper proposes a reliability-aware physiology-to-video knowledge distillation framework, termed BioKD. The proposed framework leverages physiological signals as privileged information during training to guide a video-based student model in learning deep affective representations, while relying solely on non-intrusive video inputs at inference time. To cope with the high noise and instability of physiological teacher supervision caused by inter-subject variability, signal artifacts, and temporal inconsistency, BioKD incorporates a sample-wise reliability-aware gating mechanism together with a progressive distillation strategy. By adaptively regulating the strength of knowledge transfer, the framework suppresses negative transfer induced by unreliable physiological supervision and enables more stable cross-modal distillation. Experiments on DEAP and AMIGOS show that BioKD consistently outperforms representative baselines under both trial-wise and subject-wise evaluation protocols for valence and arousal recognition. For example, BioKD achieves 68.01\% on DEAP (trial-wise arousal) and 65.29\% under the more challenging subject-wise setting, demonstrating improved performance under a subject-independent evaluation setting. Further analyses show that BioKD effectively mitigates overconfident teacher errors and outperforms an entropy-only weighting strategy, confirming the importance of explicitly modeling supervision reliability. In addition, BioKD introduces no additional inference-time overhead relative to the same video student architecture and removes the need for physiological sensing and multimodal synchronization.

## Metadata
- **Published**: 2026-08-06T13:30:13Z
- **Authors**: Bojing Hou, Ruohao Li, Yitong Zhu, Hongjun Liu, Luwen Yu, Yuyang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06023v1)