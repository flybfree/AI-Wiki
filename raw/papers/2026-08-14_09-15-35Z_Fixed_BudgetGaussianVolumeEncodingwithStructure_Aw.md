---
title: Fixed-Budget Gaussian Volume Encoding with Structure-Aware Allocation
published: 2026-08-14T09:15:35Z
authors: Michael R. Martin, Joseph Insley, Victor A. Mateevitsi, Silvio Rizzi, Kwan-Liu Ma
url: http://arxiv.org/abs/2608.14112v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fixed-Budget Gaussian Volume Encoding with Structure-Aware Allocation

## Abstract
Scientific simulations often produce scalar volumes faster than they can be stored, transferred, and loaded, while in situ reduction must use only a limited share of simulation resources. This work encodes scalar fields as anisotropic Gaussian primitives under a fixed budget. The complete primitive set is allocated analytically from local field structure, including position, orientation, and shape, then refined directly against the scalar field without densification, pruning, or count changes. The selected budget determines encoded storage before refinement and, together with the iteration schedule, provides a controllable refinement-time budget. In a controlled benchmark, truncation-aware field evaluation reduces encoding time by up to 51x; 1.4 million Gaussians encode a billion-voxel volume in at most four minutes on one desktop GPU, with reduced-iteration refinement completing in under one minute. Across five datasets spanning 2.1 million to 1.1 billion evaluated voxels, compression-useful configurations achieve 15.0-38.7 dB PSNR at compression ratios from 2.2x to over 40,000x. Pre-encoding structure statistics characterize fields for which one-shot allocation yields limited gains from additional capacity. Because primitives retain scalar attributes rather than baked appearance, a single compact model serves every subsequent visualization state - supporting post-hoc transfer-function, colormap, lighting, and viewpoint changes without re-encoding.

## Metadata
- **Published**: 2026-08-14T09:15:35Z
- **Authors**: Michael R. Martin, Joseph Insley, Victor A. Mateevitsi, Silvio Rizzi, Kwan-Liu Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14112v1)