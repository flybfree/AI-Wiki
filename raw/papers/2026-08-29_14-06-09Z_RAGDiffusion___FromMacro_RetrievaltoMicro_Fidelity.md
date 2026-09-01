---
title: RAGDiffusion++: From Macro-Retrieval to Micro-Fidelity Alignment for Garment Generation
published: 2026-08-29T14:06:09Z
authors: Yuhan Li, Xianfeng Tan, Fangao Zeng, Wenxiang Shang, Pipei Huang, Hao Zhou, Zhiyu Jin, Wenjun Zhang, Bingbing Ni
url: http://arxiv.org/abs/2608.29280v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAGDiffusion++: From Macro-Retrieval to Micro-Fidelity Alignment for Garment Generation

## Abstract
Standard clothing asset generation---restoring forward-facing flat-lay garment images from diverse real-world contexts---holds immense commercial value yet demands both macroscopic topological accuracy and microscopic physical fidelity. Although our previous work RAGDiffusion effectively eradicated large-scale structural hallucinations via retrieval-augmented macro-constraints, achieving industrial-grade micro-texture realism remains an unsolved bottleneck. We formally identify this limitation as High-Frequency Trajectory Collapse: supervised fine-tuning (SFT) converges to the conditional mean of the training distribution, which is dominated by smooth, low-frequency textures, causing high-frequency patterns (e.g., fabric weaves, intricate logos) to become nearly un-sampleable. Naively applying Reinforcement Learning (RL) post-training further triggers Artifact Hacking, where models exploit semantic biases in generic reward models by generating deceptive checkerboard noise. Our key insight is that RL can fundamentally reshape the sampling distribution of flow models---elevating the probability of high-fidelity trajectories under accurate reward guidance---while adversarial regularization prevents exploitation of reward blind spots. Realizing this principle requires three prerequisites: (i)inherent capacity, established through a 27,725-pair high-complexity garment dataset (STGarment-Plus) and a Dual-Image-Stream FLUX architecture upgrade; (ii)perceptive reward, provided by a novel attribute-aware reward model (Garment-RM) trained on 500K images via fine-grained contrastive learning, achieving 84.67% human preference accuracy; and (iii)hacking prevention, enforced by our Adversarial-Regularized GRPO (AR-GRPO) strategy that integrates a dynamic discriminator into the RL sampling trajectory to penalize artifacts while enriching authentic high-frequency details.

## Metadata
- **Published**: 2026-08-29T14:06:09Z
- **Authors**: Yuhan Li, Xianfeng Tan, Fangao Zeng, Wenxiang Shang, Pipei Huang, Hao Zhou, Zhiyu Jin, Wenjun Zhang, Bingbing Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29280v1)