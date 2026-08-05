---
title: GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model
url: http://arxiv.org/abs/2608.03215v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-50-55Z_GROW_Group_RelativeAdvantage_WeightedOn_PolicyRein.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GROW, a group‑relative advantage‑weighted on‑policy reinforcement learning method for flow‑matching text‑to‑speech models that directly optimizes the standard regression objective. By sampling groups of utterances and reweighting rewards within each group, GROW reduces average word error rate from 2.016 to 1.558 while improving speaker similarity without sacrificing UTMOS. The approach also speeds up training by a factor of about three compared with conventional DiTAR‑GRPO.

## Key Takeaways
- GROW replaces trajectory‑level likelihood ratios with group‑wise reward weighting, avoiding stochastic perturbations and large computational overhead in flow‑matching TTS.
- A Wasserstein‑2 velocity penalty keeps the updated model anchored to a frozen pretrained reference, preserving stability during RL updates.
- Positive exponential weighting is replaced by a zero‑mean signed advantage that yields effective within‑group credit assignment for strong pretrained models.

## Context
Flow‑matching text‑to‑speech relies on deterministic ODE sampling, which makes traditional reinforcement learning methods cumbersome due to per‑step likelihood ratio estimation. GROW’s group‑relative approach simplifies this by focusing on aggregate reward reweighting rather than complex trajectory tracking, aligning with the trend toward more efficient and interpretable RL in generative AI.

## Implications
For practitioners developing high‑quality TTS systems, GROW offers a faster training pipeline that maintains or improves perceptual metrics such as speaker similarity. Its open‑source implementation encourages broader adoption of RL techniques across speech synthesis research and industry pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03215v1)
