---
title: Recurrent Neural Networks Beyond Time: Learning from Multiple Ordered Projections
published: 2026-08-10T14:56:20Z
authors: Vagan Terziyan, Artur Terziian, Oleksandra Vitko
url: http://arxiv.org/abs/2608.09690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recurrent Neural Networks Beyond Time: Learning from Multiple Ordered Projections

## Abstract
Recurrent neural networks (RNNs) are widely used for sequence learning, yet their application is commonly associated with temporal data, although recurrent computation fundamentally operates on ordered sequences rather than on time itself. Building on this observation, we introduce the Ordered Structural Dependency Hypothesis (OSDH), which proposes that multiple admissible orderings of the same observations may reveal complementary structural dependencies inaccessible through a single sequential organization. To operationalize this hypothesis, we propose the Independent Structural Expert Principle (ISEP), whereby projection-specific sequence models are trained independently before their learned representations are integrated through a dedicated fusion model. As a concrete realization, we present Structural Evolution RNNs (SE-RNNs), which employ conventional RNNs as projection-specific structural experts while preserving the underlying recurrent computation unchanged. Proof-of-concept experiments on three synthetic datasets with substantially different levels of structural complexity demonstrate that the proposed architecture consistently benefits from multiple ordered projections when hidden structural dependencies are present, while remaining competitive on simpler datasets. Since OSDH is independent of the underlying sequence-processing model, the proposed framework naturally extends beyond recurrent networks and may be instantiated using alternative architectures. The results suggest a general computational perspective for exploiting complementary ordered representations across diverse structured learning problems.

## Metadata
- **Published**: 2026-08-10T14:56:20Z
- **Authors**: Vagan Terziyan, Artur Terziian, Oleksandra Vitko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09690v1)