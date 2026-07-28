---
title: Physics-Informed Neural Networks for Predicting Nitrous Oxide Flux
published: 2026-07-26T22:53:02Z
authors: Freddy Yu, Jashanjeet Kaur Dhaliwal, Subhadeep Chakraborty
url: http://arxiv.org/abs/2607.23880v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics-Informed Neural Networks for Predicting Nitrous Oxide Flux

## Abstract
Nitrous oxide (N$_2$O) is the dominant ozone-depleting substance emitted in the 21st century, and the third largest contributor to anthropogenic greenhouse gases due to its high potency and long atmospheric lifetime, with more than 70% of N$_2$O emissions occurring as a result of agricultural processes. Current approaches to predicting N$_2$O flux emissions include process-based models such as DayCent and Cycles, as well as classical AI models, but the application of Physics-Informed Neural Networks (PINNs) to predicting N$_2$O flux emissions is largely underexplored. Our paper draws upon the mechanistic equations that underlie the DayCent family of process-based models to construct a rigorously derived, literature-traceable physics residual. We then build and train an MLP-based PINN on a multi-site agricultural dataset spanning four geographically distinct US agricultural sites. Across all tested values of the physics loss weighting hyperparameter $λ$, our PINN consistently and substantially outperformed uncalibrated Cycles simulation (R$^2=0.01$), with our MLP baseline achieving mean R$^2=0.411$ across ten random seeds. Physics constraints consistently degrade model performance in holdout validation, with marginal degradation at low $λ$ and significant degradation at high $λ$, but consistently improve model performance and reduce performance variability in leave-one-site-out validation. This suggests that physics constraints sacrifice in-distribution accuracy for out-of-distribution robustness, anchoring the model toward biogeochemically plausible behavior on unfamiliar soil conditions --- though cross-site generalization remains challenging, with negative R$^2$ across all seeds and $λ$ values on our geographically distinct held-out site.

## Metadata
- **Published**: 2026-07-26T22:53:02Z
- **Authors**: Freddy Yu, Jashanjeet Kaur Dhaliwal, Subhadeep Chakraborty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23880v1)