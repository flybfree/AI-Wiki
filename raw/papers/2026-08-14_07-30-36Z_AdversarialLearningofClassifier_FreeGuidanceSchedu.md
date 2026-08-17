---
title: Adversarial Learning of Classifier-Free Guidance Schedules
published: 2026-08-14T07:30:36Z
authors: Ashwini Pokle, Alexandre Galashov, Arnaud Doucet, Mauricio Delbracio, Valentin De Bortoli
url: http://arxiv.org/abs/2608.14038v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Learning of Classifier-Free Guidance Schedules

## Abstract
Modern text-to-image diffusion models rely on classifier-free guidance (CFG) to achieve high image fidelity and text alignment. However, CFG typically applies a static, global scale across all timesteps, samples, and conditions -- a choice that is generally suboptimal and can introduce artifacts, as different states may benefit from different levels of guidance. While time-varying schedules are known to improve quality, designing them by hand is non-trivial and application-dependent. In this paper, we learn the guidance schedule as a function of diffusion time, conditioning and the current noisy sample, in order to better align sampled images with the text prompt. We frame this as a density ratio estimation problem: a discriminator is trained to estimate the time-dependent log-density ratio between the true and guided marginal distributions, while a lightweight generator network predicts the optimal, state-dependent guidance scale. Empirically, our approach outperforms both heuristic CFG schedules and prior methods for learning dynamic guidance on text-to-image generation benchmarks.

## Metadata
- **Published**: 2026-08-14T07:30:36Z
- **Authors**: Ashwini Pokle, Alexandre Galashov, Arnaud Doucet, Mauricio Delbracio, Valentin De Bortoli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14038v1)