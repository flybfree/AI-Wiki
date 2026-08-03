---
title: Dense Temporal Contrast Synthesis via Conditioned Latent Transport
published: 2026-07-31T13:12:58Z
authors: Smriti Joshi, Apostolia Tsirikoglou, Daniel M. Lang, Richard Osuala, Noah Márquez Varaa, Alejandro Guzman, Grzegorz Skorupko, Sebastian Ibarra Arregui, Lidia Garrucho, Akane Ohashi, Dimitra Ntoula, Eugen Divjak, Oğuz Lafcı, Jan C. Peeken, Julia A. Schnabel, Fredrik Strand, Oliver Diaz, Karim Lekadir
url: http://arxiv.org/abs/2607.29394v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dense Temporal Contrast Synthesis via Conditioned Latent Transport

## Abstract
Dynamic contrast-enhanced magnetic resonance imaging (DCE-MRI) is essential for breast cancer management, but reliance on gadolinium-based contrast agents (GBCAs) restricts use in contraindicated populations, prolongs scan protocols, and presents environmental toxicity concerns. Contrast synthesis offers a non-invasive alternative; however, existing approaches struggle to balance spatial realism with temporal continuity, suffer from slow iterative sampling, underutilize structural priors, and lack clinical validation. We propose a novel conditioned latent transport framework that predicts contrast enhancement in a single forward pass. By anchoring the latent trajectory to the pre-contrast anatomy and applying continuous time conditioning, the model synthesizes patient-specific contrast evolution at any acquisition time. The proposed approach outperforms baseline and the state-of-the-art models across spatial, perceptual, temporal, and distributional metrics. Evaluated on an independent external cohort, the method demonstrates robustness to domain shifts induced by scanner noise as well as differing acquisition protocol. Furthermore, our synthetic contrast enhancement significantly improved downstream tumor segmentation performance, yielding a 22.4% relative increase in Dice coefficient (0.60 vs. 0.49 baseline pre-contrast, p < 0.01), reducing boundary segmentation error by over 39%, while outperforming all other generative model baselines. Finally, a reader study involving four breast radiologists evaluated the image quality, kinetic fidelity, and diagnostic viability of our synthesized sequences across 40 randomly selected cases. The results demonstrated that in 70% of cases, synthesized images provided sufficient clinical information to support the same management decisions as real DCE-MRI, suggesting a path toward safer and faster contrast-free or contrast-reduced imaging workflows.

## Metadata
- **Published**: 2026-07-31T13:12:58Z
- **Authors**: Smriti Joshi, Apostolia Tsirikoglou, Daniel M. Lang, Richard Osuala, Noah Márquez Varaa, Alejandro Guzman, Grzegorz Skorupko, Sebastian Ibarra Arregui, Lidia Garrucho, Akane Ohashi, Dimitra Ntoula, Eugen Divjak, Oğuz Lafcı, Jan C. Peeken, Julia A. Schnabel, Fredrik Strand, Oliver Diaz, Karim Lekadir
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29394v1)