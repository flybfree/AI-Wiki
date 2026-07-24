---
title: Reasoning Fine-Tuning Induces Persistent Latent Policy States
published: 2026-07-20T21:56:22Z
authors: Abir Harrasse, Michael Lan, Hunar Batra, Fateme Hashemi Chaleshtori, Chaithanya Bandi
url: http://arxiv.org/abs/2607.18532v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Fine-Tuning Induces Persistent Latent Policy States

## Abstract
Reasoning-specialized language models show large performance gains over base models, yet the internal changes responsible for improved multi-step reasoning remain poorly understood. It is unclear whether reasoning fine-tuning improves local token-level competence or globally reorganizes how models structure inference over time. We address this question by modeling Chain-of-Thought reasoning as a switching dynamical system (SDS), in which internal representations evolve under discrete latent policy states. Our framework combines time-aware contrastive representation learning with discrete regime discovery to recover latent policies from activation trajectories. Across four benchmarks and model scales from 1.5B to 32B parameters, reasoning-fine-tuned models exhibit richer latent-policy organization than their base counterparts, characterized by more differentiated transition structure and model-dependent changes in state utilization, persistence, and mixing. The recovered regimes exhibit functional specialization aligned with distinct reasoning stages, and extensive controls confirm that their structure is not explained by correctness, representation learning, or modeling priors, but depends on the coherent temporal organization of reasoning trajectories. Causal interventions further show that the regimes are functionally meaningful: state-swap ablations reduce one-step predictive fit, while transplanting reasoning dynamics into base models improves performance on challenging reasoning problems. Finally, SDS-guided pruning of failure-prone reasoning prefixes outperforms self-consistency in 11 of 12 model-dataset settings, with gains of up to 12.5 percentage points. Together, our results suggest that reasoning fine-tuning globally reorganizes latent dynamics, offering a new lens for mechanistic analysis and process-level control of reasoning models.

## Metadata
- **Published**: 2026-07-20T21:56:22Z
- **Authors**: Abir Harrasse, Michael Lan, Hunar Batra, Fateme Hashemi Chaleshtori, Chaithanya Bandi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18532v1)