---
title: Element-Aware Group Learning for E-Commerce Image Generation
published: 2026-08-01T10:45:03Z
authors: Jingtong Chen, Jiahui Wang, Xue Zhao, ShaoGuo Liu, Minghao Li
url: http://arxiv.org/abs/2608.00584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Element-Aware Group Learning for E-Commerce Image Generation

## Abstract
Recent advances in image generation and editing have made prompt quality a key bottleneck for e-commerce creatives. Vision-language models (VLMs) can generate image-editing prompts from product images and metadata, but further improving their prompt-writing capabilities requires post-training with feedback from the generated images. Group Relative Policy Optimization (GRPO) is a natural framework for such outcome-level reward optimization. However, it assigns credit only at the full-prompt level, even though image quality often depends on specific design elements such as composition, background, and the presentation of selling points. Existing fine-grained credit assignment methods typically require step-level supervision or learned critics. To address this, we propose EAGLE-GRPO (Element-Aware Group Learning for E-Commerce Image Generation), which decomposes the group-centered reward over predefined elements. We cast element-level credit assignment as a kernel ridge regression problem and derive a closed-form solution, without additional rollouts or separate credit-assignment models. This yields interpretable per-element advantages and more precise policy updates. Experiments show that EAGLE-GRPO sustains performance gains over more training steps before plateauing and generates prompts that produce higher-quality e-commerce images than competitive VLM prompt-writing baselines.

## Metadata
- **Published**: 2026-08-01T10:45:03Z
- **Authors**: Jingtong Chen, Jiahui Wang, Xue Zhao, ShaoGuo Liu, Minghao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00584v1)