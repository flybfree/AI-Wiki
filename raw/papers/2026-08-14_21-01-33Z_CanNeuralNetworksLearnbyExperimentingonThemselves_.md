---
title: Can Neural Networks Learn by Experimenting on Themselves? Self-Interventional Learning from Functional Consequences to Predictive Self-Knowledge
published: 2026-08-14T21:01:33Z
authors: Michał Tomaszewski
url: http://arxiv.org/abs/2608.14894v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Neural Networks Learn by Experimenting on Themselves? Self-Interventional Learning from Functional Consequences to Predictive Self-Knowledge

## Abstract
Machine-learning systems usually model external data, while their internal functional organization is analyzed by external observers. This work introduces Self-Interventional Learning (SIL), in which a neural system perturbs its own functional structure, observes consequences, learns a predictive self-model, generalizes to unexecuted interventions, and uses predictions to guide later structural action. In a construction-known synthetic system, SIL recovered critical structure, redundancy, and replaceability, while synergy was not reliably recovered. Across 30 fresh confirmatory seeds, increasing the pairwise intervention budget from 4 to 56 reduced held-out prediction error from 0.0335 to 0.0148 and increased Spearman correlation from 0.629 to 0.883. In a matched ablation, preserving the correct intervention--consequence mapping reduced prospective prediction error by 81.3%, while using the same learned self-model for action reduced normalized regret by 31.7% relative to ignoring it. However, model-guided action did not significantly outperform a direct empirical-memory policy, and powered CIFAR-10/ResNet validation showed no robustness advantage over equal-budget direct repair search. These results support SIL as an intervention-driven framework for learning predictive knowledge about a network's own functional organization, while showing that the self-model remains incomplete and is not universally superior to simpler direct strategies.

## Metadata
- **Published**: 2026-08-14T21:01:33Z
- **Authors**: Michał Tomaszewski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14894v1)