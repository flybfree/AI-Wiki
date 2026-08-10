---
title: How Molecular Generative Models Organize Molecular Identity
published: 2026-08-07T08:32:13Z
authors: Raul Ortega-Ochoa, Tejs Vegge, Jens S. Bakander, Luis Mantilla Calderon, Alan Aspuru-Guzik, Tonio Buonassisi
url: http://arxiv.org/abs/2608.06956v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Molecular Generative Models Organize Molecular Identity

## Abstract
Generative models for matter are often evaluated as samplers over output representations, and their latent spaces are commonly used as proxies for navigating chemical space. Much less is known about how these models internally arrange discrete chemical identities within those representations. We study this arrangement by making molecular identity explicit and pulling it back through the generative process. Through these pullbacks we probe the regions that generate the same object, exposing the trained model's internal repertoire: a fixed partition that determines which objects (novel or not) the model can produce.   Across three molecular generative architectures, we find that this repertoire is arranged into piecewise-constant regions separated by recurring coarse-to-fine boundaries. Its organization depends on the representation probed, the identity convention, decoder stochasticity, and the metric used to compare coordinates. During training, local chemical organization stabilizes while the number of distinct molecular identities represented within each neighborhood continues to change. Internal organization must therefore be characterized, rather than assumed, before a generative space can be treated as chemically navigable.

## Metadata
- **Published**: 2026-08-07T08:32:13Z
- **Authors**: Raul Ortega-Ochoa, Tejs Vegge, Jens S. Bakander, Luis Mantilla Calderon, Alan Aspuru-Guzik, Tonio Buonassisi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06956v1)