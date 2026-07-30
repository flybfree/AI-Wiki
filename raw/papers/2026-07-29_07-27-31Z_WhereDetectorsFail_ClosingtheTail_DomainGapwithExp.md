---
title: Where Detectors Fail: Closing the Tail-Domain Gap with Expert-Guided Mutual Distillation
published: 2026-07-29T07:27:31Z
authors: Xuan Feng, Guihong Liu, Tianlong Gu, Shuai Zhao, Xuemin Wang, Chenzhong Bin, Yang Liu, Bo An
url: http://arxiv.org/abs/2607.26555v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Detectors Fail: Closing the Tail-Domain Gap with Expert-Guided Mutual Distillation

## Abstract
Multimodal fake news detectors often generalize poorly across domains because they learn to trust unreliable evidence: domain-specific shortcuts amplified by imbalanced data and semantically inconsistent text-image pairs that make cross-modal evidence unreliable. We propose Expert-Guided Mutual Distillation (EGMD), which learns what evidence to trust across the prediction pipeline. At the input level, input-level calibration encodes pair-level coherence as a shared gain before fusion. At the representation level, an expert-guided teacher aligns domain statistics and encourages domain-specific patterns to concentrate in specialized experts. At the decision level, prototype-anchored domain-specific students use mutual learning and dual-channel distillation to inherit the teacher's feature geometry and calibrated predictions while discouraging local domain priors. We further construct Weibo_Balanced, a domain-balanced benchmark that isolates the effect of imbalance on generalization. Across four datasets in two languages, EGMD achieves state-of-the-art accuracy while reducing domain bias by up to 57.3%.

## Metadata
- **Published**: 2026-07-29T07:27:31Z
- **Authors**: Xuan Feng, Guihong Liu, Tianlong Gu, Shuai Zhao, Xuemin Wang, Chenzhong Bin, Yang Liu, Bo An
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26555v1)