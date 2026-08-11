---
title: The Cost of Adaptivity: Matching Lower Bounds Across Learning Problems
published: 2026-08-09T17:19:11Z
authors: Ibne Farabi Shihab, Adria Binte Habib
url: http://arxiv.org/abs/2608.08826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Cost of Adaptivity: Matching Lower Bounds Across Learning Problems

## Abstract
Adaptive procedures must work without nuisance information an oracle may use, such as a gradient scale or smoothness index, and robust procedures may have to answer queries whose coordinate and inspection time are chosen only after the data are seen. Such comparisons are meaningful only when the oracle advantage and validity contract are stated explicitly. We formalize nuisance adaptation via a slice-normalized minimax ratio retaining the worst-case instance within each nuisance slice, and separately define the robustness cost of expanding from one preannounced Gaussian query to arbitrary post-hoc inspection. Our main result is a finite-horizon composition law for Gaussian certification: from M independent coordinates, a familywise certifier protecting every coordinate and time up to T pays optimal normalized squared half-width of order log(eM) + log log(e^eT), within the sample-mean-centered rectangular class. Epoch stitching gives the upper bound; independent Gaussian block increments across coordinates and geometric time scales give a matching lower bound, already holding on a geometric checkpoint grid, forcing quantiles of the realized maximum width so selection and stopping taxes add. Two benchmark regimes complete the picture: unknown gradient scale in online convex optimization has constant cost, while pointwise adaptation over nested Holder classes costs order (log n / log log n)^(s1/(2s1+1)). Cast as model monitoring, the law lets an analyst inspect any of M slice metrics at any data-dependent time: the naive fixed-query band's selected coverage degrades sharply, to 0.30 at M=1 and to zero for M>=10, while the epoch-stitched certifier holds familywise coverage at an additive iterated-logarithm width cost. Experiments put both sharp predictions at risk of refutation; both survive.

## Metadata
- **Published**: 2026-08-09T17:19:11Z
- **Authors**: Ibne Farabi Shihab, Adria Binte Habib
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08826v1)