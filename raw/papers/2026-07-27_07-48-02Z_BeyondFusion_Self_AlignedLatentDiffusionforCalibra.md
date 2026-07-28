---
title: BeyondFusion: Self-Aligned Latent Diffusion for Calibration-Free Infrared Super-Resolution and Infrared-Visible Fusion
published: 2026-07-27T07:48:02Z
authors: Minchong Chen, Xiaoyun Yuan, Minyu Cao, Jianing Zhang, Jun Zhang, Shuyang Liu, Xiaokang Yang
url: http://arxiv.org/abs/2607.24110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BeyondFusion: Self-Aligned Latent Diffusion for Calibration-Free Infrared Super-Resolution and Infrared-Visible Fusion

## Abstract
Mobile infrared-visible imaging typically pairs a compact infrared sensor with a high-resolution visible camera for complementary perception. While cross-sensor misalignment caused by different optics, viewpoints, fields of view, and exposure timings hinders practical deployment. In this paper, we propose BeyondFusion, a unified latent diffusion framework for calibration-free visible-guided infrared super-resolution and infrared-visible fusion tasks. The proposed framework supports both task-specific training and joint training where two tasks are optimized and executed as two readouts of the same generative process. Instead of relying on explicit registration or geometric warping, BeyondFusion introduces a cross-modal self-aligning (CMSA) module into the denoising U-Net. CMSA reorganizes infrared and visible latent tokens into a shared attention space to learn content-adaptive cross-modal correspondence during the denoising process. Together with misalignment augmentation module, the model is facilitated to exploit visible structural and semantic cues while preserving thermal consistency, enabling high-frequency infrared reconstruction and informative fused-image generation under uncalibrated conditions. Extensive experiments on public benchmarks and a mobile infrared-visible imaging system show strong performance across aligned inputs, low-resolution infrared observations, synthetic misalignments, and real mobile captures with unsynchronized sensors. Ablation studies, unified training analysis, and downstream pedestrian detection further validate the effectiveness of BeyondFusion for calibration-free multimodal imaging.

## Metadata
- **Published**: 2026-07-27T07:48:02Z
- **Authors**: Minchong Chen, Xiaoyun Yuan, Minyu Cao, Jianing Zhang, Jun Zhang, Shuyang Liu, Xiaokang Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24110v1)