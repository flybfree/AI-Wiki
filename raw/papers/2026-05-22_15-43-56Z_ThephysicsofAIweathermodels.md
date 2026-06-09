---
title: The physics of AI weather models
published: 2026-05-22T15:43:56Z
authors: George Craig, Tobias Selz, Matthias Beylich, Kirsten I. Tempest
url: http://arxiv.org/abs/2605.23778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The physics of AI weather models

## Abstract
Could it be that AI weather models are solving physical equations, although they may not be the equations used by conventional NWP models? We compute correlations of forecast skill and Centered Kernel Alignment, providing evidence that different AI weather models represent the atmosphere in similar ways, despite differences in architecture and capacity. We argue that the architecture and training of the AI models constrains the form of the physical laws that they might simulate. In particular, we propose that the models implement a particle description of the atmosphere, where the latent variables at each mesh point correspond to the position of a particle in the high dimensional latent space. We hypothesize that the movement of the particles follows a gradient flow in the latent space towards a minimum of a learned free energy functional. Analysis of the GraphCast and Aurora models show that they make changes on large spatial scales in the early processor layers and move to smaller scale with increasing layer depth, consistent with the gradient flow hypothesis.

## Metadata
- **Published**: 2026-05-22T15:43:56Z
- **Authors**: George Craig, Tobias Selz, Matthias Beylich, Kirsten I. Tempest
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23778v1)