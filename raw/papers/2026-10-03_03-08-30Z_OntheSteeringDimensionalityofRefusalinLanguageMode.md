---
title: On the Steering Dimensionality of Refusal in Language Models
published: 2026-10-03T03:08:30Z
authors: Han Wang, Erik Miehling, Dennis Wei, Karthikeyan Natesan Ramamurthy, Huan Zhang
url: http://arxiv.org/abs/2610.04245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Steering Dimensionality of Refusal in Language Models

## Abstract
Existing activation steering methods often assume that a high-level concept can be mediated by a single steering direction. To support this, two complementary interventions should be achieved: additive steering should induce the target behavior, while directional ablation should suppress it. Yet behaviors may occupy richer activation geometries beyond a single direction, and semantically similar behaviors may be represented by distinct directions. In this work, we study how many directions can reliably control two different types of refusal behaviors: refusal triggered by the safety alignment and refusal in general contexts. Given the limited expressive capability of a single steering vector, we study the general setting of steering subspaces and introduce the notion of steering dimensionality as the minimum subspace dimensionality required to reliably control a behavior. We characterize sufficient steering subspaces that cover the full extent of the target behavior through both the (monotonic) improvement before the sufficient dimensionality, and the saturation beyond it. Empirically, we find that refusal triggered by safety alignment is 1-dim steerable, while multiple distinct steering directions can achieve comparable control. In contrast, refusal in general contexts exhibits substantially richer activation geometry where even 5-dim steering subspaces fail to reliably capture its full steerable variation. Our results reveal that the activation geometry underlying refusal is highly context-dependent and can be substantially more complex than a single linear steering direction.

## Metadata
- **Published**: 2026-10-03T03:08:30Z
- **Authors**: Han Wang, Erik Miehling, Dennis Wei, Karthikeyan Natesan Ramamurthy, Huan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04245v1)