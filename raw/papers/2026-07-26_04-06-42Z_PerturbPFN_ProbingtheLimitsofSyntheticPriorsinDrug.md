---
title: PerturbPFN: Probing the Limits of Synthetic Priors in Drug Perturbation Modelling
published: 2026-07-26T04:06:42Z
authors: Yuche Gao, José Miguel Hernández-Lobato, Siyuan Guo
url: http://arxiv.org/abs/2607.23447v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PerturbPFN: Probing the Limits of Synthetic Priors in Drug Perturbation Modelling

## Abstract
Predicting cellular responses to unseen chemical perturbations is challenging due to unknown targets and mechanisms, high-dimensional expression responses, and limited experimental coverage of the large small-molecule design space. We propose PerturbPFN, a PFN-style amortized model for unknown-target perturbation prediction under a hierarchical synthetic structural prior. Instead of directly regressing high-dimensional expression responses, PerturbPFN infers a latent system graph, sparse atomic intervention targets, and intervention strengths, then propagates their effects through an SCM decoder. The model is trained entirely on prior-predictive synthetic episodes generated from biologically motivated graph and expression simulators, enabling structured in-context learning without test-time gradient updates. We evaluate PerturbPFN on both real single-cell perturbation data and synthetic benchmarks, covering effect prediction, target identification, and regulatory structure discovery. Our results show that PerturbPFN offers a complementary trade-off to specialized baselines, achieving competitive perturbation prediction with low inference cost while exposing interpretable intermediate estimates of targets, strengths, and system structure.

## Metadata
- **Published**: 2026-07-26T04:06:42Z
- **Authors**: Yuche Gao, José Miguel Hernández-Lobato, Siyuan Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23447v1)