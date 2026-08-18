---
title: Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning
published: 2026-08-16T17:35:38Z
authors: Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang, Ian Fasel, Joerg Liebelt
url: http://arxiv.org/abs/2608.15869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

## Abstract
Multimodal large language models increasingly use visual chain-of-thought (Visual CoT) to reason about spatial, temporal, and embodied environments. By generating intermediate reasoning images, Visual CoT provides an intuitive mechanism for visual foresight but introduces substantial inference overhead, which is particularly problematic for proactive video reasoning. We ask whether models can learn to think visually during training while reasoning directly at inference. We introduce Internalized Visual Thinking (IVT), a post-training framework that jointly optimizes textual prediction and next-embedding prediction over unlabeled videos. Given a partially observed video, IVT predicts latent representations of future frames together with the target textual answer, encouraging the model to capture motion, object transitions, interactions, and latent intent. At inference, IVT generates the answer directly without synthesizing or re-encoding future frames. We conduct controlled studies across target representations, decoder designs, prediction horizons, data mixtures, training curricula, and predictive objectives. IVT improves over direct-answer fine-tuning on all six evaluation settings while retaining the same inference pathway. Compared with explicit Visual CoT, IVT achieves comparable or better performance and reduces average end-to-end latency by more than 5x. Together, our findings suggest that explicit pixel-space generation at inference time, as used in visual chain-of-thought, may not be necessary for effective proactive video reasoning. Predictive world modeling can be internalized during training to produce multimodal reasoners that are both more accurate and substantially more efficient.

## Metadata
- **Published**: 2026-08-16T17:35:38Z
- **Authors**: Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang, Ian Fasel, Joerg Liebelt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15869v1)