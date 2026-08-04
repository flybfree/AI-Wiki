---
title: Not the Dimension, the Norm: What Matters in Gradient-Free Weight Perturbation of Language Models
url: http://arxiv.org/abs/2608.01624v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_02-57-20Z_NottheDimension_theNorm_WhatMattersinGradient_Free.md
generated_at: 2026-08-03 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates which aspects of gradient‑free weight perturbation actually drive performance improvements in language models and finds that the norm of the perturbation is the only factor consistently affecting results, while dimension, subspace choice, or basis alignment do not. Experiments show that a frozen frame of 12–16 scalars lags behind full‑weight search by up to 1.8 accuracy points on average, yet neither the number of perturbed entries nor the selected basis explains this gap.

## Key Takeaways
- Full‑weight search outperforms limited‑scale perturbations across most model‑benchmark cells, with the discrepancy persisting even when the subspace and basis are random.
- Matching a single scale factor to the SVD frame yields identical performance to full‑weight search, indicating that alignment alone is insufficient without sufficient norm magnitude.
- The usable range of perturbation norms narrows within a factor of five across seven models, revealing it as the primary failure mode that limits adaptation.

## Context
Current parameter‑efficient adaptation methods rely on gradient‑free sampling but often perturb every weight entry, which is computationally wasteful. Understanding what makes such perturbations effective can reduce training costs and enable scalable fine‑tuning pipelines.

## Implications
Practitioners should focus on controlling the norm of perturbations rather than experimenting with subspace dimensions or basis choices to achieve reliable performance gains in language model adaptation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01624v1)
