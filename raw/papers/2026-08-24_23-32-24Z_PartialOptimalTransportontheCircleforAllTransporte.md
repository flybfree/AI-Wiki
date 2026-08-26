---
title: Partial Optimal Transport on the Circle for All Transported Masses in O(N log N)
published: 2026-08-24T23:32:24Z
authors: Soheil Kolouri
url: http://arxiv.org/abs/2608.23910v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Partial Optimal Transport on the Circle for All Transported Masses in O(N log N)

## Abstract
Partial optimal transport compares two measures while leaving part of the mass unmatched, which is what makes it robust to outliers, occlusion, and clutter. The quantity of interest is usually the whole profile - the optimal cost at every transported cardinality - because the right amount to transport is rarely known in advance, and on the real line the PAWL algorithm returns that profile in $O(N\log N)$. Much data is periodic rather than linear: angles, phases, orientations, time of day, hue, and every direction obtained by projecting onto a great circle. On the circle the same problem acquires a global circulation, or equivalently an optimized cut, which the naive exact method handles by running the line algorithm once per support gap, at $O(N^{2}\log N)$. We show that this factor $N$ is unnecessary. The line structure survives in cut-free form, and a free-gap invariant supplies, at every step, a cut at which all previous local updates remain valid line updates. This yields PAWC: an exact $O(N\log N)$ time, $O(N)$ memory algorithm returning all $K+1$ costs, nested active sets and plans in one run, together with a single gap that is simultaneously optimal for every cardinality. Slicing over great circles extends it to $\mathbb{S}^{d-1}$. Empirically the whole profile costs $0.56$ms at $N=4096$ against $1.5$s for a single transported fraction from a general solver; on occluded, cluttered mpeg-7 shapes, holding the descriptor fixed and varying only the cost, it retains $66\%$ of the clean-data retrieval score against $16\%$ for balanced circular OT, and on $\mathbb{S}^{2}$ it halves the fitting error of spherical sliced Wasserstein against contaminated targets, synthetic and real. Code is available at https://github.com/mint-vu/Partial_Wasserstein_on_Circles.

## Metadata
- **Published**: 2026-08-24T23:32:24Z
- **Authors**: Soheil Kolouri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23910v1)