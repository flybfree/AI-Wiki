---
title: Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal
published: 2026-08-25T17:59:57Z
authors: Philipp E. Glass, Allan Tucker, Yongmin Li, Alina Miron
url: http://arxiv.org/abs/2608.24988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

## Abstract
Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $ρ= 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cosθ= 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

## Metadata
- **Published**: 2026-08-25T17:59:57Z
- **Authors**: Philipp E. Glass, Allan Tucker, Yongmin Li, Alina Miron
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24988v1)