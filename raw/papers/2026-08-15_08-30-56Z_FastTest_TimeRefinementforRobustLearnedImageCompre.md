---
title: Fast Test-Time Refinement for Robust Learned Image Compression
published: 2026-08-15T08:30:56Z
authors: Jiaming Liang, Chi-Man Pun, Weisi Lin
url: http://arxiv.org/abs/2608.15113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast Test-Time Refinement for Robust Learned Image Compression

## Abstract
Learned image compression (LIC) has demonstrated remarkable rate-distortion (RD) performance in benign settings. However, the high representational capacity endowed by deep neural networks (DNNs) comes at the expense of increased adversarial vulnerability. This hinders their adoption as trusted standardized codecs. Recent work has sketched test-time refinement (TTR) as a defense in gray-box scenarios, despite its original purpose of improving benign RD performance. Unfortunately, extensive iterations of TTR incur prohibitive overhead, while the robustness mechanism lacks theoretical understanding. Moreover, TTR has not been evaluated in white-box settings or against attacks beyond $\ell_2$-bounded rate and untargeted distortion objectives. To bridge these gaps, we present a systematic study. Our study reveals an Asymmetric Adversarial Trajectory (AAT) property in LIC systems: transitioning from adversarial to benign regions is significantly easier than the reverse process, where adversarial examples can often be roughly recovered within only 1-2 steps. We provide a two-dimensional Tube Model to explain this phenomenon. Based on AAT, we propose a Fast Test-Time Refinement (FTTR) framework for practical and robust LIC systems. We establish that the robustness arises from the contraction of adversarial regions induced by the Input-as-Label property of LIC systems, rather than from obfuscated gradients. Extensive evaluations with diverse strong adaptive attacks across multiple LIC systems demonstrate the promise of the proposed FTTR framework. The code is available at https://github.com/chinaliangjiaming/FTTR.git.

## Metadata
- **Published**: 2026-08-15T08:30:56Z
- **Authors**: Jiaming Liang, Chi-Man Pun, Weisi Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15113v1)