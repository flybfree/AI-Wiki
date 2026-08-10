---
title: Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts
published: 2026-08-07T03:43:37Z
authors: Rulin Zhou, Wanhao Liu, Guoheng Ma, Liangjin Shao, Qiujie Song, Yidu Wang, Guankun Wang, Tong Chen, Long Bai, Luping Zhou, Hongliang Ren
url: http://arxiv.org/abs/2608.06770v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts

## Abstract
Controllable surgical world models can provide a generative foundation for surgical artificial intelligence and simulation by synthesizing realistic instrument--tissue interactions. However, existing methods lack a unified multimodal control paradigm, while direct fusion of heterogeneous visual conditions often causes anatomical distortion, instrument appearance drift, and temporally inconsistent interactions. In this work, we propose {Surg-UniWorld}, a unified surgical world model with multimodal control experts. Surg-UniWorld first constructs a {Hierarchical Surgical Anchor} from first-frame appearance and hierarchical semantic masks to preserve persistent scene identity, anatomical organization, and interaction boundaries. {Anchor-Relative Modality Experts} then interpret edge, depth, and optical-flow evidence relative to the shared anchor, capturing complementary boundary, geometric, and motion information. A {Multimodal Control Expert} further performs contribution-preserving stage-wise composition of the activated modality increments and generates control hints for the Wan2.2 video diffusion backbone. To support multimodal surgical world modeling, we further construct Cholec80-SurgWAM, a benchmark for controllable surgical video generation. Extensive experiments demonstrate that Surg-UniWorld consistently outperforms existing controllable video generation methods and surgical world-model baselines in generation quality, temporal consistency, and multimodal controllability.

## Metadata
- **Published**: 2026-08-07T03:43:37Z
- **Authors**: Rulin Zhou, Wanhao Liu, Guoheng Ma, Liangjin Shao, Qiujie Song, Yidu Wang, Guankun Wang, Tong Chen, Long Bai, Luping Zhou, Hongliang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06770v1)