---
title: Fine-tuned Normalizing Flows for ALICE Zero Degree Calorimeter Fast Simulation
published: 2026-08-13T04:06:01Z
authors: Emilia Majerz, Jacek Otwinowski, Witold Dzwinel, Jacek Kitowski
url: http://arxiv.org/abs/2608.12795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-tuned Normalizing Flows for ALICE Zero Degree Calorimeter Fast Simulation

## Abstract
Simulating the ALICE Zero Degree Calorimeter (ZDC) neutron detector responses at the LHC is computationally expensive, requiring complex Monte Carlo chains. We develop a generative surrogate, focusing on Normalizing Flows (NFs). Through transfer learning, we pre-train on the full imbalanced dataset and fine-tune specialized models for different particle types ($γ$, $n$, $Λ$, $K_S^0$, $Σ^+$) using two gradual-unfreezing schemes. As standard ZDC metrics like Wasserstein distance overlook conditional structure, we introduce refined metrics: conditional weighted MAE, dispersion ratio, and Jaccard co-activation error, that better capture physics-relevant input-output dependencies and response variability. Our ensemble of fine-tuned models achieves a Wasserstein distance of $1.61 \pm 0.02$, outperforming baselines across all metrics. This work provides a generalizable NF-based framework for LHC detector simulation, combining NFs, conditional fine-tuning, and physics-motivated evaluation.

## Metadata
- **Published**: 2026-08-13T04:06:01Z
- **Authors**: Emilia Majerz, Jacek Otwinowski, Witold Dzwinel, Jacek Kitowski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12795v1)