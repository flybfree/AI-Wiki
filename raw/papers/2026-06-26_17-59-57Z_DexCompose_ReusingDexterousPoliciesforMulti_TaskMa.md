---
title: DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand
published: 2026-06-26T17:59:57Z
authors: Dihong Huang, Zhenyu Wei, Zhuxiu Xu, Yunchao Yao, Sikai Li, Mingyu Ding
url: http://arxiv.org/abs/2606.28323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand

## Abstract
Dexterous manipulation policies can solve individual skills, but composing them to perform multiple tasks with a single hand remains challenging. Adding a new task on top of an existing manipulation skill often imposes conflicting demands on overlapping fingers and contact modes, causing destructive interference between preserving an existing manipulation outcome and executing a new one. We propose DexCompose, a role-aware residual composition framework that reuses pretrained dexterous policies for multi-task manipulation through explicit finger-level action ownership. Given two pretrained full-hand policies, DexCompose first collects successful post-task states from the first skill and performs release tests over candidate finger masks to identify which fingers are necessary for maintaining the established skill state. It then trains two asymmetric residual modules: a bounded residual stabilizer for task preservation, and a context-aware residual that adapts the frozen downstream policy only within the action subspace assigned to the new task. We evaluate the framework on 16 composite dexterous manipulation tasks spanning four object-retention skills and four downstream interactions. DexCompose achieves a 77.4% average composite success rate, demonstrating that structural action ownership with dual residuals offers a promising direction for composing dexterous skills beyond conventional policy chaining.

## Metadata
- **Published**: 2026-06-26T17:59:57Z
- **Authors**: Dihong Huang, Zhenyu Wei, Zhuxiu Xu, Yunchao Yao, Sikai Li, Mingyu Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.28323v1)