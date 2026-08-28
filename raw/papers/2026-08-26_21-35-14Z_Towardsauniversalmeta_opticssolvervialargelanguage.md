---
title: Towards a universal meta-optics solver via large language models
published: 2026-08-26T21:35:14Z
authors: Huanshu Zhang, Lei Kang, Yuyan Chen, Luxiang Wang, Zhaolong Cao, Douglas H. Werner
url: http://arxiv.org/abs/2608.26417v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards a universal meta-optics solver via large language models

## Abstract
Metasurface design increasingly requires fast models that can operate across structurally distinct device families, rather than retraining a separate surrogate for every geometry class. Conventional neural network surrogates often depend on fixed-dimensional descriptors, family-specific output formats, and repeated architecture tuning, which limits their scalability across heterogeneous meta-atoms. Here, we present a unified large language model (LLM) workflow for multi-family metasurface modeling and inverse-design. Geometries, design parameters, and optical response channels were converted into a shared instruction-following text format and used to fine-tune Gemma-2-9B across 8 metasurface families. Compared with single-family baselines, the joint model simultaneously predicted the optical responses of all metasurface families while reducing the MSE for each family by an average of 56.5%. The same representation was also used for inverse design. These results show that a shared sequence-based LLM interface can provide a practical route to cross-family metasurface design while reducing the need for task-specific surrogate architectures.

## Metadata
- **Published**: 2026-08-26T21:35:14Z
- **Authors**: Huanshu Zhang, Lei Kang, Yuyan Chen, Luxiang Wang, Zhaolong Cao, Douglas H. Werner
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26417v1)