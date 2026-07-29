---
title: I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models
published: 2026-07-28T10:05:11Z
authors: Yimao Guo, Zuomin Qu, Wei Lu
url: http://arxiv.org/abs/2607.25522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models

## Abstract
The rapid advancement of video generation models has led to the increasing misuse of image-to-video (I2V) models. Although substantial progress has been made in detecting AI-generated videos, proactive defenses against I2V models remain underexplored. In particular, current proactive defenses against I2V models predominantly rely on gradient-based adversarial attacks, which require defenders to possess GPUs with substantial memory resources (VRAM) to generate adversarial examples. To address this issue, we propose I2VShield, a privacy protection method based on generative adversarial attacks tailored to Diffusion Transformer (DiT)-based I2V models. The proposed method primarily consists of two components: (1) a text-adaptive perturbation generation framework integrating adversarial learning to mitigate computational overhead while maintaining visual imperceptibility; and (2) an untargeted Multimodal Attention Disruption (MAD) attack that exploits the inherent vulnerabilities of DiT-based I2V models, maximizing the deviation of the internal attention features from their clean states. Extensive experiments demonstrate that our approach achieves highly competitive protection performance across various datasets and mainstream DiT-based I2V models, particularly in disrupting spatiotemporal coherence, while substantially reducing computational costs.

## Metadata
- **Published**: 2026-07-28T10:05:11Z
- **Authors**: Yimao Guo, Zuomin Qu, Wei Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25522v1)