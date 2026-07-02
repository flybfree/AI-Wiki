---
title: Group-invariant Coresets for Data-efficient Active Learning
published: 2026-07-01T15:46:16Z
authors: L. C. Ayres, J. C. M. Bermudez, S. J. M. de Almeida, R. A. Borsoi
url: http://arxiv.org/abs/2607.01089v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Group-invariant Coresets for Data-efficient Active Learning

## Abstract
Active learning reduces labeling cost by querying the most informative unlabeled samples, but standard coreset methods ignore known data symmetries and can waste budget on transformed versions of the same instance. We propose GRINCO, a group-invariant coreset framework that performs acquisition in the quotient space induced by a transformation group, so that selection operates on orbits rather than raw samples. The method uses either canonical representatives or learned orbit-separating invariant embeddings to define practical quotient metrics, and combines quotient-space k-center selection with invariant training through an orbit-averaged loss. We further derive a generalization bound that relates excess orbit-averaged risk to quotient-space coverage, label uncertainty, and intra-orbit variability. Experiments on synthetic scale-invariant data and image benchmarks with rotation-induced redundancy show that GRINCO improves orbit coverage and achieves stronger label efficiency than conventional coreset baselines, especially when group-induced redundancy is substantial.

## Metadata
- **Published**: 2026-07-01T15:46:16Z
- **Authors**: L. C. Ayres, J. C. M. Bermudez, S. J. M. de Almeida, R. A. Borsoi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01089v1)