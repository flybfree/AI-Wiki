---
title: Band-Count Dense Modal Estimation with Fixed-Frequency Differentiable Resonator Refinement
published: 2026-08-01T13:42:31Z
authors: Minhui Lu, Joshua D. Reiss
url: http://arxiv.org/abs/2608.00667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Band-Count Dense Modal Estimation with Fixed-Frequency Differentiable Resonator Refinement

## Abstract
Task B of the 1st DAFx Parameter Estimation Challenge requires estimating the frequencies, decay rates, gains, and number of modes in a dense plate-reverb impulse response. Weak and overlapping modes make sparse peak detection prone to severe undercounting. We train an ExtraTrees regressor on simulator-generated data to predict mode counts in four frequency bands. These counts define dense frequency grids, after which a differentiable all-pole resonator model refines decay and gain while keeping frequency fixed. On two separate synthetic validation sets, the system reduces a local challenge-style error by about 66% relative to the official default peak-picking baseline. The improvement is mainly associated with lower mode-count mismatch, while decay and gain remain the largest error sources. These findings support separating modal-density estimation from continuous parameter fitting.

## Metadata
- **Published**: 2026-08-01T13:42:31Z
- **Authors**: Minhui Lu, Joshua D. Reiss
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00667v1)