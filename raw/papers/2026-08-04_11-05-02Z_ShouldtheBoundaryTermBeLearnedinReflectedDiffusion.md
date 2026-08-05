---
title: Should the Boundary Term Be Learned in Reflected Diffusion? Conormal Trace and Reflection Masking
published: 2026-08-04T11:05:02Z
authors: Ziyue Wang, Takafumi Kanamori
url: http://arxiv.org/abs/2608.03469v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Should the Boundary Term Be Learned in Reflected Diffusion? Conormal Trace and Reflection Masking

## Abstract
We study score learning for reflected diffusion on bounded domains. Reflection keeps trajectories feasible but does not ensure that the learned score satisfies the boundary behavior implied by the forward process. With implicit score matching, integration by parts leaves a boundary term, and we show that it depends on one scalar at each boundary point: the diffusion- weighted normal component of the score, or conormal trace. The no-flux condition fixes this value while leaving the re- maining boundary components unrestricted; under anisotropic diffusion it generally differs from the ordinary normal score component. On hyperrectangles, our parametrization enforces the required trace without additional trainable parameters or a stochastic boundary estimator and, under regularity assump- tions, can represent the true score, whereas fixing an incorrect value creates an error that more data cannot remove. We ex- tend the construction to simplices and polygonal domains and identify reflection masking: hard reflection can keep samples feasible even when the learned trace is wrong, so post-reflection metrics may hide the error. Experiments show the clearest separation with less frequent reflection, anisotropic diffusion, and mass near intersections of constraints; under full reflection, final sample placement improves inconsistently, illustrating how hard repair can mask boundary-score errors and decouple score accuracy from downstream generation quality.

## Metadata
- **Published**: 2026-08-04T11:05:02Z
- **Authors**: Ziyue Wang, Takafumi Kanamori
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03469v1)