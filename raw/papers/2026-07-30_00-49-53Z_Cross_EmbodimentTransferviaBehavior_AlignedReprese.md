---
title: Cross-Embodiment Transfer via Behavior-Aligned Representations
published: 2026-07-30T00:49:53Z
authors: Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale, Dorsa Sadigh
url: http://arxiv.org/abs/2607.27549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Embodiment Transfer via Behavior-Aligned Representations

## Abstract
Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions, end-effector traces of robot motion) in vision-language-action (VLA) models to promote cross-embodiment transfer. We hypothesize that by possessing invariances across embodiments while being predictive of robot actions, these representations can help unify large-scale cross-embodiment data to enhance transfer. To assess our hypothesis, we develop a simulation-based benchmark designed to assess transfer with diverse cross-embodiment data to new embodiments. Using this benchmark, we compare different representations and ways of incorporating them. We identify that end-effector traces can be particularly beneficial for transfer, representations are generally more useful with larger prior datasets, and can be used to benefit from action-free data. We also demonstrate that they can enhance sim-to-real cross-embodiment transfer, improving task completion progress of real robot policies pre-trained on simulation data by 28%. We provide videos of our evaluations at our website: https://ajaysridhar.com/barx/.

## Metadata
- **Published**: 2026-07-30T00:49:53Z
- **Authors**: Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale, Dorsa Sadigh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27549v1)