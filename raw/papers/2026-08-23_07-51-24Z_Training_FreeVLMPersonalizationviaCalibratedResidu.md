---
title: Training-Free VLM Personalization via Calibrated Residual Decoding
published: 2026-08-23T07:51:24Z
authors: Jiaao Yu, Yujian Ma, Xianming Hu, Pengran Wang, Ang Li
url: http://arxiv.org/abs/2608.22263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-Free VLM Personalization via Calibrated Residual Decoding

## Abstract
Vision-language models can be personalized in a training-free manner by directly providing user profiles, preferences, or visual references at inference time, without updating model parameters. However, direct personalized prompting does not guarantee that the model will reliably exploit such evidence. The predictive distribution under the positive user profile often mixes two sources: personalized signals genuinely supported by the current profile, and the model's generic visual or linguistic priors. As a result, from the positive-profile response alone, it is difficult to determine whether a high-confidence answer is supported by the user profile or merely reflects the model's default preference. To address this problem, we propose a training-free calibrated residual decoding framework. Given the same image and question, we construct three evidence conditions: a positive profile , a counterfactual profile , and an empty profile . Our method keeps the prediction under   as the anchored base, and explicitly estimates the marginal contribution of personalization from score differences across the three conditions. We further introduce normalized-entropy-based uncertainty calibration, allowing the strength of personalized enhancement to adapt to the reliability of the residual signal. Experiments on MMPB, YoLLaVA, and MyVLM show that the proposed method improves personalized multimodal understanding without fine-tuning, with consistent gains on identity-sensitive visual personalization tasks. Additional analysis shows that entropy calibration stabilizes residual decoding when the contrastive personalization signal is uncertain.

## Metadata
- **Published**: 2026-08-23T07:51:24Z
- **Authors**: Jiaao Yu, Yujian Ma, Xianming Hu, Pengran Wang, Ang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22263v1)