---
title: FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference
published: 2026-07-30T08:23:52Z
authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Qianli Ma, Fanshuai Meng, Weijia Jia
url: http://arxiv.org/abs/2607.27842v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference

## Abstract
Diffusion models are widely used to generate high-quality images and videos, but their iterative denoising process remains computationally intensive. A growing class of training-free accelerators reduces this cost by reusing cached intermediate features or forecasting future ones. To control draft drift, these methods sometimes compute an exact block feature for verification. Yet the resulting exact feature is typically used only to measure discrepancy or guide a later decision and is then discarded. We find that this previously computed feature can instead be reused for correction. Forwarding it at the verification site resets the local draft residual and reduces downstream feature error. Based on this observation, we introduce FeatFix, a local exact-feature correction method for cached diffusion inference. FeatFix operates at a fixed sparse set of layer--timestep sites. At each selected site, it replaces the complete draft block output with the exact output computed from the same incoming state, avoiding token- or channel-level partial replacement and full-timestep recomputation. Experiments across four image and video backbones show that FeatFix consistently accelerates generation, achieving a speedup of up to $6.70\times$ over Vanilla while maintaining competitive output quality.

## Metadata
- **Published**: 2026-07-30T08:23:52Z
- **Authors**: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Qianli Ma, Fanshuai Meng, Weijia Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27842v1)