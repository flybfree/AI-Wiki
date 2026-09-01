---
title: AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models
published: 2026-08-29T11:44:18Z
authors: Sunghwan Han, Youngtae Han, Youngmin Yi
url: http://arxiv.org/abs/2608.29208v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models

## Abstract
Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to privacy and proprietary concerns. Moreover, although flow-matching-based VLAs have emerged as efficient alternatives to standard diffusion models, current acceleration efforts largely target VLM inference costs, failing to address the iterative ODE solving process inherent in flow matching inference. To address these limitations, we propose AdaVLA, an online, training-free adaptive framework for fast yet accurate flow-matching-based Vision-Language-Action models. We introduce a novel metric derived from the flow matching trajectory curvature to quantify action generation confidence during inference. This metric enables the dynamic reduction of inference steps and the adaptive adjustment of MLP pruning ratios through an efficiently computed importance evaluation, requiring no access to training data. Experimental results on the LIBERO benchmark using a Jetson AGX Orin device demonstrate that our method achieves $1.87\times$ and $2.24\times$ speedups for $π_{0.5}$ and X-VLA, respectively, with negligible degradation in success rates. Furthermore, we validate the robustness of our approach on real-world robotic tasks using SmolVLA.

## Metadata
- **Published**: 2026-08-29T11:44:18Z
- **Authors**: Sunghwan Han, Youngtae Han, Youngmin Yi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29208v1)