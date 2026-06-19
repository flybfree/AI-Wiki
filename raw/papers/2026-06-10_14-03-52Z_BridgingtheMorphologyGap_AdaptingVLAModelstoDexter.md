---

title: "Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning"
published: "2026-06-10T14:03:52Z"
authors: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
url: http://arxiv.org/abs/2606.12109v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning



**Source**: [Original Paper](http://arxiv.org/abs/2606.12109v1)
## Abstract
Vision-Language-Action (VLA) models have demonstrated remarkable zero-shot generalization in robotic manipulation, yet the vast majority of pre-trained pipelines remain strictly confined to low-DoF parallel grippers. Adapting these rich semantic priors to high-DoF dexterous hands introduces a severe morphology gap, direct end-to-end joint fine-tuning inherently causes catastrophic forgetting of spatial reasoning and acute action manifold collapse due to data scarcity. In this paper, we present InDex, a novel, data-efficient adaptation framework rooted in cross-morphology semantic inheritance. Rather than discarding the pre-trained 1-DoF parallel grasp output, we repurpose it as a continuous, macroscopic virtual grasp intent proxy to sequentialize the control topology. We implement a two-stage decoupled learning architecture: the first stage parameter-efficiently aligns the VLA backbone to predict continuous arm trajectories and the scalar grasp intent; the second stage freezes this spatial backbone and leverages an intent-conditioned denoising diffusion head to decode fine-grained joint articulations for multi-fingered end-effectors. Extensive simulation benchmarks across a suite of multi-stage, contact-rich dexterous manipulation tasks demonstrate that InDex effectively masters intricate skills with minimal demonstration data, substantially outperforming monolithic baselines while preserving the robust spatial generalizability of the original VLA prior.

## Metadata
- **Published**: 2026-06-10T14:03:52Z
- **Authors**: Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu, Xilun Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.12109v1)