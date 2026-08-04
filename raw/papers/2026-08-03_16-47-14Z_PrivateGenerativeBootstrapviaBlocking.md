---
title: Private Generative Bootstrap via Blocking
published: 2026-08-03T16:47:14Z
authors: Jinwon Sohn, Veronika Ročková
url: http://arxiv.org/abs/2608.02480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Private Generative Bootstrap via Blocking

## Abstract
With AI systems gaining more access to individuals' information, it is important to protect privacy when reporting statistical answers. Equally important is to privatize the reporting of uncertainty in such answers. To this end, we adopt a Bayesian likelihood-free framework and make simulation from the posterior private. In particular, we propose a new private instantiation of the Bayesian bootstrap using a blocking strategy. Rather than assigning idiosyncratic random weights to each individual, we randomly group individuals and assign a single weight to each group. By concealing individuals' contributions within a group, we fortify differential privacy gates. We harness amortized inference that decouples private learning from posterior sampling. A push-forward map from observation weights to posterior samples is learned privately by adding calibrated noise during training. Subsequent posterior draws require no additional privacy and computation budget. We call the resulting method the Private Generative Bayesian Bootstrap (PGBB). We establish a differential privacy guarantee, analyze convergence to the non-private blocked-bootstrap target, and quantify the discrepancy between the ordinary and blocked Bayesian-bootstrap posteriors. In addition, we derive data-free tuning of the block Dirichlet concentration parameter that restores posterior dispersion asymptotically. We also show a single fit of PGBB can support a family of loss-based decision rules simultaneously without additional privacy cost. In simulations and in applications to U.S. Census returns to schooling and U.S. natality birthweight quantiles, PGBB gives competitive private uncertainty quantification and improves over private Bayesian alternatives that require a specified data-generating model in common settings.

## Metadata
- **Published**: 2026-08-03T16:47:14Z
- **Authors**: Jinwon Sohn, Veronika Ročková
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02480v1)