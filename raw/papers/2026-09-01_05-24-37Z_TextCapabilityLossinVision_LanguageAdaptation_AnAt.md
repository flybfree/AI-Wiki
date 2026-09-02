---
title: Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis
published: 2026-09-01T05:24:37Z
authors: Minsik Choi, Geewook Kim, Young Geun Kim
url: http://arxiv.org/abs/2609.00746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis

## Abstract
Fine-tuning a pretrained LLM into a vision-language model (VLM) can erode the backbone's text capability, with the damage concentrated on tasks that require following exact output rules, such as instruction following, chain-of-thought reasoning graded on a strictly parsed final answer, and similar evaluations with strict graders. We trace this gap to attention-sink corruption: VL fine-tuning perturbs the early sink position that anchors a large fraction of attention probability, and how well the base LLM preserves its sink tracks how much of the affected capability survives adaptation. Building on this view, we introduce Sink Strength, a single scalar computed on the base LLM in a few seconds on a single GPU that predicts post-VL degradation without any VL training. It consistently tracks relative degradation across the six VLM-LLM pairs and multiple format-sensitive tasks. Complementing this diagnostic, we find that post-pretraining QK-RMSNorm injection fails to reproduce the protection of native QK-RMSNorm, while several off-the-shelf weight-merging settings fail to recover the lost capability after VL training. These negative results underscore the value of screening backbones with Sink Strength before VL training and narrow the intervention space toward head-selective training-time protection.

## Metadata
- **Published**: 2026-09-01T05:24:37Z
- **Authors**: Minsik Choi, Geewook Kim, Young Geun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00746v1)