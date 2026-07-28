---
title: Agentic Autoresearch for CT Reconstruction
published: 2026-07-24T18:03:21Z
authors: Andreas Maier, Lucas Kachelriess, Siming Bayer, Yixing Huang, Yan Xia, Amber Simpson, Moritz Zaiss
url: http://arxiv.org/abs/2607.22824v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Autoresearch for CT Reconstruction

## Abstract
Comparing CT reconstruction methods fairly is labor-intensive and largely manual, and many benchmarks use idealized data. We ask whether a large language model (LLM) agent can do the labor of reconstruction research on its own, and whether a ranking measured on ideal data predicts behavior under realistic noise.   We built an agentic loop: the agent edits a solver, runs a short cluster job, reads one frozen metric, and revises. The metric is a calibrated headroom score against the FBP baseline, inside the field of view; every method shares the same differentiable fan-beam projector. We benchmarked 26 methods on Mayo low-dose CT (noise-limited) and a 128-view sparse-view breast task from the noiseless DL-Sparse-View Challenge, with validation-selected iterations scored on a held-out test set. Every trained breast model was then re-scored on noisy inputs (I_0 = 10^5 photons) without retraining, and separately retrained on matched noise.   The agent independently implemented, tuned, and benchmarked all 26 methods, and recombined them into a compact solver of 969 parameters that ties the top Mayo tier at the 1% level using 0.4% of the champion's parameters. Benchmarking gives a tier of statistically indistinguishable top methods, not one winner. Mild input noise nearly inverts the breast ranking: the noiseless champion (a supervised image denoiser, hr 0.89) collapses to 0.00, while a learned primal-dual method rises to champion (0.72 to 0.93).   An ideal-data leaderboard therefore does not predict robustness. The inversion is a transfer effect, not a permanent deficit: retraining on matched noise restores much of the clean ranking (Spearman rho 0.04 to 0.61). Noise is only the easiest confounder in an open-ended set (beam hardening, scatter, anatomy, disease), so no single-factor challenge certifies generality. Benchmarks should model a broad spectrum of realistic factors at once.

## Metadata
- **Published**: 2026-07-24T18:03:21Z
- **Authors**: Andreas Maier, Lucas Kachelriess, Siming Bayer, Yixing Huang, Yan Xia, Amber Simpson, Moritz Zaiss
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22824v1)