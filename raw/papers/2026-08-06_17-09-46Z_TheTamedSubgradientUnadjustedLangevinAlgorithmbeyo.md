---
title: The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity
published: 2026-08-06T17:09:46Z
authors: Iosif Lytras, Nikolaos Makras, Sotirios Sabanis
url: http://arxiv.org/abs/2608.06283v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity

## Abstract
We study the problem of sampling from target distributions whose potentials are simultaneously non-smooth, subject to superlinear gradient growth, and non-convex. We introduce the Subgradient Tamed Unadjusted Langevin Algorithm (SG-TULA), a discretisation of the Langevin diffusion that operates directly on subgradients, without relying on computationally demanding smoothing procedures. To handle the superlinear regime, taming techniques are employed to produce a stable, explicit scheme. We derive non-asymptotic convergence bounds in Wasserstein-2 distance, with all constants tracked explicitly in terms of dimension and inverse temperature, improving upon the currently known rates for subgradient-based Langevin algorithms. We further provide excess risk estimates for the associated optimisation problem. We verify the assumptions, with explicit constants, for the regularized pretraining potential of a LLM in the GPT-2 lineage and the boosted coordinate-wise variant of SG-TULA pretrains the former competitively against finetuned AdamW and Muon, for which no comparable non-asymptotic guarantees are presently available.

## Metadata
- **Published**: 2026-08-06T17:09:46Z
- **Authors**: Iosif Lytras, Nikolaos Makras, Sotirios Sabanis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06283v1)