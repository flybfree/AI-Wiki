---
title: Where Quality Breaks in Compressed Short-Text Generation: Staged Bottleneck Localization
published: 2026-07-27T09:02:44Z
authors: Alexey Gavrilov, Alan-Barsag Gazzaev, Sergey Muravyov
url: http://arxiv.org/abs/2607.24176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Quality Breaks in Compressed Short-Text Generation: Staged Bottleneck Localization

## Abstract
Compressed short-text generators can fail in two different places: the codec may discard information before generation starts, or the latent generator may produce weak codes. Without separating these failure modes, researchers can spend compute improving the wrong component. We study this problem in a controlled 64-to-16 TinyStories case study built from a hierarchical VQ-VAE-2 codec and a masked discrete diffusion generator (MDLM). We use a staged validation protocol that separates codec reconstruction fidelity, latent generation quality, and auxiliary latent diagnostics under one shared external GPT-2 scorer, while reporting complementary semantic metrics for the geometry study. In the tested configuration, codec reconstruction alone raises median external perplexity from 15.17 to 27.36 (+80.4%) and p95 from 25.10 to 98.91 (+294.1%), showing that the dominant quality loss appears before latent generation begins. Under the same scorer, code-space MDLM remains materially stronger than token-space diffusion, reducing mean, median, and p95 by 32.9%, 30.9%, and 36.6%, respectively. Geometry-aware regularization improves local latent proxies but does not improve decoded-text metrics in the available runs. The contribution is methodological rather than algorithmic: the paper presents a reusable staged diagnosis for one concrete pipeline and shows that, in this setting, codec fidelity rather than latent denoising sets the practical quality ceiling.

## Metadata
- **Published**: 2026-07-27T09:02:44Z
- **Authors**: Alexey Gavrilov, Alan-Barsag Gazzaev, Sergey Muravyov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24176v1)