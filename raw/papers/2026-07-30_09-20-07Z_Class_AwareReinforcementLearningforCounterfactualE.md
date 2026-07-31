---
title: Class-Aware Reinforcement Learning for Counterfactual Explanation Generation
published: 2026-07-30T09:20:07Z
authors: Muhammad Adil Saleem, Syed Ali Raza, Mary-Anne Williams
url: http://arxiv.org/abs/2607.27905v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Class-Aware Reinforcement Learning for Counterfactual Explanation Generation

## Abstract
Counterfactual explanations (CFEs) enhance the interpretability of black-box models by generating alternative instances with adjusted feature values that achieve a contrastive outcome. Reinforcement learning (RL) offers a promising approach for CFE generation, enabling efficient exploration of counterfactual instances while ensuring control over key metrics like validity, sparsity, and proximity. Previous studies have formulated RL states exclusively using features derived from the predictors in the supervised dataset. This study explores the impact of including an instance's predicted class, alongside features derived from the predictors, in the RL state representation for generating CFEs. The hypothesis is that class-awareness enhances exploration efficiency and improves policy optimality. We compare the proposed class-aware RL method with the class-blind RL method, which is similar but excludes the instance's class information from the state representation. The comparison was conducted using seven datasets from diverse domains, varying in size. The results show that during training, class-aware RL offers benefits in terms of convergence speed, reward optimization, and episode length reduction. Moreover, it generates significantly more valid CFEs compared to class-blind RL. Finally, the instance's class-based feature consistently ranks among the most influential predictors in RL's action-selection, as shown by the SHAP and LIME values, underscoring the significance of class-awareness in RL for CFE generation. The impact is heightened clarity, faster learning, improved validity, and more effective counterfactual generation across diverse datasets.

## Metadata
- **Published**: 2026-07-30T09:20:07Z
- **Authors**: Muhammad Adil Saleem, Syed Ali Raza, Mary-Anne Williams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27905v1)