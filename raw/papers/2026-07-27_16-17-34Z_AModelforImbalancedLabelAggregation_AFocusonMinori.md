---
title: A Model for Imbalanced Label Aggregation: A Focus on Minority-Class Detection
published: 2026-07-27T16:17:34Z
authors: Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, Argyris Kalogeratos
url: http://arxiv.org/abs/2607.24622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Model for Imbalanced Label Aggregation: A Focus on Minority-Class Detection

## Abstract
We study imbalanced crowdsourcing with a focus on class-dependent annotator accuracy, a setting that, to the best of our knowledge, remains relatively underexplored despite its importance in real-world inspection systems where the labels of greatest operational importance are also the rarest ones. In this setting, annotators may be reliable on both classes, unreliable on both classes, majority-class specialists, or minority-class specialists. Existing models only partially address this problem: they either capture class-dependent errors but ignore item difficulty, or they model item difficulty without capturing class-dependent errors. To fill this gap for imbalanced datasets in crowdsourcing, we introduce a generative aggregation model combining item difficulty with class-dependent annotator competence. The model allows both annotator abilities and item difficulties to vary across classes. We then revisit Condorcet's Jury Theorem in the class-imbalanced setting. We also show that majority voting asymptotically preserves the underlying class proportion. We evaluate our model on $33$ real-world crowdsourcing datasets, covering multiclass tasks such as images and text, as well as two large-scale regimes: large-scale annotation datasets, with many annotations per item, and large-scale item datasets, with a large number of annotated instances. Across these diverse settings, our model consistently achieves the highest minority recall while remaining competitive in balanced accuracy, making it particularly relevant when rare-label recovery is the primary objective.

## Metadata
- **Published**: 2026-07-27T16:17:34Z
- **Authors**: Gabriel Singer, Samuel Gruffaz, Olivier Vo Van, Nicolas Vayatis, Argyris Kalogeratos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24622v1)