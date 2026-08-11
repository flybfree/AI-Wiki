---
title: Flow-based conditional cardiac anatomy generation for virtual cohorts
published: 2026-08-10T11:30:02Z
authors: Konstantinos Kevopoulos, Beatrice Moscoloni, Benjamin Alheit, Cameron Beeche, Julio A. Chirinos, Alexander Heinlein, Mathias Peirlinck
url: http://arxiv.org/abs/2608.09460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Flow-based conditional cardiac anatomy generation for virtual cohorts

## Abstract
Cardiac digital twin research is moving from subject-specific anatomical replicas toward virtual cohorts that represent clinically relevant population subgroups. Yet access to representative imaging-derived anatomy datasets remains limited by cohort size, subgroup sparsity, and data-sharing constraints. Conditional generative models could help address this gap, but virtual cohorts are useful only if they preserve realistic, metadata-dependent anatomical variability. Existing cardiac anatomy generators largely rely on conditional variational autoencoders (cVAEs), which couple representation learning and metadata conditioning through a shared regularized latent prior. We introduce CAN-FLOW, a two-step Conditional ANatomy generation framework based on normalizing FLOWs that first learns geometry-only latent representations of diffeomorphic cardiac shape momenta and then models their sex-, age-, and body-mass-index-dependent distribution with a conditional normalizing flow. We trained CAN-FLOW on 2,208 healthy UK Biobank subjects and compared it with cVAEs across regularization strengths. CAN-FLOW generated plausible stochastic biventricular anatomies that better reproduced clinical phenotype distributions, metadata-dependent trends, subgroup variability, point-cloud coverage, and high-dimensional shape variability. Together, these results establish CAN-FLOW as a shareable framework for generating realistic, stochastically varying, metadata-conditioned biventricular anatomies for virtual cohort construction and in silico clinical trial workflows.

## Metadata
- **Published**: 2026-08-10T11:30:02Z
- **Authors**: Konstantinos Kevopoulos, Beatrice Moscoloni, Benjamin Alheit, Cameron Beeche, Julio A. Chirinos, Alexander Heinlein, Mathias Peirlinck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09460v1)