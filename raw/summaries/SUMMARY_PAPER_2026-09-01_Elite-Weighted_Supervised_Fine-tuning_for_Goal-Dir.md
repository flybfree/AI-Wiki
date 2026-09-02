---
title: Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization
url: http://arxiv.org/abs/2609.00189v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-10-51Z_Elite_WeightedSupervisedFine_tuningforGoal_Directe.md
generated_at: 2026-09-01 22:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Elite‑Weighted Supervised Fine‑tuning (EW‑SFT), a method for goal‑directed molecular optimization that leverages reward information to select elite molecules and updates the model using only their native loss. The approach works across various generative architectures and design tasks, consistently outperforming native optimizers under limited 3D shape oracle calls.

## Key Takeaways
- Reward is used solely for elite selection rather than continuous weighting within the selected set, simplifying the optimization process.
- EW‑SFT can be applied to autoregressive, masked‑diffusion, and discrete‑flow generators without architectural changes.
- Under a fixed budget of 3D shape alignment oracle calls on two kinase references, EW‑SFT outperforms corresponding native optimizers.

## Context
The work addresses the challenge of reusability in molecular generation by decoupling reward guidance from architecture‑specific log probabilities. By focusing on supervised fine‑tuning with elite molecules, it reduces reliance on complex reinforcement learning pipelines that are difficult to maintain across different models.

## Implications
EW‑SFT offers a unified optimizer that can be deployed across diverse generative tasks and reference compounds, lowering development costs for drug discovery teams. Practitioners can achieve high performance without building custom RL frameworks, accelerating the design of novel molecules with specific properties.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00189v1)
