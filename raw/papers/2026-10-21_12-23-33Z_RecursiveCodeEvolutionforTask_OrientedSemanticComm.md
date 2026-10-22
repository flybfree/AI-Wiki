---
title: Recursive Code Evolution for Task-Oriented Semantic Communications
published: 2026-10-21T12:23:33Z
authors: Yan Gong, Zheng Chu, Wei Koong Chai, Hari Mohan Pandey, Jingrui Hou, Miao Zhang, Yuanjian Li, Pei Xiao
url: http://arxiv.org/abs/2610.29641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recursive Code Evolution for Task-Oriented Semantic Communications

## Abstract
Semantic communication jointly optimizes inference accuracy, channel use, and computation, yet the underlying communication program is typically specified before training. This paper presents ComRSI (Communications-Oriented Recursive Self-Improvement), a framework for recursively evolving that program through large-language-model-assisted code edits. A fixed agent modifies the encoder, channel adapters, decoder, loss, and training policy; a protected evaluator screens candidates under prescribed budgets and resource constraints. Accepted code and textual feedback inform subsequent proposals, while candidate weights are trained from scratch. In the original ten-generation CIFAR-100 lineage, eight accepted revisions produce an attention-pooled code achieving 74.3% test accuracy over an Additive White Gaussian Noise (AWGN) channel at 32 complex symbols per image, compared with 67.2% at 256 symbols for the initial design. The program also improves fading-channel accuracy and transfers to Tiny-ImageNet after retraining. A repeat study with ten searches per method compares ComRSI against non-recursive agents with and without textual history. Mean final search scores balancing accuracy, transmission rate, and computational cost are 0.7587, 0.7376, and 0.7089, respectively; the mean numbers of accepted revisions per search are 6.0, 5.0, and 2.1. The advantage over the memoryless agent is supported by a two-sided rank test, whereas the difference from the history-equipped agent remains statistically inconclusive at this sample size. Archived proposals show that pooling can yield a large improvement, while retained history supports subsequent refinement. These results support recursive program optimization within the evaluated setting and expose its remaining rate-robustness and compute-placement trade-offs.

## Metadata
- **Published**: 2026-10-21T12:23:33Z
- **Authors**: Yan Gong, Zheng Chu, Wei Koong Chai, Hari Mohan Pandey, Jingrui Hou, Miao Zhang, Yuanjian Li, Pei Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29641v1)