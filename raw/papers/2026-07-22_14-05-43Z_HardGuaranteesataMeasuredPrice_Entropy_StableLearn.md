---
title: Hard Guarantees at a Measured Price: Entropy-Stable Learned Finite Volumes for Compressible Flow
published: 2026-07-22T14:05:43Z
authors: Denis Gueyffier
url: http://arxiv.org/abs/2607.20171v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hard Guarantees at a Measured Price: Entropy-Stable Learned Finite Volumes for Compressible Flow

## Abstract
Learned solvers for compressible flow are usually compared to classical methods at equal mesh resolution rather than at equal computational cost, and they typically offer no guarantee that their solutions remain physically admissible. We present a learned finite volume scheme for the two-dimensional Euler equations on unstructured meshes, admissible by construction and with an entropy-stable interior flux. We evaluate it under protocols fixed before any computation: frozen thresholds, falsification clauses, negative controls, a factor decomposition of the learned components, and an iso-cost comparison against the refined classical baseline. The decomposition produced the central result: the guarantee machinery alone, with both learned heads switched off (the unlearned skeleton), is the strongest scheme at equal mesh on every periodic case. At equal wall-clock cost the picture inverts into a map. Learning pays robustly only on the wall case whose boundary-condition type it never saw (10.8%). Its periodic gains flip sign with the evaluation draw (+10% on one held-out case, -12% on the hardest). The skeleton is the only method whose iso-cost gain never changes sign, at a measured overhead of 1.74x per step. The guaranteed variant completes 36 of 36 rollouts, Mach extrapolation and unseen wall included, with zero negativity events. We fix the guaranteed scheme's one remaining out-of-distribution weakness, Mach extrapolation, at inference time: with scale-invariant network inputs, a specific-entropy floor, and no retraining, the corrected arm overtakes the unconstrained arm on one Mach case, cuts its deficit on the other by a third, passes the skeleton on the unseen wall, and keeps the guarantee. A spatial gate closes the loop: activating the heads only near the walls beats both the skeleton and the corrected arm, and transfers unchanged to a second wall geometry.

## Metadata
- **Published**: 2026-07-22T14:05:43Z
- **Authors**: Denis Gueyffier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20171v1)