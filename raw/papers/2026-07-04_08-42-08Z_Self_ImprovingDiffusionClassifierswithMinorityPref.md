---
title: Self-Improving Diffusion Classifiers with Minority Preference Optimization
published: 2026-07-04T08:42:08Z
authors: Hyunsoo Kim, Jungmyung Wi, Soobin Um, Donghyun Kim, Suhyun Kim
url: http://arxiv.org/abs/2607.03770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Improving Diffusion Classifiers with Minority Preference Optimization

## Abstract
Prior studies have demonstrated that diffusion classifiers achieve robust zero-shot classification performance. However, their effectiveness is strongly tied to the pretraining data distribution: they perform well in majority, high-density regions of the data manifold, but are significantly less accurate in minority, low-density regions. Although prior works on minority sampling have focused on generating more minority-like images, what minority sampling fundamentally enables beyond generation remains underexplored. In this paper, we reveal a direct relationship between minority sampling in generation and the perception capability of diffusion classifiers. Specifically, we show that enhancing minority sampling broadens the coverage of underrepresented regions on the data manifold, thereby improving diffusion-based recognition. To exploit this connection, we propose \textit{Self-Improving Diffusion Classifiers with Minority Preference Optimization} (MiPO), which fine-tunes a pretrained diffusion model using minority preference rewards. Using only arbitrary caption data, MiPO generates candidate samples, rewards those that better cover minority regions, and optimizes the model with LoRA and Group Relative Policy Optimization, without additional image data, external foundation models, or external reward models. This enables stable, prompt-adaptive minority sampling and translates low-density generative coverage into improved zero-shot diffusion classification. To sum up, we show that diffusion classifier perception is biased toward majority regions, demonstrate that this bias can be alleviated through minority preference optimization, and evaluate MiPO on five standard datasets.

## Metadata
- **Published**: 2026-07-04T08:42:08Z
- **Authors**: Hyunsoo Kim, Jungmyung Wi, Soobin Um, Donghyun Kim, Suhyun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03770v1)