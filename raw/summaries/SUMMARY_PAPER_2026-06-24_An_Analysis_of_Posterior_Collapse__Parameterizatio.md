---
title: "Summary: An Analysis of Posterior Collapse, Parameterization and Initialization in Variational Deep Gaussian Processes"
url: http://arxiv.org/abs/2606.25882v1
type: paper-summary
date: 2026-06-24
source_paper: 2026-06-24_14-25-39Z_AnAnalysisofPosteriorCollapse_ParameterizationandI.md
generated_at: 2026-06-24 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates posterior collapse in variational deep Gaussian processes and shows that it is linked to the DSVI algorithm and linear prior mean functions. It proposes an alternative initialization that mimics a linear prior at start, preventing collapse and improving training stability. Experiments confirm that this method yields comparable or better performance than standard DGPs.

## Key Takeaways
- The benefit of using a linear prior mean in all but the last layer stems from conditioning the optimization problem at initialization rather than avoiding non‑injective pathology in deep networks.
- A zero‑prior DGP can be successfully trained by initializing it with a virtual linear prior mean, eliminating the need for optimization‑driven constraints on the prior.
- The whitened parameterization provides more stable convergence and helps avoid posterior collapse, contrary to assumptions that stability is only experiential.

## Context
Variational inference in deep probabilistic models often suffers from posterior collapse, where learned variational posteriors match priors and explain data as noise. This issue hampers the practical deployment of deep GPs despite their strong predictive abilities.

## Implications
For practitioners, adopting this initialization allows flexible prior selection based on modeling assumptions without sacrificing training stability. It also offers a principled way to mitigate collapse in complex hierarchical models, encouraging more robust and interpretable probabilistic AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.25882v1)
