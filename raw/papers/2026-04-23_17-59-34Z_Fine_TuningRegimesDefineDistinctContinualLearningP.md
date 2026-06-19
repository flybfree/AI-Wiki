---

title: Fine-Tuning Regimes Define Distinct Continual Learning Problems
published: "2026-04-23T17:59:34Z"
authors: Paul-Tiberiu Iordache, Elena Burceanu
url: http://arxiv.org/abs/2604.21927v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Fine-Tuning Regimes Define Distinct Continual Learning Problems



**Source**: [Original Paper](http://arxiv.org/abs/2604.21927v1)
## Abstract
Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.

## Metadata
- **Published**: 2026-04-23T17:59:34Z
- **Authors**: Paul-Tiberiu Iordache, Elena Burceanu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2604.21927v1)