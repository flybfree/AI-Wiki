---
title: ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration
url: http://arxiv.org/abs/2609.00061v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-30_14-13-50Z_ReNFT_RepairingModeCollapseinRewardPost_Trainingvi.md
generated_at: 2026-09-01 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper ReNFT addresses mode collapse in reward post‑training of diffusion generators by repairing an adapter that has collapsed while preserving its high reward. It demonstrates internal probability‑mass recalibration can restore diversity without external signals. Experiments show retained rewards and improved diversity scores on benchmark tasks.

## Key Takeaways
- The paper shows that mode collapse is a suppression rather than deletion, allowing reversal via internal recalibration.
- ReNFT uses unconditional probes to generate counterfactual proposals from the same prompt and noise, exposing suppressed alternatives and post‑trained tendencies.
- Adaptive reward ranking with flipping guard enables joint‑and‑paired NFT updates that repair adapters while maintaining reward levels.

## Context
Diffusion models often suffer from mode collapse after reward fine‑tuning, limiting diversity in generated images. Traditional solutions depend on external objectives or interface modifications, which do not repair existing adapters. This work focuses on internal mechanisms to fix collapsed behavior without changing the model architecture.

## Implications
ReNFT offers a practical method for maintaining high‑quality reward signals while preserving prompt diversity, benefiting researchers and practitioners aiming for robust generative models. By repairing adapters internally, it reduces reliance on costly external interventions and supports scalable fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00061v1)
