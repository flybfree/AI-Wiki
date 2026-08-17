---
title: Catching the Imposter: Self-Supervised Learning of Physical Coherence with Cross-Entity Feature Permutations
published: 2026-08-14T15:15:19Z
authors: Aleksei Rozanov, Arvind Renganathan, Vipin Kumar
url: http://arxiv.org/abs/2608.14372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Catching the Imposter: Self-Supervised Learning of Physical Coherence with Cross-Entity Feature Permutations

## Abstract
Scientific data often describe entities whose features are jointly governed by the laws of physics, yet existing self-supervised learning (SSL) objectives largely ignore this physical coherence. We introduce imposter, a discriminative pretext task that replaces subsets of an entity's features with real observations donated by another entity and trains the encoder to identify the swapped features. Because every donated value is individually plausible, the task can only be solved by learning cross-feature physical dependencies. We evaluate the proposed objectives on global ERA5-Land reanalysis data using 21 environmental variables and assess the learned representations on seven downstream tasks spanning climate classification, carbon flux estimation, and streamflow prediction. Our study includes, to our knowledge, the first systematic comparison of self-supervised objectives for land-surface modeling under a shared architecture and pre-training budget. We find that the most effective pretext task depends on the downstream task family rather than any single objective's superiority, and that imposter provides complementary information when combined with existing SSL objectives. These results suggest that physical coherence is a valuable new source of self-supervision for scientific foundation models.

## Metadata
- **Published**: 2026-08-14T15:15:19Z
- **Authors**: Aleksei Rozanov, Arvind Renganathan, Vipin Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14372v1)