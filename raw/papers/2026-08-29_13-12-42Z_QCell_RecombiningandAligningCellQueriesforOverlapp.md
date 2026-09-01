---
title: QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation
published: 2026-08-29T13:12:42Z
authors: Yaroslav Prytula, Anton Popov, Dmytro Fishman
url: http://arxiv.org/abs/2608.29253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation

## Abstract
Instance segmentation of overlapping cells in microscopy remains challenging due to semi-transparent structures that produce weak boundaries and mixed visual evidence in overlap regions. Existing methods address this through local regions of interest or shape priors but lack global reasoning across overlapping objects. We present QCell, a novel query-based model that de-overlaps cell instances in microscopy scenes. Our approach combines (i) an instance recombination module that decomposes and recombines query representations in latent space, enabling the model to reason about complete object structure under overlap, and (ii) a contrastive query alignment objective that combines distinctive instance feature learning and separation of overlapping cell queries. We additionally introduce a new Organoid dataset benchmark for overlapping cell segmentation. We show that QCell outperforms state-of-the-art methods across multiple benchmarks, achieving +2.2 AP and +2.7 AJI on ISBI2014. Code is available at https://github.com/SlavkoPrytula/QCell

## Metadata
- **Published**: 2026-08-29T13:12:42Z
- **Authors**: Yaroslav Prytula, Anton Popov, Dmytro Fishman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29253v1)