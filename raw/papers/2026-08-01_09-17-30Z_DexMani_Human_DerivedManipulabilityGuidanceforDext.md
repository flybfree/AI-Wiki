---
title: DexMani: Human-Derived Manipulability Guidance for Dexterous Rotation
published: 2026-08-01T09:17:30Z
authors: Xiaoyang Chen, Shengcheng Luo, Haoran Guo, Jiaming Jiang, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
url: http://arxiv.org/abs/2608.00554v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DexMani: Human-Derived Manipulability Guidance for Dexterous Rotation

## Abstract
Dexterous object rotation is a sequential contact problem: each support, release, and re-contact decision must both produce the desired object motion, and prepare the hand configuration for continued rotation. Existing reinforcement learning methods discover such movement patterns through trial and error on specific robotic hand embodiments, without explicitly accounting for how each contact transition affects the hand's ability to sustain object rotation in subsequent steps. We introduce DexMani, a framework that transfers human demonstrations as contact-conditioned manipulability evolution. This prior captures how successful human contact transitions reshape the object-rotation directions available to the hand. DexMani then learns this manipulability evolution and uses it to guide downstream reinforcement learning, enabling rotation skills to be acquired across robot embodiments with distinct kinematics and active-contact configurations. Across the Shadow Hand, Allegro Hand, and XHand, DexMani achieves the highest success rates in every evaluated setting for both seen and unseen objects. DexMani reaches an average success rate of 57.5% on LEAP Hand, outperforming other baselines and producing smoother rotatory motions. Project site: https://dexmani.github.io

## Metadata
- **Published**: 2026-08-01T09:17:30Z
- **Authors**: Xiaoyang Chen, Shengcheng Luo, Haoran Guo, Jiaming Jiang, Wanlin Li, Ziyuan Jiao, Chenxi Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00554v1)