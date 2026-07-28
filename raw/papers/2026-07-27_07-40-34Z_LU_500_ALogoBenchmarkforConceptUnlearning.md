---
title: LU-500: A Logo Benchmark for Concept Unlearning
published: 2026-07-27T07:40:34Z
authors: Keyu Li, Jin Gao, Jialing Zhang, Dequan Wang
url: http://arxiv.org/abs/2607.24101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LU-500: A Logo Benchmark for Concept Unlearning

## Abstract
Concept unlearning is increasingly used to limit the reproduction of protected or unsafe visual concepts in text-to-image models. Existing evaluations, however, mostly study targets that dominate the whole image, such as styles, broad object categories, or portrait-like identities, leaving company logos comparatively underexamined. Logos create a different failure mode: a small localized mark can carry the entire protected concept, must be visually precise to remain recognizable, and can be triggered implicitly by products, storefronts, packaging, or advertisements even when the word ``logo'' is absent. We introduce LU-500, a logo-unlearning benchmark built from Fortune Global 500 companies to study this localized and semantically entangled setting. LU-500 contains nearly 10,000 curated text-query and logo-image pairs, with an explicit track (LUex-500) and an implicit contextual track (LUim-500). To avoid reducing the task to a binary detector score, we define a multi-grained protocol that evaluates both local logo removal and global image preservation in pixel and latent spaces. Experiments on representative inference-time methods, including NP, SLD, and SEGA, and compatible fine-tuning-based methods such as ESD and Forget-Me-Not, show that the evaluated methods struggle to remove logo evidence without changing non-target content. We further analyze ProLU, a prompt-space multi-agent baseline: it improves local erasure by removing logo-inducing semantics, but also illustrates why prompt filtering is not a substitute for weight-level disentanglement. Correlation analyses over logo area, location, and structural complexity suggest that future logo unlearning may need spatially aware controls, such as SSIM-guided constraints, rather than purely global concept suppression.

## Metadata
- **Published**: 2026-07-27T07:40:34Z
- **Authors**: Keyu Li, Jin Gao, Jialing Zhang, Dequan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24101v1)