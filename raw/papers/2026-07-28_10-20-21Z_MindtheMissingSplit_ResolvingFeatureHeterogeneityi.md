---
title: Mind the Missing Split: Resolving Feature Heterogeneity in Swarm Learning with Random Forests
published: 2026-07-28T10:20:21Z
authors: Mohammad Tajabadi, Dominik Heider
url: http://arxiv.org/abs/2607.25538v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Missing Split: Resolving Feature Heterogeneity in Swarm Learning with Random Forests

## Abstract
Swarm Learning is a decentralized collaborative learning mechanism that allows multiple organizations to train a shared model without central coordination or direct data sharing. In typical horizontal Swarm Learning, datasets across sites are usually assumed to share the same feature set. However, in real-world applications, sites often have partially overlapping features because measurements, protocols, and available covariates differ across sites. This feature heterogeneity creates a practical issue for machine learning algorithms such as Random Forests. Specifically, when decision trees are pooled into a global Random Forest, inference at a given site can become ill-defined if a traversal encounters a split on a feature that is not available locally, often forcing organizations to discard site-specific variables upfront. In this paper, we address feature heterogeneity in Swarm Learning with Random Forests under partially overlapping feature spaces. We propose several deterministic and probabilistic inference-time strategies that resolve such missing splits without restricting training to the intersection of features. We evaluate the methods on nine datasets and demonstrate that they outperform both the intersection baseline and locally trained models across a broad range of scenarios.

## Metadata
- **Published**: 2026-07-28T10:20:21Z
- **Authors**: Mohammad Tajabadi, Dominik Heider
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25538v1)