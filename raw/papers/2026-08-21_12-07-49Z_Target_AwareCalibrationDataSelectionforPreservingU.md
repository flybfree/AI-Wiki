---
title: Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models
published: 2026-08-21T12:07:49Z
authors: Zhen Yang, Sizai Hou, Kaiwen Zheng, Yaofang Liu, Liang He, Yixuan Chen, Kangning Cui
url: http://arxiv.org/abs/2608.21019v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models

## Abstract
Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective. We frame calibration-data selection for quantization as a target-dependent uncertainty-preservation problem. Different deployments emphasize different regions of the input distribution, yet prior work mainly optimizes accuracy-oriented compression metrics or adjusts scores after quantization. We formalize this goal with distributional and boundary preservation risks, and provide a simple mixture-mismatch argument explaining why no single calibration recipe should be expected to fit all targets. We introduce Doubt-Preserving Quantization (DPQ), a lightweight pre-quantization recipe family that uses full-precision predictions to construct target-aligned calibration mixtures of high-doubt examples and generic anchors. Across 8 language models, 9 NLP benchmarks, and 22 comparison methods, the leading fixed recipe changes with the preservation target: DPQ-r75 leads on SQuAD2 answerability-boundary preservation, while milder or single-signal variants, including DPQ-r50, confidence-only, and entropy-only, better preserve broad multiple-choice QA behavior. These results show that calibration data should be selected for the specific full-precision score behavior a deployment needs to preserve, rather than treated as a fixed quantization detail.

## Metadata
- **Published**: 2026-08-21T12:07:49Z
- **Authors**: Zhen Yang, Sizai Hou, Kaiwen Zheng, Yaofang Liu, Liang He, Yixuan Chen, Kangning Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21019v1)