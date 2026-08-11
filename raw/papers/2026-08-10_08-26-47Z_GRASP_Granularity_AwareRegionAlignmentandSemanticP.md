---
title: GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views
published: 2026-08-10T08:26:47Z
authors: Jiahui Cui, Yan Zhao, Kan Wei, Enze Zhu, Peirong Zhang, Lei Wang, Yiru Wang
url: http://arxiv.org/abs/2608.09270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views

## Abstract
Fine-grained cross-modal understanding in drone views is essential for aerial vision-language navigation. However, the inherent wide field of view and overhead perspective of drone scenarios impose dual challenges on vision-language understanding. At the macro level, overwhelming background clutter in visual representations leads to Cross-Modal Focus Misalignment, where the model prioritizes global environmental similarities over specific object details. At the micro level, Visual Isomorphism creates ambiguity, where candidates share similar geometric structures yet differ only in subtle attributes. To address these challenges, we propose the Granularity-Aware Region Alignment and Semantic Prototype (GRASP) learning framework, enhancing discriminative capability through two synergistic strategies. Specifically, we introduce Region-Focused Alignment (RFA) to promote object-centric cross-modal alignment while suppressing background interference. Concurrently, to tackle visual isomorphism, we propose Semantic Perturbation Enhanced Matching (SPEM), which leverages a foreground-purified Semantic Prototype Codebook (SPC) to construct semantically perturbed negatives for fine-grained semantic discrimination. Extensive experiments on the GeoText-1652 benchmark and the unseen ERA dataset demonstrate that GRASP achieves competitive performance in drone-view fine-grained image-text retrieval, validating its effectiveness for cross-modal understanding in aerial scenarios. Our code implementation is available at https://github.com/UCAS-JC/GRASP.

## Metadata
- **Published**: 2026-08-10T08:26:47Z
- **Authors**: Jiahui Cui, Yan Zhao, Kan Wei, Enze Zhu, Peirong Zhang, Lei Wang, Yiru Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09270v1)